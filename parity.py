def main():
    x=int(input("Enter number: "))
    if(is_even(x)):
        print("x is even.")
    else:
        print("x is odd.")



def is_even(x):
    return x%2==0
    
main()