
# Hangman Game

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    found_letters=0
    for char in secret_word:
        if char in letters_guessed:
            found_letters+=1
    
    if found_letters==len(secret_word):
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word=""
    for char in secret_word:
        if char in letters_guessed:
            guessed_word+=char
        else:
            guessed_word+="_ "
    
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters=string.ascii_lowercase
    
    available_letters = list(available_letters)
    
    for char in letters_guessed:
        if char in available_letters:
            available_letters.remove(char)
            
    available_letters = ''.join(available_letters)
    
    return available_letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    vowels=['a', 'e', 'i', 'o', 'u']
    guessed = False
    letters_guessed=[]
    guesses_left = 6
    lost=False
    warnings_left = 3
    breakline="---------------"
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {0:d} letters long.".format(len(secret_word)))
    
    
    #starting the loop
    while(not guessed and not lost):
        #exi control 
        if guesses_left <= 0 or warnings_left <= 0:
            lost = True
            
            
        #print before every guess
        print(breakline)
        print("You have {0:d} warnings left".format(warnings_left))
        print("You have {0:d} guesses left.".format(guesses_left))
        print("Available letters: " + get_available_letters(letters_guessed))
        guessed_letter = input("Please guess a letter: ").lower()
        
        #check if guessed_letter is valid input
        if guessed_letter in letters_guessed:
            print("You have already guessed this letter")
            warnings_left-=1
            continue
        elif len(guessed_letter) != 1 or (not guessed_letter.isalpha()):
            print("Enter a character")
            warnings_left-=1
            continue
        else:
            #if guessed letter is valid then append it to list of guessed letters
            letters_guessed.append(guessed_letter)
        
        
        #check if guessed letter is in the word
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if guessed_letter in list(secret_word):
            print("Good guess:" + guessed_word)
        else:
            print("Oops! That letter is not in my word: " + guessed_word)
            
            if guessed_letter in vowels:
                guesses_left-=2
            else:
                guesses_left-=1
        
        #check winning status
        if guessed_word.replace(' ', '') == secret_word:
            guessed = True
                
        ################################
        #End of loop
        ################################
        
    #Checking how the loop ended and printing the result  
    if guessed_word.replace(' ', '') == secret_word:
        unique_characters_num = len(list(set(secret_word)))
        score=guesses_left*unique_characters_num
        print(breakline)
        print("Congratulations, you won!")
        print("Your total score for this game is:", score)
    elif lost==True:
        if warnings_left<=0:
            print("Sorry you have lost because you have entered too many invalid characters. The word was", secret_word)
        elif guesses_left<=0:
            print("Sorry, you have ran out of guesses. The word was", secret_word)
        
            


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
