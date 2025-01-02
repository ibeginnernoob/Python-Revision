
# try and exception blocks don't have their own scope, just like if/else statements

# try -> else or exception

while(True):
    try:
        x=int(input("Enter number: "))
    except ValueError:
        print("x is not a integer.")
        continue
    else:
        break

print("x is",x)