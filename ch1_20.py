MyDict = {
    "Pankha" : "Fan",
    "Dabba" : "Box",
    "Vastu": "Item"
}
print("Options are ",MyDict.keys())

a = input("Enter the hindi word\n")
# print("The meaning of your word is :",MyDict[a])

# Below lines will not throw an error

print("The meaning of your word is :",MyDict.get(a))

