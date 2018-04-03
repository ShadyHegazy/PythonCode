# Hangman game


import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    i=0
    while i<(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            return False
            break
        elif i==len(secretWord)-1:
            return True
            break
        else:
            i+=1
            


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedsofar=''
    g=0
    while g<(len(secretWord)):
        if secretWord[g] not in lettersGuessed:
            guessedsofar=guessedsofar+' _ '
            g+=1
        elif secretWord[g] in lettersGuessed:
            guessedsofar=guessedsofar+secretWord[g]
            g+=1
    return guessedsofar



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    AllLetters=string.ascii_lowercase
    remaining=''
    p=0
    while p<len(AllLetters):
        if AllLetters[p] in lettersGuessed:
            p+=1
        elif AllLetters[p] not in lettersGuessed:
            remaining=remaining+AllLetters[p]
            p+=1
    return remaining
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord))+' letters long.')
    remainingguesses=8
    lettersGuessed=[]
    while remainingguesses>0:
        remaining=getAvailableLetters(lettersGuessed)
        print('-----------')        
        print('you have ' + str(remainingguesses)+ ' guesses left')
        print('Available letters: '+remaining)
        x=input('Please guess a letter: ')
        guess=x.lower()
        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            if isWordGuessed(secretWord, lettersGuessed):
                print('Good guess: '+ getGuessedWord(secretWord, lettersGuessed))  
                print('-----------')
                print('Congratulations, you won!')
                break
            elif guess not in secretWord:
                remainingguesses-=1
                print('Oops! That letter is not in my word: '+ getGuessedWord(secretWord, lettersGuessed))
            elif guess in secretWord:
                print('Good guess: '+ getGuessedWord(secretWord, lettersGuessed)) 
        else: 
            print("Oops! You've already guessed that letter: "+ getGuessedWord(secretWord, lettersGuessed))  
    if remainingguesses==0:
        print('-----------')
        print('Sorry, you ran out of guesses. The word was '+ secretWord+'.')
    
                
                
        
        
        


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
