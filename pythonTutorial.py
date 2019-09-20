#Hello World goes to the console
print("Hello World")

#accepts user text from the console and stores it in name
name = input("Please enter your name: ")

#says hey to name
print("Hey ", name, "! :)")

#control structures: if/elif/else block <-(for making decisions)
age = int(input("What is your age?: "))

if age >= 18:
  print("You are an adult\n") #Note: \n prints a new line (like pressing enter)
elif age > 0:
  print("You are a child\n")
else:
  print("What???")


#i goes from 0 to 9 <- note that the range is 10 while the last
#number is 9...can you see why? (count the amount of numbers from 0 to 9)
for i in range(10):
  print(i)

#makes a new line(like pressing enter)
print("\n")

#i goes from 4 to 10 <-(not including 10)
for i in range(4,10):
  print(i)

#another new line
print("\n")

#i goes from 4 to 10 but is incremented by 2 each time
for i in range(4, 10, 2):
  print(i)

#another newline
print("\n")
#broken while loop
''' <- Note that this is how you comment out multiple lines of code
xyz = 10
while xyz > 0:
  print xyz
''' 

#this while loop works
xyz = 10
while xyz > 0:
  print (xyz)
  xyz = xyz - 1

print("\n")

#quadratic formula: y = -b +- Sqrt[b^2 - 4ac]/(2a)
a = 1
b = -2
c = 1

y1 = -b + (b**2 - 4 * a * c)**0.5 / (2*a)
y2 = -b - (b**2 - 4 * a * c)**0.5 / (2*a)
print("y1 = ", y1, "\ny2 = ", y2)
print("\nGoodbye :)")
