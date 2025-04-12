from stats import count_words, char_counts, dictionary_list


def get_book_text(filepath):

    with open(filepath) as f:
        return f.read()



def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)

    counts_list = dictionary_list(char_counts(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for count in counts_list:
        print(f"{count['char']}: {count['count']}")
    print("============= END ===============")
    
if __name__ == "__main__":
    main()