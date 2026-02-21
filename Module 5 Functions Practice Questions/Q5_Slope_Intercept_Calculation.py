'''
You are given the slope m and the y-intercept b of a line, along with a value x. Your task is to calculate and return the value of y 
using the equation of a line in slope-intercept form:
'''

def calculate_y(slope, intercept, x): 
    return slope*x + intercept 

print(calculate_y(2,3,4))
print(calculate_y(1.5,-2,2))  