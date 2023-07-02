MyDict = {
    "Shubham" : "A Coder",
    "Fast" : "Time is very quick",
    "Marks":  [9,6,5,4],
    "Anotherdict" : {'Harry':'player'},
    1:2
}

# Dictionary Methods

# print(type(MyDict.keys())) -->prints the keys of the dictionary

# print(list(MyDict.values()))  --> print the values of the dictionary

# print(MyDict.items()) --> print the (key,value) for all contents of the dictionary

# UpdateDict = {
#     "Friends" : "Lovish"
# }
# MyDict.update(UpdateDict)
# print(MyDict)
# print(MyDict.get()("Shubham2")) --> prints  value associated with key "Shubham"

# print(MyDict["Shubham2"])  --> prints  value associated with key "Shubham"

# the difference between.get and [] syntax in dictionaries

# print(MyDict.get()("Shubham2")) --> Returns none as Shubham2 is not present in the dictionary

# print(MyDict["Shubham2"])  --> Throws an error as Shubham2 is not present in the dictionary