from stats import get_total_word,get_total_char, sorted_dict
import sys

def get_book_text(filepath):
  with open(filepath) as r:
    return r.read()

def main():
 if len(sys.argv) != 2:
   print("Usage: python3 main.py <path_to_book>")
   sys.exit(1)
 path = sys.argv[1]
 num_words = get_total_word(get_book_text(path))
 print("============ BOOKBOT ============")
 print(f"Analyzing book found at {path}...")
 print("----------- Word Count ----------")
 print(f'Found {num_words} total words')
 print("--------- Character Count -------")
 char_dict = get_total_char(get_book_text(path))
 final_dict = sorted_dict(char_dict)
 for x in final_dict:
   temp = x["char"]
   if temp.isalpha():
     print(f"{temp}: {x['num']}")
 print("============= END ===============")
main()
