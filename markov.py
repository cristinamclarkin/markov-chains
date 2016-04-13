from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()
    #print contents
    return contents 
    "This should be a variable that contains your file text as one long string"



def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi'): ['there']}
    """

    chains = {}
    # splitting our giant string into single words using whitespace
    list_of_words = text_string.split()
    # terminates loop at second to last word so that there is no index error
    for i in range(len(list_of_words) - 2):
        # setting string values index that will be used to form the key name in our tuple
        # begins at first word in our string
        word1 = list_of_words[i]
        # moves through string in increments of one
        word2 = list_of_words[i +1]
        # creates key variable name using two strings
        my_key = (word1, word2)
        # creates varaiable for third word that will be added to a list 
        # that acts as our value for keys
        word3 = list_of_words[i + 2]
        # if our value is not in chains (our dictionary), add value to list 
        if my_key in chains:
            chains[my_key].append(word3)
        # if it is not, assign word (value) to key (tuple) 
        else: 
            chains[my_key] = [word3]

    return chains , tuple(list_of_words[-2:])




def make_text(chains , last_words):
    """Takes dictionary of markov chains; returns random text."""
    # randomly selects keys from our dictionary
    my_key = choice(chains.keys())
    
    # creates an string into which we will put our random keys and 
    # values in
    text = ""
    
    # while item is in our dictionary
    while True:
        
        # randomly selects key value 
        next_word = choice(chains[my_key])
        
        # concatenates randomly selected words
        text = text + " " + next_word

        # creates new tuple pair from the list of values 
        my_key = (my_key[1], next_word)

        # references previously established parameter so that loop
        # is broken once all tuple options are exausted 
        if my_key == last_words:
            break

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains , last_words = make_chains(input_text)
#print chains 


# Produce random text
random_text = make_text(chains, last_words)

print random_text