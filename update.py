#!/usr/bin/python3
import os

os.system("cp slides_src/lecture1.pdf slides/lecture1.pdf")
os.system("cp slides_src/lecture2.pdf slides/lecture2.pdf")
os.system("cp slides_src/lecture3.pdf slides/lecture3.pdf")

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--m",default="Update",
        help='Message')

args = parser.parse_args() # get the arguments

os.system("git add .")
os.system("git commit -m \"" + args.m+ "\"")
os.system("git push")
