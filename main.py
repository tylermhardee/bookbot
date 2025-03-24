import sys
from stats import count_words
from stats import count_letters
from stats import sort_letter_counts

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def main():
	path = sys.argv[1]
	book_text = get_book_text(path)
	word_count = count_words(book_text)
	letter_count = count_letters(book_text)
	sorted_chars = sort_letter_counts(letter_count)
	print(letter_count)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")

	for item in sorted_chars:
		char = item["char"]
		count = item["count"]
		if char.isalpha(): #only print alphabetic characters
			print(f"{char}: {count}")

	print("============= END ===============")

main()

