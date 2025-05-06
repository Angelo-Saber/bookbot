import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 
from stats import sorted_list
from stats import character_count
from stats import count_words

def get_book_text(filepath): 
    with open(filepath) as f:
         text = f.read()
         return text 



def main():
    path_to_file = sys.argv[1] 
    text = get_book_text(path_to_file)
    num_words = count_words(text)
    char_counts = character_count(text)
    sort_list = sorted_list(char_counts)
    print(f"============ BOOKBOT ============")
    print(f"Analysing book found at {path_to_file}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_dict in sort_list:
        char = char_dict["char"]
        count = char_dict["num"]
        print(f"{char}: {count}")
    
    print("============= END ===============")

main()



