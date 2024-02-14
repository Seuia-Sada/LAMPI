
print("insert the expression.\n\t it have to follow the foward rules <number1> <operator> <number2>\n")

i_buf  = input()

operator = ''
num1 = ""
num2 = ""

result = ...

if not i_buf.isdigit():
    i_size = len(i_buf)
    i = 0

    while i < i_size:
        if i_buf[i].isdigit():
            if operator == '':
                num1 += i_buf[i]
            else:
                num2 += i_buf[i]

        elif i_buf[i] != ' ':
            operator = i_buf[i]

        i += 1

else:
    num1 = i_buf

    print("num1:", num1)
    
    operator = input("opearator: ")
    num2 = input("num2: ")

num1 = int (num1)
num2 = int (num2)

if operator == '+':
    result = num1 + num2 

elif operator == '-':
    result = num1 - num2 

elif operator == '*':
    result = num1 * num2 

elif operator == '/':
    result = num1 // num2 

elif operator == '%':
    result = num1 % num2

print(f"\n{num1} {operator} {num2} = {result}")

