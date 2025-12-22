import sys
from stats import count_words, count_characters, chars_dict_to_sorted_list

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = args[1]

    with open(book_path) as f:
        text = f.read()

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    chars_dict = count_characters(text)
    sorted_chars = chars_dict_to_sorted_list(chars_dict)

    for item in sorted_chars:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
