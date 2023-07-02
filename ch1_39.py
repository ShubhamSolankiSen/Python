# Write a program to print the following star pattern

# step no.1
n = 3

# for i in range(3):
#          print("*" * (i+1))

        #  step no.2

n = 3
for i in range(3):
        print("  " * (n-i-1),end="")
        print(" * " * (2*i+1),end="")
        print(" " * (n-i-1))