"""
Lab 6 - Michael Mensah
"""

#3.1

for num in range(6):
    if num != 3:
        print(num)
        
#3.2

result_32=1
for num in range (1,6):
    result_32 = result_32 * num
print(result_32)

#3.3

result_33 = 0
for num in range (1,6):
    result_33 = result_33 + num
print(result_33)

#3.4

result_34 = 1 
for num in range (3,9):
    result_34 = result_34 * num
print(result_34)

#3.5

product = 1
for num in range (1,9):
    product = product*num
divisor = 1
for number in range (1,4):
    divisor = divisor*number
final_answer = (product/divisor)
print(final_answer)

#3.6
result = 0
for word in 'This is my sixth string'.split():
    result = result+1
print(result)

#3.7

my_tweet = {
            "favorite_count":1138,
            "lang": "en",
            "coordinates": (-75, 40),
            "entities": {
                         'hashtags': [" Preds ", "Pens", " SingIntoSpring "]
                        }
           } 
result_37 = 0
for hashtag in my_tweet['entities']['hashtags']:
    result_37 = result_37+1
print(result_37)