"""
Michael mensah - Lab 5 
"""

#3.1

alien_color = 'green'
if alien_color == 'green':
    print ("You have scored 5 points! Congrats!")
    
#3.2

else:
    print ("You have scored 10 points! Good job!")
    
#3.3

favorite_fruits = ['apple','grape','orange']
if 'apple' in favorite_fruits:
    print('Apples are the best!')
if 'grape' in favorite_fruits: 
    print('Grapes are awesome!')
if 'orange' in favorite_fruits:
    print ('Oranges are amazing!')
if 'strawberry' in favorite_fruits:
    print ('Strawberries rock!')
if 'watermelon' in favorite_fruits:
    print ('Watermelon is the best melon!')

#3.4

age = 10
if age < 10:
    print('You are a kid.')
elif age <20:
    print('You are a tennager.')
else:
    print('You are an adult.')
    if age>65:
        print('You are and elder.')