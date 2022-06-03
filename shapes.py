from re import A
from tokenize import Double
from turtle import circle


class Circle:
    
    def __init__(self,r):
          self.r= r
   
    def area(self):
        A=round(3.142*(self.r**2),3)
        return A 
    
    def circumfrence(self):
        C = round(3.142*(self.r*2),3)
        return C

class Square:
        def __init__(self,a):
             self.a=a
             
        def area(self):
            A=(self.a**2)   
            return A  
        
        def perimeter(self):
            P=4*self.a
            return P 
        
class Rectangle:
    def __init__(self,w,l):
        self.w=w
        self.l=l        
            
    def area(self):
        A=self.w*self.l
        return A
    
    def perimeter(self):
        P=2 * (self.l+ self.w) 
        return P
    
class Sphere:
    def __init__(self,r):
        self.r= r
    
    def surface_area(self):
        A=4*3.142*(self.r**2)
        return A
    
    def  volume(self):
        v=(4/3)*(3.142 *self.r**3)
        return v
        
               