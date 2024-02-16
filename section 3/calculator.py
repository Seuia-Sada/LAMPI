
print("insert the expression. It have to follow the foward rules <number1> <operator> <number2>\n")

operator = ''
num1 = ""
num2 = ""

i_buf  = ""

for read in input():
    if read != ' ':
        i_buf += read

result = None

if not i_buf.isdigit():
    for i in range(len(i_buf)):
        if i_buf[i].isdigit():
            if operator == '':
                num1 += i_buf[i]
            else:
                num2 += i_buf[i]

        elif operator == '':
            operator = i_buf[i]
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

