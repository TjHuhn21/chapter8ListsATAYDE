fhand = open('remeo.txt', 'r')
words = list()
for lines in fhand:
    # SPLITS EACH LINE OF THE FILE
    line_words = lines.split()
    #LOOPS THROUGH LIST OF WORDS ON THE LINE
    for word in line_words:
        #ADDS THE WORD IF NOT ALREADY IN THE LIST
        if word not in words:
            words.append(word)
words.sort()
print(words)
