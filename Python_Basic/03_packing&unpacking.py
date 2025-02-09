
packed_values = 1,2,3,4,5
print(packed_values)

numbers = [1,2,3,4,5]
a, *b, c = numbers
print(a); print(b); print(c)

def my_func(*objects):
    print(objects)
    print(type(objects))
my_func(1,2,3,4,5)

packed_values = 1,2,3,4,5
a,b,c,d,e = packed_values
print(a,b,c,d,e)

def my_function(x,y,z):
    print(x,y,z)

names = ['alice','jane','peter']
my_function(*names)

def my_function(x,y,z):
    print(x,y,z)
my_dict = {'x':1, 'y':2, 'z':3}
my_function(**my_dict)