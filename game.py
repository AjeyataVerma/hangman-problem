import requests

def game():
    word = str(requests.get("https://random-word-api.herokuapp.com/word?number=1").json()[0])
    print("******** Welcome to Hangman Game **********")
    print("You have 5 lives to play the game")

    
    random_word = "_ " * len(word)
    lives = 5

    while lives > 0 and '_' in random_word:
        print(f"You have {lives} chances left")
        print(random_word)
        n = str(input("Guess the character: "))
        n = n.lower()
        if n in word:
            guessed = [i for i, w in enumerate(word) if w == n]
            for i in guessed:
                if random_word[i] == "_":
                    random_word = random_word[:i] + n + random_word[i+1:]
                    break
        else:
            lives -= 1
    if lives == 0:
        print("\nYou lost! \nThe word was: ", word)
    else:
        print("Congratulations, you guessed it right!")


if __name__ == '__main__':
    game()