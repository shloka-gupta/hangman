import random

def comp():
	words = ['cats','dogs','helloo','moons','rome']
	return random.choice(words)
def play():
	word = comp()
	letters_guessed=[] ; correct_letters_guessed=[]
	tries = 5
	guessed = False
	alphabet = 'abcdefghijklmnopqrstuvwxyz'

	print('the word contains',len(word), ' letters')
	print('_'*len(word))
 	
	while guessed == False and tries>0:
		print('you have '+str(tries)+ ' tries')
		guess = input("please enter one letter or full word ").lower()
		#1-user inputs a letter
		if len(guess)==1:
			if guess not in alphabet:
				print("you have not entered a letter.")
			elif guess in letters_guessed:
				print("you have already guessed that letter")
			elif guess not in word:
				print('sorry,that letter is not part of the word: ')
				letters_guessed.append(guess)
				tries=tries-1
			elif guess in word:
				print('well good that letter exists')
				letters_guessed.append(guess) ;correct_letters_guessed.append(guess)
                
			else:
				print('idk why we get this message')
		#2-user enters word
		elif len(guess) == len(word):
			if guess == word:
				print("you have guessed the right word")
				guessed = True
			else:
				print("sorry ")
				tries = tries-1
		#3 user inputs the 
		else:
				print("the length of your guess is not thr word we're looking for")
		
		status = ''
		if guessed == False:
			for letter in word:
				if letter in letters_guessed:	
					status += letter
				else:
					status += '*'
			print(status)
		if status == word:
			print("well done , you guessed it right")
			guessed = True
            		
		elif tries == 0:
			print("good try. but u lost")

play()
