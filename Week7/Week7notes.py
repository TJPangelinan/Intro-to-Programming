#What is a loop
#Loop repeats code
#Python uses WHILE and FOR loops, only two types of loops. A FOR loop repeats a certain amount of times, a WHILE loop goes on 

#repeat this loop 3 times
# for number in range(3):
#     #print Hello each time the loops runs
#     print('Hello')

#While loops
#a while loop repeats while a condition is true
#create a starting variable
# number=1
# #keep looping while number is less than or equal to 5
# while number<=5:
#     #print the current value of number
#     print(number)
#     #add 1 to number after each loop
#     number+=1

#make sure something changes inside a WHILE loop. Other wise you may create an infinite loop

#WHILE loops with user input
#a while loop is useful when you want to keep asking until a user gives a valid answer

#Ask user for their age
# age=int(input('enter your age: '))
# #want to keep looping if the age is greater than 1 or greater than 20
# while age <1 or age > 120:
#     print('Invalid age')
#     #ask the user to their age again
#     age=int(input('enter your age: '))
# #this runs after loop finishes
# #loop stops ince the condition becomes false
# print('Age is valid')


#for loops
#a for loop works through items one at a time

#create a list containing
# games=['Minecraft',"Mario",'Zelda']
# #take one item from the games list at a time
# for game in games:
#     #print the current game
#     print(game)

#using RANGE()
#range() is a sequence of numbers

#start at 2 and stop before 8
# for number in range(2,8):#2 is our starting point and we will stop before 8
#     print(number)
    #remember the ending number in range() is not included

#loop through 2-7
# for number in range(2,8):
#     #multiply the number by itself
#     square=number*number#print the squared number
#     print(square)
     


#looping through strings
# a string can be looped through one character at a time
#store a string value inside a variable
# word='Tanks'
# #take one character from the string at a time
# for letter in word:
#     #print the current letter
#     print(letter)



#using BREAK
#break stops a loop early
#loop through number 1-10
# for number in range(1,11):
#     #print the current number
#     print(number)
#     #Want to stop the loop when number is equal to 5
#     if number==5:
#         #stops the loop immediately
#         break


#Nested loops
# nested loop is a loop inside another loop
#outer loop that runs through 1,2,3
# for number in range(1,4):
#     #inner loop also runs through 1,2,3
#     for number2 in range(1,4):
#         #print the current value from both loops
#         print(number,number2)


 
#choosing the right loop
#use a while loop when repitition depends on a condition
#keep looping while answer is not yes
# answer=input('Enter yes ')
# while answer !='yes':
#     #ask the user again
#     answer=input('Enter yes')


# #use a FOR loop when working through items
# #go through each item in the list
# itemlist=[]
# for item in itemlist:
#     #print the current item
#     print(item)


# #use for with range() when working through numbers
# #loop through numbers 1-10
# for number in range(1,11):
#     #print the current number
#     print(number)