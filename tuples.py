
def main():
    student=get_student()
    print(f"{student[0]} is {student[1]} years old!")

def get_student():
    name=input("Name: ")
    age=int(input("Age: "))
    return (name,age)

if __name__=="__main__":
    main()