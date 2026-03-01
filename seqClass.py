#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# FIX: Accept lower-case sequences by converting everything to upper-case
args.seq = args.seq.upper()

# FIX: Validate that the sequence contains only valid nucleotides (A,C,G,T,U)
if re.search(r'^[ACGTU]+$', args.seq):
    has_t = 'T' in args.seq
    has_u = 'U' in args.seq

    # FIX: A biological sequence cannot contain both T and U at the same time.
    # If it does, it cannot be classified as DNA or RNA.
    if has_t and has_u:
        print("The sequence is not DNA nor RNA (contains both T and U)")
    elif has_t:
        print("The sequence is DNA")
    elif has_u:
        print("The sequence is RNA")
    else:
        print("The sequence can be DNA or RNA")
else:
    print("The sequence is not DNA nor RNA (invalid characters found)")

# Motif search (optional)
if args.motif:
    # Keep motif search case-insensitive by normalizing to upper-case
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")