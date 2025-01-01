i=3
while(i!=0):
    print("meow")
    i-=1

print("\n")

for i in [0,1,2]:
    print("meow")

print("\n")

for _ in range(3):  # range(3) -> 0,1,2
    print("meow")

x=int(input("Enter number: "))

# while(x<0):
#     x=int(input("Enter number: "))

#               or

while True:
        if(x>=0):
            break
        else:
            x=int(input("Enter number: "))

for _ in range(x):
    print("meow")