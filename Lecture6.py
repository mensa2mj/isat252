"""
Lecture 6
"""
#demo_str = 'this is my string'
#for str_item in demo_str:
#     print(str_item)

#for word_item in demo_str.split():
#        print(word_item)
#        for str_item in word_item:
#            print(str_item)

#print(range(5))
#for each_number in range(1,5):
#    print(each_number)
    
num_list = [213,321,123,312]
max_item = num_list[0]  #max item is the place holder, and uses the first item as the initial value
for each_number in num_list:
    if max_item <= each_number:
        max_item = each_number
print(max_item)