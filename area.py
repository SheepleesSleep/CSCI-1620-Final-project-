from math import *
class area():
    ''''
    This class is used to calculate the area of various shape specified by the user.
    All Areas are calculated as floats.
    '''
     
    def circle(radius:float) -> float:
        """
        This function returns the area of a circle, given the radius
        :param radius: the radius used to calculate the area of the circle
        :throws VauleError: if radius is not a positive input or greater than zero
        :throws TypeError: If the input type is not a int or float
        """
        if type(radius) != int and type(radius) != float:
            raise TypeError('Non numerical input')
    
        if radius <= 0:
            raise ValueError("Not positive")
        
        return (pi) * pow(radius, 2)
    
    def square(length: float) -> float:
        """"
        This function returns the area of a square given the length 
        :param length: The length of the square's sides.
        :throws VauleError: if length is not a positive input or greater than zero
        :throws TypeError: If the input type is not a int or float
        """
        if type(length) != int and type(length) != float:
            raise TypeError('Non numerical input')
    
        if length <= 0:
            raise ValueError("Not positive")    
       
        return  pow(length, 2)
    
    def rectangle(length: float, width: float) -> float: 
        """
        This function returns the area of a rectangle give the length and width
        :param length: The measurement passed for the length of the rectangle.
        :param width: The measurement passed for the width of the rectangle
        :throws VauleError: if length or width is not a positive input or greater than zero
        :throws TypeError: If the input type is not a int or float
        """
        if type(length) != int and type(length) != float:
            raise TypeError('Non numerical input')
    
        if length <= 0:
            raise ValueError("Not positive")
        
        if type(width) != int and type(width) != float:
            raise TypeError('Non numerical input')
    
        if width <= 0:
            raise ValueError("Not positive")
        
        return length * width
    
    def triangle(base: float, height: float) -> float:
        """
        This function returns the area of a triangle given the base and height
        :param base: The measurement passed for the base of the triangle
        :param height: The measurement passed for the height of the triangle
        :throws VauleError: if height or base is not a positive input or greater than zero
        :throws TypeError: If the input type is not a int or float
        """
        if type(base) != int and type(base) != float:
            raise TypeError('Non numerical input')
    
        if base <= 0:
            raise ValueError("Not positive")
        
        if type(height) != int and type(height) != float:
            raise TypeError('Non numerical input')
    
        if height <= 0:
            raise ValueError("Not positive")
        
        return(0.5) * base * height  
        