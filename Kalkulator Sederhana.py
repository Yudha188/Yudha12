#Logika matematika dasar

x = int(input("Masukan Nilai x = "))
ops =input("opr (+ - * / %) = ")
y = int(input("Masukan Nilai y = "))
if ops == "+":
    print(x, "+",y, "=", x+y)
elif ops == "-":
    print(x, "-",y, "=", x-y)
elif ops == "*":
    print(x, "*",y, "=", x*y)
elif ops == "/":
    print(x, "/",y, "=", x/y)
elif ops == "%":
    print(x, "%",y, "=", x%y)