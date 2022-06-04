import copy 
import random

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    # i = 0
    ten_letters = []
    pool_of_letters = []
    # letter_pool_copy = LETTER_POOL.copy()
    for letter, count in LETTER_POOL.items(): 
        pool_of_letters.extend([letter] * count)
    while len(ten_letters) < 10:
        random_letter = random.choice(pool_of_letters)
        if random_letter in pool_of_letters:
            ten_letters.append(random_letter)
            pool_of_letters.remove(random_letter)
    
    return ten_letters
    
def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass