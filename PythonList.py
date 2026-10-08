fhand = open('remeo.txt', 'r')
words = list()
for lines in fhand:
    line_words = lines.split()
    for word in line_words:
        if word not in words:
            words.append(word)
words.sort()
print(words)
