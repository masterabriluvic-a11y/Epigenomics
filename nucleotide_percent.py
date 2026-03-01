#!/usr/bin/env python3
# Compute nucleotide percentages for a DNA or RNA sequence.

from collections import Counter

def nucleotide_percent(seq: str) -> dict:
    seq = seq.upper().replace(" ", "").replace("\n", "")
    valid = set("ACGTU")
    if any(ch not in valid for ch in seq):
        bad = sorted(set(ch for ch in seq if ch not in valid))
        raise ValueError(f"Invalid characters found: {bad}")

    total = len(seq)
    counts = Counter(seq)
    return {base: 100 * counts[base] / total for base in sorted(counts)}

if __name__ == "__main__":
    s = input("Enter DNA/RNA sequence: ")
    perc = nucleotide_percent(s)
    for k, v in perc.items():
        print(f"{k}: {v:.2f}%")