import math

# Create sine function
def sine(x):
    # declare initialize counter and sin value
    c = 0
    sine = 0
    
    while c <= b:
      i = (2*c) + 1
      s = (((-1)**c) * (x**(i))) / math.factorial(i)
      sine = sine + s
      c = c + 1    
      print(sine)
    return sine

#main function

# Get the input from the user
x = int(input('What is the value of x? '))
b = int(input('What is the number of iterations? '))

sine = sine(x)

# Display the comparison for the function and the result
print('The value of sin(x) = ', sine)
print('Using the math.sine function sin(x) = ', math.sin(x))
