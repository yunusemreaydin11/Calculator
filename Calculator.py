print("Welcome To Calculator!")

first_number = float(input("First Number: "))
second_number = float(input("Second Number: "))
process = input("+ , - , x , / : ")
if process == "+":
    def addition(a,b):
        addition_result = a + b
        print(f"{a} + {b} = {addition_result}") 
    addition(first_number,second_number)
         
elif process == "_":
    def subtraction(a,b):
        subtraction_result = a - b
        print(f"{a} - {b} = {subtraction_result}")
    subtraction(first_number,second_number)
        
elif process == "x":
    def multiplication(a,b):
        multiplication_result = a * b
        print(f"{a} x {b} = {multiplication_result}")
    multiplication(first_number,second_number)
       
elif process == "/":
    def division(a,b):
        division_result = a / b
        print(f"{a} / {b} = {division_result}")
    division(first_number,second_number)
        

else:
    print("Please enter a valid transaction!")
        

     