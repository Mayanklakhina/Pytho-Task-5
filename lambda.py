
# Using lambda funtion in another function: 

def func(i,j):
    return lambda x,y : (x + y) + (i-j)


result = func(2,3)                   
print(result(13,15))