import sys
import os
import glob
import argparse

# Application version
version = "1.0-alpha"
verbose = False
extension = "jpg"
start = 0

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
            print("idx must be a numbrer")
            sys.exit()

    if pfx is None:
        pfx = ""

    if verbose:
        print("  Path: {}".format(os.getcwd()))
        print("  Extension: {}".format(ext))
        print("  Start: {}".format(idx))
        print("  Prefix: {}".format(pfx))
        print("  Recursive: {}".format(r))
    
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
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Help from the script to establish metadata.")

    parser.add_argument("--version", help="Show the version of the script", action="store_true")
    parser.add_argument("--verbose", help="Shows detailed information of the processes", action="store_true")
    parser.add_argument("--rename", help="Rename PATH files. Default: 0001.jpg", metavar="PATH")
    parser.add_argument("--ext", help="Extension of the files to be processed. Default: jpg", metavar="EXTENSION")
    parser.add_argument("--idx", help="Start number to rename. Default: 0001", metavar="START")
    parser.add_argument("--pfx", help="Prefix to rename. Default: none", metavar="PREFIX")

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
    if args.rename:
        rename(args.rename, args.ext, args.idx, args.pfx)
        sys.exit()