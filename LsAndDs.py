list1=list()   # initialize a new list

dict1={
    "name":"Adheil",
    "age":19
}

for field in dict1:
    print(field+":",dict1[field])

students=[
    {
        "name":"Adheil",
        "age":19,
        "can_drive":True
    },
    {
        "name":"Ahana",
        "age":13,
        "can_drive":False
    }
]

for i in range(len(students)):
    print(i, "name:" , students[i]["name"], "age:" , students[i]["age"], "can drive:" , students[i]["can_drive"])