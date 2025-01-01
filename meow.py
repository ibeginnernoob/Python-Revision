def main():
    number=get_number()
    meow(number)
    

def get_number():
    x=0
    while True:
        x=int(input("Enter number: "))
        if(x>=0):
            return x

def meow(x):
    for _ in range(x):
        print("meow")
    
main()