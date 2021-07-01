from random import randint
import os


def run():
    os.system('cls')
    print(
        '''
   **  **    ***    **   **  *******  **      **    ***    **   **
   **  **   ** **   ***  **  **       ***    ***   ** **   ***  **
   ******   *****   **** **  ** ****  ****  ****   *****   **** **
   **  **  **   **  ** ****  **   **  ** **** **  **   **  ** ****
   **  **  **   **  **  ***  *******  **  **  **  **   **  **  ***
    ''')

    is_playing = 'y'
    words = read_words()
    os.system('pause')

    while(is_playing == 'y'):
        try:
            word = words[randint(0, len(words) - 1)]
            play(word)
            print('You won!')
        except:
            print("The answer is", word)
            print('Game Over')
        finally:
            is_playing = input('Want to play again? y/n: ')

    os.system('cls')
    print('Thank you por playing :)')


def read_words():
    '''
    In this function, we read our list of words that is located in /files/words.txt
    and is returned as a list.
    '''
    words = []
    with open('files/words.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words.append(line.strip())

    return words


def play(word):
    actual_try = [None for x in range(len(word))]
    fails = 0
    answer_count = 0
    has_won = False
    char = ''

    while(not has_won):
        is_correct = False
        draw_hangman(fails, actual_try)
        if fails >= 6:
            raise Exception("Game over")

        elif answer_count == len(word):
            has_won = True

        char = input('Enter a letter: ')

        for i in range(len(word)):
            if word[i] == char:
                answer_count += 1
                is_correct = True
                actual_try[i] = char

        if not is_correct:
            fails += 1


def draw_hangman(n_failure, try_list):
    hangman_list = [
        '''
    ||==================
    ||            |
    || 
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    =======@========== ========
    ||                        ||
    ||                        ||
    ||                        ||
    ''',
        '''
    ||==================
    ||           |
    ||          ___
    ||         /   \\
    ||        | * * |
    ||         \___/
    ||           
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    =======@========== ========
    ||                        ||
    ||                        ||
    ||                        ||
    ''',
        '''
    ||==================
    ||            |
    ||           ___
    ||          /   \\
    ||         | * * |
    ||          \___/
    ||            |
    ||            |
    ||            |
    ||            |
    ||            |
    ||
    ||
    ||
    ||
    =======@========== ========
    ||                        ||
    ||                        ||
    ||                        ||
    ''',
        '''
    ||==================
    ||            |
    ||           ___
    ||          /   \\
    ||         | * * |
    ||          \___/
    ||            |
    ||        ----|
    ||            |
    ||            |
    ||            |
    ||
    ||
    ||
    ||
    =======@========== ========
    ||                        ||
    ||                        ||
    ||                        ||
    ''',
        '''
    ||==================
    ||            |
    ||           ___
    ||          /   \\
    ||         | * * |
    ||          \___/
    ||            |
    ||        ----|----
    ||            |
    ||            |
    ||            |
    ||
    ||
    ||
    ||
    =======@========== ========
    ||                        ||
    ||                        ||
    ||                        ||
    ''',
        '''
    ||==================
    ||            |
    ||           ___
    ||          /   \\
    ||         | * * |
    ||          \___/
    ||            |
    ||        ----|----
    ||            |
    ||            |
    ||            |
    ||           /
    ||          /
    ||         /
    ||
    =======@========== ========
    ||                        ||
    ||                        ||
    ||                        ||
    ''',
        '''
    ||==================
    ||            |
    ||           ___
    ||          /   \\
    ||         | x x |
    ||          \___/
    ||            |
    ||        ----|----
    ||            |
    ||            |
    ||            |
    ||           / \\
    ||          /   \\
    ||         /     \\
    ||
    =======@            ========
    ||      \                 ||
    ||       \                ||
    ||        \               ||
    '''
    ]
    os.system('cls')
    if(n_failure >= len(hangman_list) - 1):
        print(hangman_list[len(hangman_list) - 1])
    else:
        print(hangman_list[n_failure])
    for char in try_list:
        if char == None:
            print('_', end='')
        else:
            print(char, end='')
    print('')


if __name__ == '__main__':
    run()
