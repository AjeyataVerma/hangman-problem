import requests

def game():
    word = str(requests.get("https://random-word-api.herokuapp.com/word?number=1").json()[0])
    print("******** Welcome to Hangman Game **********")
    print("You have 5 lives to play the game")

    wrong_list=[]

    # for i in range (len(display)):
#   #replace each letter with a '_'
#   display = display[0:i] + "_" + display[i+1:]
    random_word = word
    for i in range(len(random_word)):
        random_word = random_word[0:i] + "_" + random_word[i+1:]
    #random_word = "_" * len(word)
    lives = 5

    while lives > 0 and '_' in random_word:
        print(f"You have {lives} chances left")
        print(" ".join(random_word))
        n = input("Guess the character: ")
        n = n.lower()
        if not n.isalpha():
            print("Guess only a letter")
        elif(len(n)>1):
            print('Guess only one letter...')
        elif(n in wrong_list):
            print('You have Already guessed this letter')
            lives +=1
        if n in word:
            guessed = [i for i, w in enumerate(word) if w == n]
            for i in guessed:
                if random_word[i] == "_":
                    random_word = random_word[:i] + n + random_word[i+1:]
                    break
        else:
            lives -= 1
            wrong_list.append(n)

    if lives == 0:
        print("\nYou lost! \nThe word was: ", word)
    else:
        print("Congratulations, you guessed it right!")


if __name__ == '__main__':
    game()
