#!/usr/bin/python
from string import maketrans
import sys
import argparse 


ap = argparse.ArgumentParser()
group = ap.add_mutually_exclusive_group(required=True)
group.add_argument('-s', nargs=1) # Specify the string to decode

opts = ap.parse_args()


if opts.s:
        str = opts.s[0]
	intab = "abcdefghijklmnopqrstuvwxyz"
	outtab = "zyxwvutsrqponmlkjihgfedcba"
	trantab = maketrans(intab, outtab)
	print str.translate(trantab)
