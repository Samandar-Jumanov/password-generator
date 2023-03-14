#password generator 
import random 
letter_len_question = input('How much length you wanna make\n ')
symbol_question = input('How much symbol you want \n')
number_question = input('How many numbers you want to add\n ')

print('Welcome to the Password generator')
symbols =['@', '$', '!', '*',')', '(', '+']
numbers =["1", "2", "3", "4", "5", "6", "7", "8", "9"]

letters =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'X', 'W', 'Z']

# password =''

# for chart in range(1, int(letter_len_question) + 1):
#     password+=random.choice(letters)

# for chart in range(1, int(symbol_question) + 1):
#     password+=random.choice(symbols)  

# for chart in range (1, int(number_question) + 1):
#     password+=random.choice(numbers)

# print(password)


#Hard level 

strong_password =[]

for chart in range(1, int(letter_len_question) + 1):
    strong_password+=random.choice(letters)

for chart in range(1, int(symbol_question) + 1):
    strong_password+=random.choice(symbols)  

for chart in range (1, int(number_question) + 1):
    strong_password+=random.choice(numbers)

random.shuffle(strong_password)
pswd = ''
for p in strong_password :
  pswd+=p
print(pswd)
