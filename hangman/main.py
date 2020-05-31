from words import word_list
import time
import random

def get_word():
    word = random.choice(word_list)
    return word.lower()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words   = []
    tries = 6
    print('Lets play hangman')
    print(display_hangman(tries))
    print(word_completion)
    while not guessed and tries > 0:
        user_guess = input('Guess the letter or the word: ').lower
        if len(user_guess) == 1 and guess.isalpha():
            if user_guess in guessed_letters:
                print('You already guessed the letter ', user_guess)

            elif guess_not in guessed_letters:
                print('You already guessed ', user_guess)
                tries -= 1
                guessed_letters.append(user_guess)
            else:
                print('Good Job ', user_guess + ' is in the word.')
                guessed_letters.append(word)
                word_as_list = list(word_completion)
                indices = [i for i,letter in enumerate(word) if letter == guess]
                for index in indinces:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(user_guess) == len(word) and guess.isalpha():
            if user_guess in guessed_words:
                print('you already guessed the word ', user_guess)
            elif user_guess != word:
                print(user_guess, " is not the word.")
                tries -= 1
                guessed_words.append(user_guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Not a valid guess')
        if guessed:
            print('Congrats you guessed the correct word! You Win :)')
        else:
            print('Sorry you ran out of tries :( . The correct word was ' + word + ' Better luck next time! :-)')
def display_hangman(tries):
    stages = [   '''
                      ---------
                     |        |
                     |        O
                     |       \|/
                     |        |
                     |       / \ 
                     |
                     -
                 ''',
                 '''
                      ---------
                     |        |
                     |        O
                     |       \|/
                     |        |
                     |       /
                     |
                     -
                 ''',
                 '''
                      ---------
                     |        |
                     |        O
                     |       \|/
                     |        |
                     |      
                     |
                     -
                 ''',
                 '''
                      ---------
                     |        |
                     |        O
                     |       \|
                     |        |
                     | 
                     |
                     -
                 ''',
                 '''
                      ---------
                     |        |
                     |        O
                     |        |
                     |        |
                     |
                     |
                     -
                 ''',
                 '''
                      ---------
                     |        |
                     |        O
                     |        
                     |        
                     |      
                     |
                     -
                 '''
]

def main():
    word = get_word
    play(word)
    while input('Play again Y/N').upper() == "Y":
        word = get_word
        play(word)

if __name__ == "__main__":
    main()