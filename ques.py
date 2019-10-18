name,char=input("Enter name and a character of that name seperated by a space: \n").split()
print(f"Length of name is {len(name)}")
print(f"count :{name.lower().count(char.lower())}")
