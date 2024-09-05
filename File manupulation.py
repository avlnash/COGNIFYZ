def count_words(file_path):
    word_counts = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.lower().split()
                for word in words:
                    word = word.strip(",.!?;:\"'")
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
        for word in sorted(word_counts.keys()):
            print(word + ": " + str(word_counts[word]))
    except UnicodeDecodeError:
        print("Error: The file could not be decoded. Please check the file encoding.")
file_path = input("Enter the path to the text file: ").strip('"')
count_words(file_path)
