def add (a,b):
    return(a+b)
def minus (a,b):
    return(a-b)
def divide (a,b):
    if b == 0:
        return ("Error : Value Cannot Divide With 0")
    return (a/b)
def multiply (a,b):
    return(a*b) 

print("Welcome To Simple Calculator Made By Nasir Memon")
print("Please Input Your Selection From Below Option\nPRESS A FOR ADDITION:\nPRESS B FOR MINUS:\nPRESS C FOR DIVISION:\nPRESS D FOR MULTIPLICATION:")  
ANSWER = input("Please Input Your Selection : ").upper()
NUM_1 = float(input("Please Input Your First Number : "))
NUM_2 = float(input("Please Input Your Second Number : "))
if ANSWER == "A":
    print("Your Answer Is After Addition Is", add(NUM_1 , NUM_2))
elif ANSWER == "B":
    print("Your Answer Is After Minus Is", minus(NUM_1 ,NUM_2))
elif ANSWER == "C":
    print("Your Answer Is After Division Is", divide (NUM_1 ,NUM_2))
elif ANSWER == "D":
    print("Your Answer Is After Multiply Is", multiply(NUM_1,NUM_2))
else:
    print("Please Input From Provided Option A,B,C OR D")




