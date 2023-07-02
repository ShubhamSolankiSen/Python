# problem no. 1

# name = input("Enter your name\n")

# print("Good Afternoon , "+ name)

# problem no.2

letter = ''' Dear <|Name|>,
Greetings from ABC coding house . I'm happy to tell you about your selection 
                   You are selected !
                   have a great day ahead!
                   Thanks and regards ,
                   Bill
                  Date: <|Date|>'''
name = input("Enter your name\n")
date = input("Enter date\n")
letter = letter.replace("<|Name|>", name)
letter =  letter.replace("<|Date|>", date)
print(letter)