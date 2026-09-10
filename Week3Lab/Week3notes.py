# a=10
# #reassign the variable
# a=12
# #It's just overriding the previous variable
# b=12
# sum=a+b
# print(f"The sum of the 2 variables is {sum}")
# #exponents
# sum=a**b

# #Whats the difference betweem INT and FLOAT
# #INT=Whole numbers (decimal point, 1,2,3,4)
# #Float=Decimal numbers(10.0, 5.0, 6.6)
# # #aslong as they have decimal they are float numbers
# # num1=10
# # num2=2.25

# # print(num1,type(num1))


# # #Between these two operators / and //, which is INT value and which gives float
# # #// is floor division, gives whole number
# # print(10//3)
# # #/ is regular division and gives Float number



# # print(10/3)
# # user_text=input('type something: ')
# # print(user_text)
# # print(type(user_text))
# # #no matter what the input is, the data the of user input is always string

age_text=input('How old are you now? ') #age_text is a string
age_number=int(age_text) #this converts our string variable value into an INT variable
print(age_number,type(age_number))
print(f'Next year you will be {age_number+1}')


# #string is what goes between "", String holds no numeric value. Text data
# #Indexing is searching text 
# word='Python'
# print(word[0]) #This will index the first character
# # print(word[1]) #second character
# # print(word[2]) #third character

# # #slicing (substring) is when we want to show a range of character
# # word2='Programming'
# # print(word2[0:4]) #I want to print the first 4 characters
# # #print(variable_name[Start:End])
# # #start at said number and stop right before End
# # print(word2[3:8])
# # print(word2[:6])
# # #you dont have to put zero
# # print(word2[6:])
# # # #same for the end
# # # print(word2[10:])

# phrase='Hello, World!'
# print(phrase.upper()) #to uppercase everything use .upper() function
# print(phrase.lower()) #to lowercase everything use .lower() function

# #List is an ordered collection of values, store within a variable using [
# numbers=[10,2,3,5]
# word=['cat','dog','hamster']
# mized=['snake',10.25,3]
# print(numbers[0:3])
# print(numbers)
# print(numbers[3])

# word.append('Gerbil')
# print(word)


# word.remove('cat')
# print(word)