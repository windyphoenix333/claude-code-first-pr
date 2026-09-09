import sys
from collections import Counter


def word_counts(text):
    words = text.lower().split()
    return Counter(words)


def main():
    if len(sys.argv) != 2:
        print("Usage: python word_count.py <file>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        text = f.read()

    counts = word_counts(text)
    for word, count in counts.most_common(10):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
