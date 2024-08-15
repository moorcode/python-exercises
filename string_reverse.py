word = input("Enter a word to be reversed: ")

def do_over(redo):
    if redo=="y" or redo=="yes":
        word = input("Enter another word to be reversed: ")
        string_reverse(word)
    elif redo=="n" or redo=="no":
        print("Thanks for playing!")
    else:
        redo = input("Please enter a valid character (y/n): ")
        do_over(redo)
    
def string_reverse(word):
    reversed = ""
    index = len(word) - 1
    while index >= 0:
        reversed += word[index]
        index = index - 1
    print(reversed)
    redo = input("Try again? (y/n): ")
    do_over(redo)

string_reverse(word)