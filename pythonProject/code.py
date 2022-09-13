def find(string, char):
    for i, c in enumerate(string):
        if c == char:
            yield i


# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
winner = False
count = 0
s_word = "book"
word = ['_', '_', '_', '_']

for i in range(0, 10):

    print("Guess the word: ")

    print(" ".join(word))

    val = input("letter: ")
    guess = list(find(s_word, val))
    print(guess)

    if not guess:
        print("try again")

    else:
        print("you got it!")
        length = len(guess)
        for i in range(0, length):
            word[guess[i]] = val
            count += 1

    if count == len(s_word):
        winner = True
        break

    print('************\n')

if winner:
    print("\nCONGRATS YOU WON!!!\n")

else:
    print("It's okay you tried your best")