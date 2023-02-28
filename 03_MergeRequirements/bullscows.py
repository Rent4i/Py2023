import random, requests

def ask(prompt: str, valid: list[str] = None) -> str:
    
    word = input(prompt)
    while word != "я устал" and word not in valid:
        word = input("Нет такого слова, попробуй снова: ")
    return word
        
def inform(format_string: str, bulls: int, cows: int) -> None:
        print(format_string.format(bulls, cows))
        

def bullscows(guess: str, secret: str) -> (int, int):
    cows, bulls = 0,0
    for i,c in enumerate (guess):
        if  c==secret[i:i+1]:
            bulls+=1
    cows= len(set(guess) & set(secret))
    return (bulls, cows)

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    word = random.choice(words)
    i=1
    while True:
 
        w= ask("Введите слово: ", words)
        if w == word or w == "я устал":
            if w=="я устал":
                print("В следующий раз получится! А слово было - ", word)
                return i-1
            return i
        else:
            b,c = bullscows(word, w)
            inform("Быки: {}, Коровы: {}", b, c)
            i+=1
def count(str1 ,str2) :

    set_string1 = set(str1)
 
    set_string2 = set(str2)
 
    matched_characters = set_string1 & set_string2
    return len(matched_characters)


url = 'https://raw.githubusercontent.com/Harrix/Russian-Nouns/main/dist/russian_nouns.txt'
wordsfile = requests.get(url)
open('words.txt', 'wb').write(wordsfile.content)

words= open("words.txt", encoding = "utf-8").readlines()
words=[word.rstrip() for word in words]
print(gameplay(ask, inform, words))
