import time
#Task1 Creating Dictionary of Students Marks

reg= { }  #creating register as dictionary to store name and marks
n=int(input("How many data you want to input: "))
for i in range(n):
    name, mark = input(f"Student {i+1} (Name Marks):").lower().split()
    mark=int(mark)
    reg[name]=mark
print(reg)

name=input("Enter the name you want to search in dictionary of student's marks: ").lower()

if name in reg:
    print(f"{name} is present in dictionary")
else:
    print(f"{name} is NOT present in dictionary")
time.sleep(3)



#Task2 Demonstrate List Slicing

l=[1,2,3,4,5,6,7,8,9,10]
l1=l[:5]
l2=l1[::-1]
print(f"Original list is {l}")
print(f"Extracted first five elements are {l1}")
print(f"Reversed extracted elements are {l2}")