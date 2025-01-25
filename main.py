def count_words(text):
    words = text.split()
    return len(words)
def count_characters(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1 
    return char_count  

def sort_on(dict):
    return dict["count"]


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        word_count = count_words(file_contents)
        print(f"{word_count} words found in the document\n")

        character_count = count_characters(file_contents)
        chars_list = []
        for char, count in character_count.items():
            chars_list.append({"char": char, "count": count})

        chars_list.sort(reverse=True, key=sort_on)

        for char_dict in chars_list:
            print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")

        print("--- End report ---")
                        
if __name__ == "__main__":
    main()