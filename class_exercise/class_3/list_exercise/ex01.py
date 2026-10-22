
sentence = input("Please, enter any sentence: ").lower().replace(",", "").replace(".", "")

word_count ={}

for word in sentence.split():
	word_count[word] = word_count.get(word, 0) + 1
repeated_words = []

for word, count in word_count.items():
	if count > 1:
		repeated_words.append(word)
		
		print(f"{repeated_words}: {count}")