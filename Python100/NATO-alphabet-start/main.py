import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter:row.code for (index, row) in data.iterrows()}


invalid = True
while invalid:
    word = input("Enter a word: ").upper()
    try:
        nato_list = [nato[letter] for letter in word]
    except:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(nato_list)
        invalid = False
