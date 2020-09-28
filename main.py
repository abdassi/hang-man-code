import random
import string
wrongs = []
words = ['apple', 'banana', 'orange', 'board', 'monkey', 'car', 'taxi']
expressions=[ "What's this?","What's that?","Is anything wrong?"
    ,"What Is everything OK?" ]
expression = random.choice(expressions)
word = random.choice(words)
len_word = len(word)
pattern = ["_"] * len_word

def play_game():
    level()
    while '_' in pattern and len(wrongs) < 3:
        one_round()
    if '_' in pattern:
        print('You lose!')
    else:
        print('You win!')

def level():
    while True:
        level = input("choose level ( easy or hard ) : ")
        if level == "hard":
            word = expression
            break
        elif level == "easy":
            break


def one_round():
    x = input("Enter a letter : ")
    if x not in string.ascii_lowercase:
        print('you should inter a letter.')
        return
    if x in word:
        if x in pattern:
            print("You have entered this letter previously.")
            return
        else:
            for (index, letter) in enumerate(word):
                if letter == x:
                    pattern[index] = letter
            print(pattern)
    else:
        if x in wrongs:
            print("You have entered this letter previously.")
            return
        else:
            wrongs.append(x)
            print('The letter is wrong.')


if __name__ == "__main__":
    play_game()
