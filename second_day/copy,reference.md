# In python array , list, dist all are mutable

- if we write h1 = []; 
  - h1 = h1;
  - here h1 is list , and list is mutable . when we assign h1 in h2 it not just copy h1 into h2 . It make a new pointer and point there where h1 is pointing.

  - for copying we write like that
    - h2 = h1[:]

# Numbers in python

- for finding power we use (a**b), it means a to the poer b;
- 4*2.4 , instead of this we can write float(4)*2.4. Now it is more readable.
 

#   Some function 
- x = 10
 - s = "Hello\nWorld"

- print(str(s))   # Output: Hello
                #         World

- print(repr(s))  # Output: 'Hello\nWorld'

- repr() => Gives a detailed or unambiguous string version of an object

- x << 2, x is left shifted by2 

#  String

-  string is immutable

- string_name[start:end:hoping];
- string_name.strip() => it remove the spaces from   starting and from ending.
- string_name.replace("string", "your_string") => it replace string to your string in string

- string_name.split(); => it convert string into array, it split the string on the basis of your given data and store it in array
- string_name.find("string") 
- string_name.count("string")
- Placeholder 
  - string_name.format() => it serach {} this paranthesis if found this replace it with your value


- "".join(list_name) => it convert list to string
- len(string_name) => find length
