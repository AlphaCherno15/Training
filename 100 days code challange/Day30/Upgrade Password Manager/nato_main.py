import pandas as pd
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
data = pd.read_csv("nato_phonetic_alphabet.csv")
word = input("Enter a word: ").upper()
word_letters = list(word)
new_code= []
for letter in word_letters:
    try:
        for (index, row) in data.iterrows():
            if row.letter == letter:
                new_code.append(row.code)
    except:
        print("Sorry, only letters in the alphabet please.")
        break
        
print(new_code)

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
try:
    new_code2 = [nato_dict[letter] for letter in word]
except KeyError:
    print("Sorry, only letters in the alphabet please.")
else:
    print(new_code2)