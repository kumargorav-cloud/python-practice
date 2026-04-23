# data types in python
#numeric data type=>(int,float,complex)
int_type = 4235
float_type = 2435.523
complex_type = 24+253j
print(type(int_type))
print(type(float_type))
print(type(complex_type))

#sequence data types=>(tuple,list,range,string)
string_type = "this is string data type"
tuple_type = (423,'gorav',4236,{'name':'gorav'})
list_type = ['akask''abinavh','suryansh']
range_type = range(25)
print(type(string_type))
print(type(tuple_type))
print(type(list_type))
print(type(range_type))
#mapping data types=>(dict)
dict_type = {'name':'gorav','class':'mca','college':"chandigarh university"}
print(type(dict_type))
# set types =>(set,frozenset)
set_type = {'papaya','animal','banyan','grape','watermelon'}
print(type(set_type))
#boolean and none type => (bool,none(absence of a value or none))
bool_type = True
bool_type2 = False
none_type = None
print(type(bool_type))
print(type(bool_type2))
print(type(none_type))
#binary type => (bytes,bytearray,memoryview)


# Create a mutable bytearray
data = bytearray(b"Hello World")

# Create a memoryview
mv = memoryview(data)

# Slice without copying (points to original memory)
view_slice = mv[0:5]

# Modify the original data through the view
mv[0] = 74  # ASCII for 'J'
print(data)  # Output: bytearray(b'Jello World')