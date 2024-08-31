import pandas as pd


df = pd.read_csv("nato_phonetic_alphabet.csv")

alpha_dict = {row.letter: row.code for (ind, row) in df.iterrows()}

is_ready = False
while not is_ready:
    user_word = input("please enter a word: ")
    try:
        alphabet_result = [alpha_dict[letter] for letter in user_word.upper()]
        print(alphabet_result)
        is_ready = True
    except KeyError:
        print("Sorry, only letters in the alphabet please")

