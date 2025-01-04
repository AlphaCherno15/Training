#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
name_list = []
with open("Input/Names/invited_names.txt") as data:
    names = data.readlines()
    for name in names:
        new_name = name.strip()
        name_list.append(new_name)
with open("Input/Letters/starting_letter.txt") as data:
    letter = data.read()
    for name in name_list:
        new_letter = letter.replace("[name]", name)
        print(new_letter)
        with open(f'Output/ReadyToSend/Letter For {name}.docx', mode="w") as dt:
            dt.write(f'{new_letter}')