"""
Lecture 9 - Class
"""

class car:
    maker = 'toyota'
    def __init__(self, input_model):
        self.model = input_model
        
#my_corolla = car('corolla')
#print(my_corolla.maker)
#print(my_corolla.model)

#my_highlander = car('highlander')
#print(my_highlander.maker)
#print(my_highlander.model)

    def report(self):
        return self.maker, self.model
    
my_car = car('corolla')
print(my_car.report())

my_car.maker = 'ford'
print(my_car.report())