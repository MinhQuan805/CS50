import csv
import sys


def main():

    # TODO: Check for command-line usage
    try:
        if len(sys.argv) != 3:
            sys.exit("No match command-line usage")
        elif not sys.argv[1].startswith("databases/") or not sys.argv[2].startswith("sequences/"):
            sys.exit("Incorrect file path")
    except FileNotFoundError:
        sys.exit("File Not Found")
    # TODO: Read database file into a variable
    l = []
    with open(sys.argv[1]) as data:
        sub = csv.DictReader(data)
        dna = sub.fieldnames
        for row in sub:
            l.append(row)
    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as file:
        sequence = file.read().strip()
    # TODO: Find longest match of each STR in DNA sequence
    for i in range(1, len(dna)):
        longest = longest_match(sequence, dna[i])
        store = []
        for row in l:
            if row[dna[i]] == str(longest):
                store.append(row)
        l = store
        if len(l) == 0:
            print("No match")
            return 1
    if len(l) == 1:
        print(l[0]['name'])
        return 0
    # TODO: Check database for matching profiles


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
