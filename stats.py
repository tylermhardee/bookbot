def count_words(text):
        words = text.split()
        return len(words)

def count_letters(text):
	letter_counts = {}
	for char in text:
		char = char.lower()
		if char in letter_counts:
			letter_counts[char] += 1
		else:
			letter_counts[char] = 1
	return letter_counts

def sort_letter_counts(letter_counts):
	sorted_list = []
	for char, count in letter_counts.items():
		sorted_list.append({"char": char, "count": count})
	def sort_on(dict):
		return dict["count"]
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list
