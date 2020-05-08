import sys
import os
import argparse

# Application version
version = "1.0-alpha"
verbose = False

if __name__ == "__main__":
	parser = argparse.ArgumentParser("Help from the script to establish metadata.")

	parser.add_argument("--ver", help="Show the version of the program", action="store_true")
	parser.add_argument("--verbose", help="Shows detailed information of the processes", action="store_true")

	args = parser.parse_args()

    # verbose
	if args.verbose:
		verbose = True
		if verbose:
			print("Verbose mode is on.")
	
    # ver
	if args.ver:
		if verbose:
			print("The script version is: {}".format(version))
		else:
			print(version)
		sys.exit()