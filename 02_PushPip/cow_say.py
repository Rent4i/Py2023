import random
import cowsay
def ask(prompt: str, valid: list[str] = None) -> str:
    word = input()
    while word not in valid:
        print("Try again")
        word = input()

    return word
        
def inform(format_string: str, bulls: int, cows: int) -> None:
        print(format_string.format(bulls, cows))
        


def bullscows(guess: str, secret: str) -> (int, int):
    cows, bulls = 0,0
    for i,c in enumerate (guess):
        if len(guess) <= len (secret) and c==secret[i]:
            bulls+=1
        if c in secret:
            cows+=1
    return (bulls, cows)

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    word = random.choice(words)
    print(word, words)
    b,c,i=0,1,1
    while True:
 
        w= ask("Введите слово: ", words)
        if w == word:
            return i
        b,c = bullscows(word, w)
        inform("Быки: {}, Коровы: {}", b, c)
        i+=1
       
    
print(gameplay(ask, inform, ["secret", "loose", "haha", "lol", "norm", "kaka"]))
