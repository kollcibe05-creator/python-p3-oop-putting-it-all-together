#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition="managable"):
        self.brand = brand
        self.size = size 
        self.condition = condition 
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")              
    pass
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"  

shoe = Shoe("Louis Vuitton", 8)    
print(shoe.brand)
print(shoe.size)
print(shoe.condition)


