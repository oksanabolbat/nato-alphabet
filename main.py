import pandas as pd

# with open("nato_phonetic_alphabet.csv") as alphabet_file:
#     ctx = alphabet_file.read()

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pd.read_csv("nato_phonetic_alphabet.csv")
# for (ind, row) in df.iterrows():
#     print(row)
alpha_dict = {row.letter: row.code for (ind, row) in df.iterrows()}
print(alpha_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("please enter a word: ")
alphabet_result = [alpha_dict[letter] for letter in user_word.upper()]
print(alphabet_result)

