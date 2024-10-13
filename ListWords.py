word_count = {}

try:
    with open("Pytho\ReadFile\Words.txt", 'r') as file:
        contents = file.read()
        words = contents.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1 
            else:
                word_count[word] = 1  
    print("Word count:", dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True)))

    
except FileNotFoundError:
    print("File not found")