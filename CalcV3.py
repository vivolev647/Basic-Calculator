operand_one = 0
operand_two = 0
result = 0
inp = input("Please input your calculation: ")
inp = inp.replace(" ", "")
table = [] # Creates a blank table for later use
numbers_table = []
operator_location_table = []

for q in range(len(inp)): # Loop that adds things into a table
    table.append(inp[q])


operator_plus_amount = table.count("+")
operator_minus_amount = table.count("-")
operator_multiply_amount = table.count("*")
operator_divide_amount = table.count("/")

def operator_plus_amount_function():
    for i in range(operator_plus_amount):
        operator_location_table.append(table.index("+"))
        table[table.index("+")] = "."

def operator_minus_amount_function():
    for i in range(operator_minus_amount):
        operator_location_table.append(table.index("-"))
        table[table.index("-")] = "."

def operator_multiply_amount_function():
    for i in range(operator_multiply_amount):
        operator_location_table.append(table.index("*"))
        table[table.index("*")] = "."

def operator_divide_amount_function():
    for i in range(operator_divide_amount):
        operator_location_table.append(table.index("/"))
        table[table.index("/")] = "."
operator_divide_amount_function()
operator_minus_amount_function()
operator_plus_amount_function()
operator_multiply_amount_function()

operator_location_table.sort()
print(operator_location_table)

for i in range(len(operator_location_table)):
    operator = inp[operator_location_table[w]]
    if result == 0:
        operand_one = inp[0:operator_location_table[w]]
        try:
            operand_two = inp[operator_location_table[w] + 1:operator_location_table[w+1]]
        except:
            operand_two = inp[operator_location_table[w] + 1:len(inp)]

        
        if operator == "*":
            result = int(operand_one) * int(operand_two)
        elif operator == "+":
            result = int(operand_one) + int(operand_two)
        elif operator == "/":
            result = int(operand_one) / int(operand_two)
        elif operator == "-":
            result = int(operand_one) - int(operand_two)
    
    else:
        try:
            operand_two = inp[operator_location_table[w] + 1:operator_location_table[w+1]]
        except:
            operand_two = inp[operator_location_table[w] + 1:len(inp)]

        if operator == "*":
            result = result * int(operand_two)
        elif operator == "+":
            result = result + int(operand_two)
        elif operator == "/":
            result = result / int(operand_two)
        elif operator == "-":
            result = result - int(operand_two)

    
print(f"Your Finished Value is: {result}")









