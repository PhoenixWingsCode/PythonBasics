#Loops are used to repeat instructions
count=1#iterator
while count<=5:
    print("hello",count)
    count+=1
#Iteration means one loop cycle has been completed
print(count)

num1=1
while num1<=5:
    print(num1)
    num1+=1

print("Loop ended")

num2=1
while num2<=5:
    if(num2==3):
        break#used to terminate the loop when encountered
    print(num2)
    num2+=1

print("Loop ended")

#continue: terminates execution in the current iteration and continues execution of the loop with the next iteration
num3=0
while num3<=5:
    if(num3==3):
        num3+=1
        continue
    print(num3)
    num3+=1

print("Loop ended")

#Loops are used for sequential traversal.
#For traversing list, string, tuples, etc.

nums=[1,2,3,4]
for num in nums:
    print(num)

print("Numbers")

veggies=["potato","brinjal","ladyfinger","cucumber"]
for veg in veggies:
    print(veg)

print("Vegetables")

#For traversing use for loop and for working with the condition use while loop

tup=(1,2,3,7,2,1,4,3)

for val in tup:
    print(val)

print("List using for loop")

name="hiral"
for val in name:
    if(val=='a'):
        print("a found")
        break
    print(val)
else:
    print("END")

"""
Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before 
a specified number.

range(start?, stop, step?)
starting value is optional
stepping value is also optional
stop number will not be printed
"""

for val in range(5):#range(stop)
    print(val)

print("Loop ended")

for val in range(2,5):#range(start,stop)
    print(val)

print("Loop ended")

for val in range(2,10,2):#range(start,stop,step)
    print(val)

print("Loop ended")


"""
Pass is the null statement that does nothing.
It is used as a placeholder for future code.
"""

for val in range(5):
    pass

print("Loop ended")