from tkinter import \
    PhotoImage, Button, Tk, \
    messagebox, DISABLED, NORMAL, \
    Label, StringVar
from string import ascii_uppercase
import random

window = Tk()
window.title("Hangman")
window.config(bg='Grey')

# list containing all the buttons from A to Z
BUTTONS = []

photos = [
    PhotoImage(file="./images/hang0.png"), PhotoImage(file="./images/hang1.png"),
    PhotoImage(file="./images/hang2.png"), PhotoImage(file="./images/hang3.png"),
    PhotoImage(file="./images/hang4.png"), PhotoImage(file="./images/hang5.png"),
    PhotoImage(file="./images/hang6.png"), PhotoImage(file="./images/hang7.png"),
    PhotoImage(file="./images/hang8.png"), PhotoImage(file="./images/hang9.png"),
    PhotoImage(file="./images/hang10.png"), PhotoImage(file="./images/hang11.png")
]


def words():
    # words() randomly selects a list and a word from a respective list and then words() returns name of list and a word
    no = random.randint(1, 4)
    if(no == 1):
        name = 'Colors'
        Colors = ['ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'BROWN', 'MAGENTA', 'OLIVE', 'MAROON', 'NAVY',
                  'TURQUOISE', 'SILVER', 'LIME', 'TEAL', 'INDIGO', 'VIOLET', 'PINK', 'BLACK', 'WHITE', 'GREY']
        return random.choice(Colors), name
    elif(no == 2):
        name = 'Country'
        Country = ['INDIA', 'DENMARK', 'ICELAND', 'SWITZERLAND', 'NETHERLANDS',
                   'CANADA', 'NEWZEALAND', 'AUSTRALIA', 'SPAIN', 'RUSSIA', 'COSTARICA', 'AUSTRIA']
        return random.choice(Country), name
    elif(no == 3):
        name = 'Animal'
        Animals = ['SQUIRREL', 'KOALA', 'ELEPHANT', 'LEOPARD', 'HIPPOPOTAMUS', 'GIRAFFE',
                   'DOLPHIN', 'REINDEER', 'PEACOCK', 'PENGUIN', 'PARROT', 'FLAMINGO', 'WOODPECKER']
        return random.choice(Animals), name
    elif(no == 4):
        name = 'Flower'
        Flowers = ['HIBISCUS', 'JASMINE', 'LILY', 'LOTUS', 'MARIGOLD',
                   'MORNINGGLORY', 'TULIP', 'ROSE', 'SUNFLOWER', 'LAVENDER', 'CHERRYBLOSSOM']
        return random.choice(Flowers), name


def w_disable(letter):
    # w_disable disables the button in green color if the letter is in the word
    for i in BUTTONS:
        if(i['text'] == letter):
            return i.config(bg='ForestGreen', state=DISABLED)


def n_disable(letter):
    # n_disable disables the button in red color if the letter is not in the word
    for i in BUTTONS:
        if(i['text'] == letter):
            return i.config(bg='FireBrick', state=DISABLED)


def enable():
    # enables all disabled buttons
    for i in BUTTONS:
        if(i['state'] == 'disabled'):
            i.config(bg='skyblue', state=NORMAL)


numberOfGuesses = 0


def newGame():
    global numberOfGuesses
    numberOfGuesses = 0
    imgLabel.config(image=photos[0])
    newGame.the_word, name = words()
    newGame.the_word_withSpaces = " ".join(newGame.the_word)
    lblWord.set(" ".join("_"*len(newGame.the_word)))
    Label(window, text=name, bg='Azure', font=("Consolas 15 bold"),
          width=10).grid(row=1, column=4, columnspan=6, padx=10)
    enable()


def guess(letter):
    # checks if the letter is in the word or not
    flag = 0
    global numberOfGuesses
    if numberOfGuesses < 11:
        txt = list(newGame.the_word_withSpaces)
        guessed = list(lblWord.get())
        if newGame.the_word_withSpaces.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                    w_disable(letter)
                    flag = 1
                lblWord.set("".join(guessed))
                if lblWord.get() == newGame.the_word_withSpaces:
                    if(flag == 1):
                        messagebox.showinfo("Hangman", "You guessed it! ")
                        flag = 0

        else:
            numberOfGuesses += 1
            n_disable(letter)
            imgLabel.config(image=photos[numberOfGuesses])
            if numberOfGuesses == 11:
                messagebox.showinfo("Hangman", "Game Over")


imgLabel = Label(window, bg='Azure')
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

lblWord = StringVar()
Label(window, textvariable=lblWord, bg='Azure', font=("Consolas 20 bold"),
      width=30).grid(row=0, column=3, columnspan=6, padx=10)


row, col = 3, 0

for i in ascii_uppercase:
    if col != 0 and col % 9 == 0:
        row += 1
        col = 0

    button = Button(window, text=i, command=lambda k=i: guess(k),
                    font=("Helvetica 18"), width=5, bg='skyblue')
    button.grid(row=row, column=col)
    BUTTONS.append(button)

    col += 1

Button(window, text="New\nGame", command=lambda: newGame(), font=(
    "Helvetica 10 bold"), bg="pink").grid(row=5, column=8, sticky="NSWE")
newGame()
window.mainloop()
