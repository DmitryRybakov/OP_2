def create_text(text):
    x = input('Введiть слова: ')
    while x:
        text += x + " " + "\n"
        x = input('Введiть слова: ')
    return text

def input_file():
    file = open ('file.txt', 'w')
    file.write(text)
    file.close

    file = open ('file.txt')
    print('Перший текстовий файл: ', file.read())
    file.close

def find_new_file():
    new_words = ""
    new_words = find_new_words()
    print('new_words = ', new_words)
    print()

    new_file = open ('new file.txt', 'w')
    new_file.write(new_words)
    new_file.close

    new_file = open ('new file.txt')
    print('Новий текстовий файл: ', new_file.read())
    new_file.close

def find_new_words():
    file = open ('file.txt')

    words = []
    for line in file:
        words += line.split(' ')

    file.close

    new_words_list = []
    for word in words:
        if word != ' ' and word !='\n' and word != '':
            if words.count(word) < int(N):
                new_words_list.append(word)

    new_words_less_N = ' '.join(new_words_list)
    print('Слова вхідного файлу, які зустрічаются в ньому меньше N раз: ', new_words_less_N)
    print()

    new_words_list.sort(key=len)
    new_words_list.reverse()
    new_words = ' '.join(new_words_list)

    print('Слова вхідного файлу, які зустрічаются в ньому меньше N раз в порядку спадання їхньої довжини: ')
    
    return new_words


N = input('Введіть N: ')

text = ""
text = create_text(text)
while text == "":
        print('Текст не введений!')
        text = create_text(text)
print()

print('Введенне N: ', N)
print()

print('Слова вхідного файлу: ', text)

input_file()

find_new_file()



