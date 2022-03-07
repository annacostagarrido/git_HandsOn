#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()                 # Sequence in upper case

if re.search('^[ACGTUN]+$', args.seq): # If the seq contains these characters is DNA or RNA
    if "U" not in args.seq and "T" in args.seq: # If the seq contains T but not U, is DNA
        print ('DNA')
    elif "T" not in args.seq and "U" in args.seq: # If the seq contains U but not T, is RNA
        print ('RNA')
    else:
        print ('DNA or RNA') 
else:
    print ('The sequence is not DNA nor RNA')


if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq): # see if the sequence contains a given motif
        print("FOUND!")
    else:
        print("NOT FOUND MOTIF")
