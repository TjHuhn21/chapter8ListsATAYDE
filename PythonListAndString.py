file = open('mbox-short.txt', 'r')
count = 0
for lines in file:
    if lines.startswith('From:'):
        continue
    elif lines.startswith('From'):
        sender_information = lines.split()
        print(sender_information[1])
        count += 1
    else:
        continue
print('There were ', count,' line in the file with From as the first word')