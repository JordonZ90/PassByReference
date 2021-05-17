def box(random_parameter):
    random_parameter.append("Hello")  # Value of the argument


#  When a function is called, the values of the arguments are copied to the parameter variables


cube = [1, 2, 3]
box(cube)  # Cube is the parameter value
print(cube)
