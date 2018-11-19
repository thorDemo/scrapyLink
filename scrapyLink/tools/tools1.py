

with open('D:\workspace\scarpyLink\scrapyLink\source\domain.txt', 'r+') as file:
    for line in file:
        print('\'http://www.%s\',' % line.strip('\n'))
