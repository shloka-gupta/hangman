from tkinter import*
from string import ascii_uppercase
from tkinter import messagebox
import random 

window=Tk()
window.title("Hangman")
window.config(bg='Grey')

BUTTONS =[ ]
photos = [PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang0.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang1.png"),
PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang2.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang3.png"),
PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang4.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang5.png"),
PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang6.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang7.png"),
PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang8.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang9.png"),
PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang10.png"),PhotoImage(file="C:\\Users\\Bharat\\Desktop\\Hangman\\images\\hang11.png")]

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

def w_disable(letter):
	for i in BUTTONS:
		if(i['text'] == letter):
			return i.config(bg='ForestGreen',state=DISABLED)
def n_disable(letter):
	for i in BUTTONS:
		if(i['text'] == letter):
			return i.config(bg='FireBrick',state=DISABLED)
def enable():
	for i in BUTTONS:
		if(i['state'] == 'disabled'):
			i.config(bg='skyblue',state=NORMAL)
numberOfGuesses=0
def newGame():
	global numberOfGuesses
	numberOfGuesses=0
	imgLabel.config(image=photos[0])
	newGame.the_word,name=words()
	newGame.the_word_withSpaces=" ".join(newGame.the_word)	
	lblWord.set(" ".join("_"*len(newGame.the_word)))
	Label(window,text=name,bg='Azure',font=("Consolas 15 bold"),width=10).grid(row=1,column=4,columnspan=6,padx=10)
	enable()

def guess(letter):
	flag=0
	global numberOfGuesses
	if numberOfGuesses<11:
		txt=list(newGame.the_word_withSpaces)
		guessed=list(lblWord.get())
		if newGame.the_word_withSpaces.count(letter)>0:
			for c in range(len(txt)):
				if txt[c]==letter:
					guessed[c]=letter
					w_disable(letter)
					flag=1
				lblWord.set("".join(guessed))
				if lblWord.get() == newGame.the_word_withSpaces:
					if(flag == 1):
						messagebox.showinfo("Hangman","You guessed it! ")
						flag=0
					
		else:
			numberOfGuesses+=1
			n_disable(letter)
			imgLabel.config(image=photos[numberOfGuesses])
			if numberOfGuesses == 11:
				messagebox.showinfo("Hangman","Game Over")			

imgLabel = Label(window,bg='Azure')
imgLabel.grid(row=0,column=0,columnspan=3,padx=10,pady=40)
imgLabel.config(image=photos[0])

lblWord = StringVar()
Label(window,textvariable=lblWord,bg='Azure',font=("Consolas 20 bold"),width=30).grid(row=0,column=3,columnspan=6,padx=10)


btn1 = Button(window,text='A',command=lambda:guess('A'),font=("Helvetica 18"),width =5,bg='skyblue')
btn1.grid(row=3,column=0)
BUTTONS.append(btn1)
btn2 = Button(window,text='B',command=lambda:guess("B"),font=("Helvetica 18"),width =5,bg='skyblue')
btn2.grid(row=3,column=1)
BUTTONS.append(btn2)
btn3 = Button(window,text='C',command=lambda:guess("C"),font=("Helvetica 18"),width =5,bg='skyblue')
btn3.grid(row=3,column=2)
BUTTONS.append(btn3)
btn4 = Button(window,text='D',command=lambda:guess("D"),font=("Helvetica 18"),width =5,bg='skyblue')
btn4.grid(row=3,column=3)
BUTTONS.append(btn4)
btn5 = Button(window,text='E',command=lambda:guess("E"),font=("Helvetica 18"),width =5,bg='skyblue')
btn5.grid(row=3,column=4)
BUTTONS.append(btn5)
btn6 = Button(window,text='F',command=lambda:guess("F"),font=("Helvetica 18"),width =5,bg='skyblue')
btn6.grid(row=3,column=5)
BUTTONS.append(btn6)
btn7 = Button(window,text='G',command=lambda:guess("G"),font=("Helvetica 18"),width =5,bg='skyblue')
btn7.grid(row=3,column=6)
BUTTONS.append(btn7)
btn8 = Button(window,text='H',command=lambda:guess("H"),font=("Helvetica 18"),width =5,bg='skyblue')
btn8.grid(row=3,column=7)
BUTTONS.append(btn8)
btn9 = Button(window,text='I',command=lambda:guess("I"),font=("Helvetica 18"),width =5,bg='skyblue')
btn9.grid(row=3,column=8)
BUTTONS.append(btn9)


btn10 = Button(window,text='J',command=lambda:guess("J"),font=("Helvetica 18"),width =5,bg='skyblue')
btn10.grid(row=4,column=0)
BUTTONS.append(btn10)
btn11 = Button(window,text='K',command=lambda:guess("K"),font=("Helvetica 18"),width =5,bg='skyblue')
btn11.grid(row=4,column=1)
BUTTONS.append(btn11)
btn12 = Button(window,text='L',command=lambda:guess("L"),font=("Helvetica 18"),width =5,bg='skyblue')
btn12.grid(row=4,column=2)
BUTTONS.append(btn12)
btn13 = Button(window,text='M',command=lambda:guess("M"),font=("Helvetica 18"),width =5,bg='skyblue')
btn13.grid(row=4,column=3)
BUTTONS.append(btn13)
btn14 = Button(window,text='N',command=lambda:guess("N"),font=("Helvetica 18"),width =5,bg='skyblue')
btn14.grid(row=4,column=4)
BUTTONS.append(btn14)
btn15 = Button(window,text='O',command=lambda:guess("O"),font=("Helvetica 18"),width =5,bg='skyblue')
btn15.grid(row=4,column=5)
BUTTONS.append(btn15)
btn16 = Button(window,text='P',command=lambda:guess("P"),font=("Helvetica 18"),width =5,bg='skyblue')
btn16.grid(row=4,column=6)
BUTTONS.append(btn16)
btn17 = Button(window,text='Q',command=lambda:guess("Q"),font=("Helvetica 18"),width =5,bg='skyblue')
btn17.grid(row=4,column=7)
BUTTONS.append(btn17)
btn18 = Button(window,text='R',command=lambda:guess("R"),font=("Helvetica 18"),width =5,bg='skyblue')
btn18.grid(row=4,column=8)
BUTTONS.append(btn18)


btn19 = Button(window,text='S',command=lambda:guess("S"),font=("Helvetica 18"),width =5,bg='skyblue')
btn19.grid(row=5,column=0)
BUTTONS.append(btn19)
btn20 = Button(window,text='T',command=lambda:guess("T"),font=("Helvetica 18"),width =5,bg='skyblue')
btn20.grid(row=5,column=1)
BUTTONS.append(btn20)
btn21 = Button(window,text='U',command=lambda:guess("U"),font=("Helvetica 18"),width =5,bg='skyblue')
btn21.grid(row=5,column=2)
BUTTONS.append(btn21)
btn22 = Button(window,text='V',command=lambda:guess("V"),font=("Helvetica 18"),width =5,bg='skyblue')
btn22.grid(row=5,column=3)
BUTTONS.append(btn22)
btn23 = Button(window,text='W',command=lambda:guess("W"),font=("Helvetica 18"),width =5,bg='skyblue')
btn23.grid(row=5,column=4)
BUTTONS.append(btn23)
btn24 = Button(window,text='X',command=lambda:guess("X"),font=("Helvetica 18"),width =5,bg='skyblue')
btn24.grid(row=5,column=5)
BUTTONS.append(btn24)
btn25 = Button(window,text='Y',command=lambda:guess("Y"),font=("Helvetica 18"),width =5,bg='skyblue')
btn25.grid(row=5,column=6)
BUTTONS.append(btn25)
btn26 = Button(window,text='Z',command=lambda:guess("Z"),font=("Helvetica 18"),width =5,bg='skyblue')
btn26.grid(row=5,column=7)
BUTTONS.append(btn26)

Button(window, text="New\nGame",command=lambda:newGame(),font=("Helvetica 10 bold"),bg="pink").grid(row=5,column=8,sticky="NSWE")
newGame()
window.mainloop()	