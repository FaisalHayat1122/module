#functions in pythob
#is a modules in python


#use define modules
def faisal():
    select=input("what you want to use? \n1.calc \n2.marksheet \n3.nothing:").lower()
    if select=="calc":
        num1=int(input("Enter a number 1:"))
        num2=int(input("Enter a number 2:"))
        print(f"This is addition:{num1+num2} \n.This is substraction:{num1-num2} \n.This is multiplication:{num1*num2} \n.This is divison:{num1/num2}")
    elif select=="marksheet":
        obtain=int(input("Enter your obtained marks:"))
        total=500
        per=(obtain/total)*100
        if per>=70:
            grade="A+"
        else:
            grade="Fail"
            print(grade)