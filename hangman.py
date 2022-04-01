"""
Learn Python the Fun Way - Hangman Game by DeShay K.
Github: https://github.com/deshayk
Medium: https://www.medium.com/@deshayk
LinkedIn: https://www.linkedin.com/in/deshayk/
"""

import random # gives you access to the random module, needed to choose a random word from the word-list python file 
from wordList import words # imports the words array file from the same directory as the wordList.py file

def getWord(words):
  word = random.choice(words) #randomly chooses a word from the words array
  return word.upper() #returns the word in uppercase to improve readability and consistency

def hangmanGame():
  word = getWord(words) #gets a random word from the words array
  wordLetters = set(word) #creates a set of the letters in the word
  alphabet = set(string.ascii_uppercase) #creates a set of the letters in the alphabet
  usedLetters = set() #creates a set of the letters already used
  
  lives = 7 #sets the number of lives to 7 (includes the head, the body, the left arm, the right arm, the left leg, and the right leg)
  
  while len(wordLetters) > 0 and lives > 0: #while the word has letters and the user still has lives
    print("\n") #prints a new line
    print("Lives Remaining: " + str(lives)) #prints the number of lives remaining
    
    wordList = [letter if letter in usedLetters else "-" for letter in word] #creates a list of the letters in the word, with the letters in the word replaced with dashes if they have not been used yet
    print(" ".join(wordList)) #prints the word with dashes in place of the letters that have not been used yet