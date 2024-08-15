word = input("Please enter a word to check if it is a palindrome: ")

def repeat(redo):
    if redo=="y" or redo=="yes":
        word = input("Please enter another word to check if it is a palindrom: ")
        is_palindrome(word)
    elif redo=="n" or redo=="no":
        print("Thanks for playing!")
    else: 
        redo = input("Please enter a valid character (y/n): ")
        repeat(redo)


def is_palindrome(word):
    if word == word[::-1]:
        print(word + " is a palindrome!")
    else:
        print(word + " is not a palindrome :-(")
    redo = input("Do you want to play again? (y/n): ")
    repeat(redo)

is_palindrome(word)



