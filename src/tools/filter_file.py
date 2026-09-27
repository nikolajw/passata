def main():
    input_file = "src/passata/words1.txt"
    output_file = f"{input_file}_filtered.txt"

    with open(input_file, "r") as f:
        lines = f.readlines()

    filtered_lines = [line for line in lines if 4 <= len(line.strip()) <= 8 and line.strip().isalpha()]

    with open(output_file, "w") as f:
        f.writelines(filtered_lines)

    print(f"Kept {len(filtered_lines)} of {len(lines)} words")


def next():
    input_file = "src/tools/eff_large_wordlist.txt"
    output_file = "words2.txt"

    with open(input_file, "r") as f:
        lines = f.readlines()

    filtered_lines = [
        line for line in lines
        if len(line.strip().split()) == 2 and 4 <= len(line.strip().split()[1]) <= 8
    ]

    with open(output_file, "w") as f:
        f.writelines(filtered_lines)

    print(f"Kept {len(filtered_lines)} of {len(lines)} words")


if __name__ == "__main__":
    next()
