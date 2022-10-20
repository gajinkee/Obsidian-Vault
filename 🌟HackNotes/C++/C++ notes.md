```C++
cin << Enter your input:

cin.ignore

```

## Operators
1. Arithmetic
	- + - * / 
	- ++ and --
2. Relational
	-  > < >= == != etc
3. Logical
	- && || !
4. Bitwise
	-  Test, set or shift bits in a byte or word
	- & AND 
	- | OR
	- ==^ *XOR* == 
	- ~ NOT >> shift right , << shift left
	
## Iteration & Conditional structures
1. Selection
	 1. if
	 2. switch/case/default
1. Iteration 
	1. while
	2. for (initialisation; condition; increment) {}
	3. do-while
1. Jump 
	1. break
	2. continue
	3. goto
	4. return

## Pointers
- Variable that holds memory
- if a contains address of b, a points to b
```c++
type *name;
```
type: defines the type of variable the pointer points to
pointers must be declared as above

```c++
y=1
p1 = &y;
z = *p1;
p2 = p1
*p2 = 5
```
& returns the memory adress
	( ie above, the ==**address of y**== is stored in x
`*` returns the value located at the memory address
	(ie z give the value y)
At the last part, value of y is changed to 5 by proxy of `*p2 = 5` 
	(since `*p2` is the value of y)

## Functions

```C++
type function_name (param1,param2,...){
	statements;
	return(return_value);
};

void function_name(param1,...){
	statement;
	//Void means no value is returned
}
```
where:
	- type specifies type of data returned by function
	- fuction name anyt identifier
	- params variables that receive their values when function is called
note: 
 - Main is always first function to be called
 - C++ uses call by value
	 - code in function does not alter args in the caller (ie changes in stuff in function wont affect main, only the returned value matters)
	 - The variable is copied into the 
 - Call by reference can by done by:
	 ````c++
	 // int& means passing the variable itself and not a copy of its value
	 void swap(intt& x, int& y){
		int tmp;
		
		temp = *x ; 
		*x = *y; //Exchanges the actual variable of x and y not their copies
		*y = temp;
	 }
	 ````