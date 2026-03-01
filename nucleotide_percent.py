#!/usr/bin/env python3
# Compute nucleotide percentages for a DNA or RNA sequence.

from collections import Counter

def nucleotide_percent(seq: str) -> dict:
# Convert sequence to uppercase and remove spaces and newline characters
    seq = seq.upper().replace(" ", "").replace("\n", "")
# Define valid nucleotide characters
    valid = set("ACGTU")
# Check for invalid characters in the sequence
    if any(ch not in valid for ch in seq):
# Identify which invalid characters were found
        bad = sorted(set(ch for ch in seq if ch not in valid))
        raise ValueError(f"Invalid characters found: {bad}")

    total = len(seq)
	if total == 0:  # Handle empty sequence gracefully
        raise ValueError("Sequence is empty")
    # Count occurrences of each nucleotide using Counter
    counts = Counter(seq)

    # Return percentages for each nucleotide in alphabetical order
    # Only include nucleotides actually present in the sequence
    return {base: 100 * counts[base] / total for base in sorted(counts)}

if __name__ == "__main__":
# Prompt user to input a DNA or RNA sequence
    s = input("Enter DNA/RNA sequence: ")
# Compute nucleotide percentages   
 perc = nucleotide_percent(s)
# Print results neatly with two decimal places
    print("Nucleotide percentages for the given sequence:")
    for k, v in perc.items():
        print(f"{k}: {v:.2f}%")
