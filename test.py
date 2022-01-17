#Дана строка состоящая из слов разделенных один или несколькими пробелами,
#нужно напечатать на экран слвоа который повторяются в страке более 1 раза

text = "привет привет      выа выа  аываыв"

def dublicate_1(text: str):
    dubs = []
    words = text.split()

    for word in words:
        if words.count(word) > 1:
            dubs.append(word)
    dubs = list(set(dubs))
    print(sorted(dubs))

def dublicate_2(text: str):
    words = text.split()
    wordsCounter = {word: words.count(word) for word in words}

    for word in wordsCounter:
        if wordsCounter[word] > 1:
            print(word, end = " ")

dublicate_1(text)
dublicate_2(text)