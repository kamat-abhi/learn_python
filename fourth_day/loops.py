numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
pos_num = 0
for num in numbers:
    if num > 0:
        pos_num += 1
print("Positive numbers:", pos_num)        

n = int(input("Enter your number: "))
sum =0
for i in range(1, n+1):
    if i%2 == 0:
        sum += i
print("Sum of even numbers:", sum)      

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

string = input("Enter your string for reverse: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string) 

string = input("Enter your string: ")
counter = 0
temp = string[0]
for i in range(1, len(string)):
    if string[i] == temp:
        print("Duplicate character:", string[i])
        counter += 1
        break
    else:
        temp = string[i]
if counter == 0:
    print("No duplicate characters found")        