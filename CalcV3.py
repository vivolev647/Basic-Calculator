Num1 = 0
Num2 = 0
FinishedVal = 0
inp = input("Please input your calculation: ")
inp = inp.replace(" ", "")
table = [] # Creates a blank table for later use
NumbersTable = []
OperatorLocationTable = []

for q in range(len(inp)): # Loop that adds things into a table
    table.append(inp[q])

OperatorPlusAmount = table.count("+")
OperatorMinusAmount = table.count("-")
OperatorMultiplyAmount = table.count("*")
OperatorDivideAmount = table.count("/")

def OperatorPlusAmount2():
    for b in range(OperatorPlusAmount):
        OperatorLocationTable.append(table.index("+"))
        table[table.index("+")] = "."

def OperatorMinusAmount2():
    for b in range(OperatorMinusAmount):
        OperatorLocationTable.append(table.index("-"))
        table[table.index("-")] = "."

def OperatorMultiplyAmount2():
    for b in range(OperatorMultiplyAmount):
        OperatorLocationTable.append(table.index("*"))
        table[table.index("*")] = "."

def OperatorDivideAmount2():
    for b in range(OperatorDivideAmount):
        OperatorLocationTable.append(table.index("/"))
        table[table.index("/")] = "."
OperatorDivideAmount2()
OperatorMinusAmount2()
OperatorPlusAmount2()
OperatorMultiplyAmount2()

OperatorLocationTable.sort()
print(OperatorLocationTable)

for w in range(len(OperatorLocationTable)):
    Operator = inp[OperatorLocationTable[w]]
    if FinishedVal == 0:
        Num1 = inp[0:OperatorLocationTable[w]]
        try:
            Num2 = inp[OperatorLocationTable[w] + 1:OperatorLocationTable[w+1]]
        except:
            Num2 = inp[OperatorLocationTable[w] + 1:len(inp)]

        
        if Operator == "*":
            FinishedVal = int(Num1) * int(Num2)
        elif Operator == "+":
            FinishedVal = int(Num1) + int(Num2)
        elif Operator == "/":
            FinishedVal = int(Num1) / int(Num2)
        elif Operator == "-":
            FinishedVal = int(Num1) - int(Num2)
    
    else:
        try:
            Num2 = inp[OperatorLocationTable[w] + 1:OperatorLocationTable[w+1]]
        except:
            Num2 = inp[OperatorLocationTable[w] + 1:len(inp)]

        if Operator == "*":
            FinishedVal = FinishedVal * int(Num2)
        elif Operator == "+":
            FinishedVal = FinishedVal + int(Num2)
        elif Operator == "/":
            FinishedVal = FinishedVal / int(Num2)
        elif Operator == "-":
            FinishedVal = FinishedVal - int(Num2)

    
print(f"Your Finished Value is: {FinishedVal}")









