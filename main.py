#import the random feature
import random
#slecing a word at random from the wordlist
with open("wordlist.txt", 'r') as file:
    alltext = file.read()
    words = list(map(str, alltext.split()))
    hangman = (random.choice(words))
#creating a few variables
guess = ("Guessed Words")
guessed = []
livesleft = 7

#blanking out the answer untill its relvealed
def answer():
  global hangman
  word = ""
  for letter in hangman:
    if letter in guessed:
      word += letter
    else:
      word += "*"
  print (word)
  if word == hangman:
    print ("YOU WIN!!!\n the hidden word was: ", hangman)    
    quit()
  
#the main body of the game using global variables
#able to only input 1 unique letter at a Timeout
#removing a life if required
def letter():
  global guessed
  global livesleft
  global guess
  global hangman
  print("\nLIVES LEFT =", livesleft)
  guess_letter = input('\nPlease enter a letter: ')
  if len(guess_letter) <= 1:
    guess=guess_letter
  else:
    print ("\n***please only select 1 letter at a time***") 
    letter() 
  if guess not in guessed:
    guessed += guess
    if guess not in hangman:
      livesleft -= 1
  else:
    print ("\nLetter already guessed")
  print("\n", "\nGuessed letters",guessed)

#if game over or if scripts are to be ran again
def result():
  if livesleft < 1:
    print("\n\n***YOU LOSE***\n hidden word was ",hangman)
  elif guess not in hangman:
    print("\nincorrect please guess again\n")
    answer()
    letter()
    result() 
  else:
    answer()
    letter()
    result()

#only available to be able to see the random word
#print("word here only for scripting/testing:\n",hangman,"\n")

#start of the game
print("WELCOME TO HANGMAN:\n")
print("Your hidden word is:",(len(hangman)),"letters long")
print("You have 7 lives to guess this word\n")
answer()
letter()
result()