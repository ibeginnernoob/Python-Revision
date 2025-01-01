def main():
    name=input("Enter name: ")
    hello(name)

def hello(name="World"):
    print(f"Hello, {name}!")

main()