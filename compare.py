x=int(input("Enter number: "))
y=int(input("Enter 2nd number: "))

# and / or keywords used for multiple comparisons

# imp -> if and else don't have their own scope
# to display this behaviour -

if(True):
    z=10

print(z)  # z is accessible despite being inside the if block

if(x>y or x<y):
    print("x is not equal to y.")
else:
    print("x is equal to y.")



if(x%2==0 and y%2==0):
    print("x and y are even.")