#week 10 notes, functions
#what is a function
#a function is a named set of instructions you can run whenever you want
#functions let us write code once and reuse it when we need it

#Def(define) a function: create a funciton by starting with def
#Call a function: run the function by using its name with parantheses()
# Parameter: Placeholder variable inside the funciton definition
#Argument: the real value that we pass into the function via the parameter

#create a function that says "Hello"
# def say_hello():
#     print('Hello')
# #call the funciton
# say_hello()

#def telles Pythons: "Im defining a function"
#Coder inside the function must be indented
#Nothing runs until you call it

#Parameters and arguments
# def greet(name):
#     #name is a parameter(a placeholder/variable)
#     print(f'Hello, {name}')
# name=input('Enter your name: ')
# greet(name)
# greet('Carl')
#parameters are like blanks. arguments fill them in
#only time you need a parameter is when your gonna pass info from outside the function into the function

# def greet():
#     name=input('Enter your name: ')
#     print(f'Hello, {name}')
# greet()


#Print vs Return
#A function that prints:
# def hello_print():
#     print('hello world')
# #this shows the text to the user
# #but it does not give a value back to the rest of the program

# #A function that Returns :
# def hello_return():
#     name=input('Enter your name ')
#     return f'Hello, {name}'
# #This sends a value back to wherever the function was called
# #the caller can store it, print it, etc

# # hello_return()
# # hello_print()

# msg=hello_return()
# print(msg)

# result=hello_print()
# print(result)#this will print none because hello_print doesnt return a value back to the function

# #print is for the user while Return is for the program

# #Function example
# #calc program

# def calc(num1,num2):
#     operator=input('What sort of math do you want to do: +,-,*,/')
#     #use if/else to decide what to do
#     #perform the math
#     #print of Return the result
#     if operator=='+':
#         return num1+num2

# print(calc(1,3))#function now has the value of 4


#fake loop
#a function can call itself, this is called recursion
#a function can behave like a loop if it repeats until a condition is met
#if a function is calling itself, it must have a stop condition

#a function that prompts user if they want to continue, if user doesnt want to continue 'loop' stops
#if user says yes, ask them again
# def play_again():
#     answer=input('Again? (y/n): ').lower()
#     if answer=='y':
#         play_again()#calls itself again
#     else:
#         print('goodbye')
# play_again()
