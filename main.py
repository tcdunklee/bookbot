from stats import get_num_words,sort_character_list
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(len(sys.argv))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(sys.argv[1])} total words")
    print("--------- Character Count -------")
    character_dictionary = sort_character_list(sys.argv[1])
    for pair in character_dictionary:
        if pair["char"].isalpha():
            print(f"{pair["char"]}: {pair["num"]}")
    print("============= END ===============")

main()

