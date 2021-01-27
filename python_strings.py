#Python Stings

#Python is loosly typed -- data types

# String variableName -- Java C++ Swift Most OBJ Oriented Languages
# String variableName = "This is a string"
# Int variableInt = 34

# Python
# variableName = "This is a string" ---> String
# variableName = 3 --> Int
# variableInt = 34 --> Integer


# Python is scripting language
# -- Python can run on anything that allows the interpreter to be installed
# -- Does not require compile
# -- You won't know failure of the code until you run it.
# -- Slower to run through the interpreter

# String is a list of characters
#       Character [a-z,A-Z]
#       Number [0-9]
#       Special Character [@#$%]
#       Space [" "]
#       Escape Character [\n --> newline, \t --tab, \\]

school = 'WEBER STATE'

print ('first character is:', school[0]) #0 is the first character
print ('second character is:', school[1])

print ('last character is:', school[-1])
print ('second to last character is:', school[-2])

first_name = 'Jayden' #-- String data type
last_name = 'Owings' #-- String data type

initials = 'Initials:', first_name[0], last_name[0]

first_initial = first_name[0]
last_initial = last_name[0]

print (initials)
print ('Inititals:', first_initial, last_initial)
print ('Inititals:', first_initial + last_initial)


first_first_three = first_name[0:3] #Includes first number, not the last number
last_first_two = last_name[:2] #if you start at begining or end, you can leave that side of the colon blank
print(first_first_three)

Capital_name = first_name.upper()

print(Capital_name)




