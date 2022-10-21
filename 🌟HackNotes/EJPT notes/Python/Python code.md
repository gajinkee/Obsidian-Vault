## <u>Dictionaries</u>
#codenotes
- mapping objects
- key pair mapping
- like list but must use keys to access value instead of indices

``` python
dictionary = {'first': 1 ,"second" : 'two'}
```
element on left is key, right is value
Key is immutable (cannot be changed) but value can be changed

Note: if no key:value exist, its added at the beginning

### Methods 
dict.values() : return all values in dict
dict.keys() : returns all keys
dict.items() : returns all key and value pairs
```python
"key" in dictonary #returns bolean if key exists in dict
"value" in dictionary.values() #returns bolean for exitence of values

dict.get("key","msg if not found") #returns the rightside if key not found 

```

## Scopes
```python
def my_sum(x,y):
	""" Returns sum"""
	return 
x= 123

#global scope prints 123
print(x)

#local scope inside function prints 1+2=3
print(my_sum(1,2))


```

Global scope values can be changed
```python
def change():
	global x 
	x = 1
x = 3

#prints 3
print(x)

change()
#prints 1
print(x)

```

Functions stored in variables
```python
def a(x,y):
	return(x+y)
def b(x,y)
	return(x-y)

#differs from string assignment as no quotes used unlike 3
dictionary = {
	1 : a , 
	2 : b ,
	3 : "a"
}

user_input = int (input("""Select function:
1) Sum
2) Minus						
"""))

if user_input in dictionary :
	x = int(input("First num:"))
	y = int(input("Second num:"))
	#function is returned by dictionary[user_input]  
	#variables are passed tru (x,y)
	result = dictionary[user_input](x,y)
else:
	print("wrong input")

```

## Modules

```python
#the functions are called objects(contain more than functions) in python, so objects in a module
from module_name import somefunction,anotherfunct
from module_name import * #imports all functions

somefunction()
anotherfunct()

#or (above is preferred)

import module_name

module_name.function
module_name.another
```