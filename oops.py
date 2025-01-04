class Student:
    def __init__(self,name,house,patronus):
        self.name=name
        self.house=house
        self.patronus=patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def get_patronus(self):
        print(f"Patronus: {self.patronus}")

    @property
    def house(self):
        return self._house
        
    @house.setter
    def house(self,house):
        if house not in ["Gryffindor","Ravenclaw","Huffelpuff","Slytherin"]:
            raise ValueError("Invalid house")
        self._house=house

    @classmethod
    def get(cls):
        name=input("Name: ")
        house=input("House: ")
        patronus=input("Patronus: ")
        return cls(name,house,patronus)
    
def main():
    student=Student.get()
    print(student)
    student.get_patronus()

if __name__=="__main__":
    main()