#What is a boolean?
#A boolean is a value that is either true or false

# print(5>10)
# print(10<20)
# print(3>=74)
# print('cat'=='Cat')

#any expression that evaluates to true of false is a boolean expression
#if statements use these to decided what to run

#how can you create a conditional statement based on user input?
# answer=input('Do you want to continue? (yes or no)').lower()
# if answer=='yes':
#     print('Continuing the program....')
# elif answer=='no':
#     print('Exiting the program now')
# else:
#     print('Invalid response')

#comparison operators
# == equal to

# !=not equal to

# <less than

# >greater than

# <= less than or equal to

# >= greater than or equal to

# score=85
# print(score>75)
# print(score<75)
# print(score==100)

# #Using AND & OR
# temp=72
# if temp>=72 and temp <=75:
#     print('This is comfortable room temp')

#When using AND, both conditions must be TRUE
#When using OR, at least one condition must be TRUE

#I want this program to output('You dont have class today')
# day='Saturday'
# is_holiday=False
# # if day=='Saturday' or day=='Sunday' or is_holiday:
# #     print('You dont have class today')
# if day=='Saturday':
#     print('No class its saturday')
# elif day=='Sunday':
#     print('No class its sunday')
# elif is_holiday==False:
#     print('Its a holiday')

#Chained Comparisons
# score=75
# #How to write out 65 is <= score but less than 90
# if 60 <= score <90:
#     print('Score is passing but not perfect')

#Using if + elif + else
#This is a simple 3 category example
#This program prints out the shipping cost based on the order price
#When using any sort of money input we will use float
# total=float(input('Enter your order total: '))
# if total<25:
#     print('Shipping is $10')
# #if user input is less than 50, they get $5 shipping
# elif total<50:
#     print('You get $5 shipping! ')
# else:
#     print('Free shipping')

#Compare == & is
# list1=[1,2,3]
# list2=[1,2,3]
# list3=list1
# print(list1==list2) #true: content are equal
# print(list1 is list2) #false: Different objects in memory
# print(list1==list3) #true:content still the same
# print(list1 is list3) #true: list3 points to the same object as list1

#== compares values/content
# is compares identity(are you literally the same object? )

#Two different boxes can have the same stuff inside (==)
# But they're still two different boxes(is)

#multi brand example
# program that tells me if the number is positive or negative
number=int(input('Enter your number ' ))
if number<0:
    print('Negative')
elif number>0:
    print('positive')
else:
    print('Your number is 0')