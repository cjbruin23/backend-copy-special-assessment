#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import argparse

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
    special_array = []

    for cfile in os.listdir(dir):
        found = re.search(r'__\w+__', cfile)
        if found:
            special_array.append(os.path.abspath(cfile))
    print "\n".join(special_array)
    return special_array

# New dir should have a '.' for creating new folders
# from current directory
def copy_to(paths, new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    for cfile in paths:
        shutil.copy(cfile, new_dir)
    return 

def zip_to(paths, new_dir):
    print "Command I'm going to do:"
    cmd_to_run = "zip -j " + new_dir
    for a_path in paths:
        cmd_to_run += " " + a_path 
    print cmd_to_run
    os.system(cmd_to_run)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('dir', help='prints current directories special files')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions
    if not args:
        parser.print_usage()
        sys.exit(1)
    
    special_array = get_special_paths(args.dir)

    if args.todir:
        copy_to(special_array, args.todir)
    if args.tozip:
       zip_to(special_array, args.tozip)
    

        
    return
  
if __name__ == "__main__":
    main()
