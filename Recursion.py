def show(num):
    if(num == 0):
        return
    print(num)
    show(num - 1)

show(5)

print("Show ended")

def fact(num):
    if(num==0 or num==1):
        return 1
    return num * fact(num-1)

print(fact(5))

print("Factorial ended")