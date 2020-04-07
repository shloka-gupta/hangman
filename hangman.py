from tkinter import*
from string import ascii_uppercase
from tkinter import messagebox
import random 

window=Tk()
window.title("Hangman")
window.configure(bg='grey')

def words():
	global name
	no=random.randint(1,4)
	if(no==1):
		name='Colors'
		Colors=['ORANGE','YELLOW','GREEN','BLUE','BROWN','MAGENTA','OLIVE','MAROON','NAVY','TURQUOISE','SILVER','LIME','TEAL','INDIGO','VIOLET','PINK','BLACK','WHITE','GREY']
		return random.choice(Colors),name
	elif(no==2):
		name='Country'
		Country=['INDIA','DENMARK','ICELAND','SWITZERLAND','NETHERLANDS','CANADA','NEWZEALAND','AUSTRALIA','SPAIN','RUSSIA','COSTARICA','AUSTRIA']
		return random.choice(Country),name
	elif(no==3):
		name='Animal'
		Animals=['SQUIRREL','KOALA','ELEPHANT','LEOPARD','HIPPOPOTAMUS','GIRAFFE','DOLPHIN','REINDEER','PEACOCK','PENGUIN','PARROT','FLAMINGO','WOODPECKER']
		return random.choice(Animals),name
	elif(no==4):
		name='Flower'
		Flowers=['HIBISCUS','JASMINE','LILY','LOTUS','MARIGOLD','MORNINGGLORY','TULIP','ROSE','SUNFLOWER','LAVENDER','CHERRYBLOSSOM']
		return random.choice(Flowers),name



photos = [PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang0.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang1.png"),
PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang2.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang3.png"),
PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang4.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang5.png"),
PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang6.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang7.png"),
PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang8.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang9.png"),
PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang10.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang11.png")]


def newGame():
	
	global the_word_withSpaces
	global numberOfGuesses
	numberOfGuesses=0
	imgLabel.config(image=photos[0])
	the_word,name=words()
	the_word_withSpaces=" ".join(the_word)	
	print(the_word)
	print(name)
	lblWord.set(" ".join("_"*len(the_word)))
	Label(window,text=name,font=("Consolas 15 bold"),width=10).grid(row=1,column=4,columnspan=6,padx=10)

def guess(letter):
	flag=0
	global numberOfGuesses
	if numberOfGuesses<11:
		txt=list(the_word_withSpaces)
		guessed=list(lblWord.get())
		if the_word_withSpaces.count(letter)>0:
			for c in range(len(txt)):
				if txt[c]==letter:
					guessed[c]=letter
					flag=1
				lblWord.set("".join(guessed))
				if lblWord.get() == the_word_withSpaces:
					if(flag == 1):
						messagebox.showinfo("Hangman","You guessed it! ")
						flag=0
					
		else:
			numberOfGuesses+=1
			imgLabel.config(image=photos[numberOfGuesses])
			if numberOfGuesses == 11:
				messagebox.showinfo("Hangman","Game Over")

imgLabel = Label(window)
imgLabel.grid(row=0,column=0,columnspan=3,padx=10,pady=40)
imgLabel.config(image=photos[0])

lblWord = StringVar()
Label(window,textvariable=lblWord,font=("Consolas 20 bold"),width=30).grid(row=0,column=3,columnspan=6,padx=10)


n=0
for c in ascii_uppercase:
	Button(window,text=c,command=lambda c=c: guess(c), font=("Helvetica 18"),width =5,bg="skyblue").grid(row=2+n//9,column=n%9)
	n+=1

Button(window, text="New\nGame",command=lambda:newGame(),font=("Helvetica 10 bold"),bg="pink").grid(row=4,column=8,sticky="NSWE")

newGame()
window.mainloop()














		








	