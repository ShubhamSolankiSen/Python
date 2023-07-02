'''st = "This is a string double    Spaces"
doublespaces =  st.find("  ")
print(doublespaces)'''

# Ans. will be 23

# on the other hand
'''st = " This is a string double    Spaces"
doublespaces = st.find("  ")
print(doublespaces)'''

st = " This is a string double   spaces"
st = st.replace("  ", " ")
print(st)