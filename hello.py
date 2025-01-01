name=input("What's your name?\n").strip()
print("Hello, "+name+"!")
print(f"Hello, {name}!")    # f-string or format string


print("Hello,",end=' ')
print(name)

print("Hello, \"friend\" ",name,"!",sep="")

# This is a comment

"""This is a multiline comment
It can extend over multiple lines!"""

firstname=name.split(" ")[0]
lastname=name.split(" ")[0]

print(f"Hello, {firstname}")