"""
Michael Mensah - Lab 3
"""
#3.1
str_list = ['a','d','e','b','c']
str_list.sort()
#3.2
str_list.append('f')
#3.3
str_list.remove('d')
print(str_list)
#3.4
print(str_list[2])
#3.5
my_list = ['a','123',123,'b','B','False',False,123,None,'None']
print(set(my_list))
#3.6
print(len('This is my third python lab'))
#3.7
num_list = [12,32,43,35]
x,y = 12,35
print(x,y)
#3.8
game_board = [[0,0,0],[0,0,0],[0,0,0]]
print(game_board)
game_board[1]=[0,1,0]
print(game_board)