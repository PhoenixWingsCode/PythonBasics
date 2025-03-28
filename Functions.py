#Functions
#Block of statements that perform a specific task

"""def func_name(param1, param2..):
    #some_work
    return val

func_name(arg1,arg2..)function call """

def sum(num1, num2):
    sum = num1+num2
    print(sum)
    return sum

sum(15, 10)

#When you give default value it goes from the last
def cal_prod(b, a=2):
    return a * b

product = cal_prod(4)
print(product)

print("hiral", end=" ")#sep = " "
print("kanakhara")#end = "\n"