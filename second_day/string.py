chai =  "masala chai"
slice_chai = chai[0:5]
print(slice_chai)
slice_chai = chai[0:10:2] 
# here we hope 2        
print(slice_chai)
chai.strip()
print(chai)
chai = "Lemon, Ginger, Masala, Mint"
print(chai.split(", "))

abhi = "Abhishek Kumar Kamat"
print(abhi.split(" "))
# here split function convert string into array based on " "
print("".join(abhi))
# here join function convert array into string based on "" and space between all the values;
print(len(abhi))
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

