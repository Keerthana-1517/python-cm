def get_person_details():
  """
  function to read a person's details from the keyboard
  """
  name=input("enter your name:")
  address=input("enter your addresss:")
  email=input("enter your email:")
  phone=input("enter your phone number:")
  return name,address,email,phone
def print_person_details(name,address,email,phone):
  """
  function to print a person's details.
  """
  print("\n---personal details---")
  print(f"name:{name}")
  print(f"address:{address}")
  print(f"email:{email}")
  print(f"phone number:{phone}")
#Get details from the user
name,address,email,phone = get_person_details()
#print the details
print_person_details(name,address,email,phone)


