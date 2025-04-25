#take input from the user
char=input("enter a single character:")

#check if the input is a single character
if len(char)!=1:
   print("please enter only one character!")
else:
    #check if the character is a digit
    if char.isdigit():
       print(f"'{char}'is a digit.")
    #check if the character is a lowercase letter
    elif char.islower():
       print(f"'{char}'is a lowercase character.")
    #check if the character is an uppercase letter
    elif char.isupper():
       print(f"'{char}'is an uppercase character.")
    #if none of the above listed,it is a special character
    else: 
       print(f"'{char}'is a special character.")
                        
