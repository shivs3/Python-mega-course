print('Hello Hex')

# Enter First number:
# Enter Second Number:
# Enter 1 for addition, 2 for substraction, 3 for multiplication
# 4 for division and 5 for exit:

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
while(True):
    num1 = float(input('Enter the first Number:'))
    num2 = float(input('Enter the second Number:'))
    print('Enter:\n1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division\n5 for EXIT')
    opt = int(input('Enter your Choice: '))
    if opt==1:
        res = add(num1,num2)
        print('The sum is ',res)
    elif opt==2:
        res = sub(num1,num2)
        print(res)
    elif opt==3:
        res = mul(num1,num2)
        print(res)
    elif opt==4:
        res = div(num1,num2)
        print(res)
    elif opt==5:
        print('Thank You')
        break