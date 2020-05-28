"""
Michael Mensah - Lab 7
"""

#3.1

i = 0
while i < 6:
    if i !=3:
        print(i)
    i=i+1

#3.2

num = 1
result = 1
while num <= 5:
    result = result * num
    num = num+1
print(result)

#3.3

number = 1
ans = 0
while number <=5:
    ans = ans + number
    number = number+1
print(ans)

#3.4

variable = 3
product = 1
while variable <= 8:
    product = product * variable 
    variable = variable +1
print(product)

#3.5

num1 = 1
prod1 = 1
while num1 <=8:
    prod1 = prod1 * num1
    num1 = num1 +1
    
num2 = 1
prod2 = 1
while num2 <=3:
    prod2 = prod2 * num2
    num2 = num2 +1

final_answer = (prod1/prod2)
print(final_answer)


#3.6

num_list = [12,32,43,35]
while num_list:
    num_list.remove(num_list[0])
print(num_list)