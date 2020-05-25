import sys
import os
import glob
import argparse
import json

# ------------------ Default values ------------------
# Application version
version = "1.0-alpha"

# Verbose mode off
verbose = False

# Default extension
extension = "jpg"

# Default start
start = 0

# ------------------ Commands ------------------
# Preformatted exiftool commands
SET_MD_EXIFTOOL_CMD = """exiftool -overwrite_original \\
        -title=\"{}\" -description=\"{}\" \\
        -AllDates=\"{}\" -FileModifyDate=\"{} {}\" \\
        -keywords=\"{}\" \\
        -GPSLatitude=\"{}\" -GPSLatitudeRef=\"{}\" -GPSLongitude=\"{}\" -GPSLongitudeRef=\"{}\" \\
        {}*.{}"""

DEL_MD_EXIFTOOL_CMD = ""


# ------------------ Logical ------------------

# Implements rename options
def rename(path, ext, idx, pfx):
    os.chdir(path)

    if ext is None:
        ext = extension
    else:
        ext = ext.replace("*","")
        ext = ext.replace(".","")

    if idx is None:
        idx = start
    else:
        try:
            idx = int(idx)
        except:
            print("idx must be a numbrer!")
            sys.exit()

    if pfx is None:
        pfx = ""

    if verbose:
        print("  Path: {}".format(os.getcwd()))
        print("  Extension: {}".format(ext))
        print("  Start: {}".format(idx))
        print("  Prefix: {}".format(pfx))
    
    if idx == 0:
        count = 1
    else:
        count = idx
    
    total_renamed = 0

    for filename in glob.glob("*." + ext):
        renamed = pfx + str(count).zfill(4) + "." + ext
        os.rename(filename, renamed)
        count += 1
        total_renamed += 1        

    print("Renamed {} files!".format(total_renamed))
    
# Implements set metadata options
def metadata(jsonfile, albumid, ext):

    if os.path.exists(jsonfile) == False:
        print("The {} file does not exist!".format(jsonfile))
        sys.exit()

    if ext is None:
        ext = extension
    else:
        ext = ext.replace("*","")
        ext = ext.replace(".","")

    with open(jsonfile) as info:
        d = json.load(info)
        if verbose:
            print("  PATH: {}".format("jsonfile"))
            print("  YEAR: {}".format(d["year"]))
            print("  ID: {}".format(d["id"]))

        found = False
        for a in d["albumes"]:
            if a["id"] == albumid:
                found = True
                set_metadata_album(jsonfile, a, ext)
        if found == False:
            print("The Album ID {} does not exist!".format(albumid))


def set_metadata_album(path, album, ext):
    path = os.path.dirname(os.path.abspath(path)) + "/" + album["name"] + "/"

    if verbose:
        print("    PATH: {}".format(path))
        print("    EXTENSION: {}".format(ext))
        print("    ALBUM ID: " + album["id"])
        print("    NAME: " + album["name"])
        print("    PHOTOS: " + album["photos"])
        print("    VIDEOS: " + album["videos"])

    
    keys = album["keys"]["what"] + ";" + album["keys"]["who"] + ";" + album["keys"]["where"] + ";" + album["keys"]["owner"]
    cmd = SET_MD_EXIFTOOL_CMD.format(
        album["title"], album["description"], 
        album["date"], album["date"], album["time"],
        keys, album["gps"]["latitude"]["lat"], 
        album["gps"]["latitude"]["dir"], album["gps"]["longitude"]["lon"], album["gps"]["longitude"]["dir"],
        path, ext)
    
    os.system(cmd)
    print("    For the album: '{}'".format(album["name"]))


# ------------------ Menu ------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser("Help from the script to establish metadata.")

    parser.add_argument("--version", help="Show the version of the script", action="store_true")
    parser.add_argument("--verbose", help="Shows detailed information of the processes", action="store_true")
    
    parser.add_argument("-r", help="Rename PATH files. Default: 0001.jpg", metavar="PATH")
    parser.add_argument("--idx", help="Start number to rename. Default: 0001", metavar="START")
    parser.add_argument("--pfx", help="Prefix to rename. Default: none", metavar="PREFIX")

    parser.add_argument("-m", help="Set metada, Album ID, from info file", metavar=("JSON FILE", "ALBUM ID"), nargs=2)   

    
    parser.add_argument("--ext", help="Extension of the files to be processed. Default: jpg", metavar="EXTENSION")


    

    args = parser.parse_args()

    # verbose
    if args.verbose:
        verbose = True
        if verbose:
            print("Verbose mode is on.")

    # ver
    if args.version:
        if verbose:
            print("The script version is: {}".format(version))
        else:
            print("Version: ", version)
        sys.exit()

    # rename
    if args.r:
        rename(args.r, args.ext, args.idx, args.pfx)
        sys.exit()

    # metadata
    if args.m:
        metadata(args.m[0], args.m[1], args.ext)
        sys.exit()