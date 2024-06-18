import pandas as pd
import re


def checkProfanity(df, word, counted):

    regex_pattern = r'\b{}\b'.format(re.escape(word))

    if df['text'].str.contains(regex_pattern, regex=True).any():
        counted += 1
        print("Found")
        print(counted)
    else:
        print("Not Found")
    
    return counted  

def check_word(df, word):
    print("Checking", word)
    letters = list(word)
    arraybaseword = []
    for letter in letters:
        row_index = df.map(lambda x: x == letter).any(axis=1)
        if row_index.any():
            first_item = df.loc[row_index, df.columns[0]].values[0]
            if(first_item != letter):
                print(f"The letter '{letter}' appears in the DataFrame. The letter '{first_item}' was hidden.")
                arraybaseword.append(first_item)
            else:
                arraybaseword.append(first_item)
        else:
            print(f"The letter '{letter}' does not appear in the DataFrame.")
        
    baseword = ''.join(arraybaseword)    
    return baseword

if __name__ == "__main__":
        
        df = pd.read_csv('profanity_en.csv')
        altdf = pd.read_csv('alt.csv')

        removed_columns = df[['text']] #remove other columns
        print("Running")
        userinput = input("Filter Text: ")
        print(userinput)
        
        splitinput = userinput.split()
        itemcount = len(splitinput)
        counted = 0
        for word in splitinput:
            clean_input = check_word(altdf, word)
            print("Original: ",word)
            print("Cleaned: ", clean_input)
            counted = checkProfanity(df, clean_input, counted)
            
        print("Words Present:", itemcount)
        print("Words Flagged: ", counted)
