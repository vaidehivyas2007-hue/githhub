# Interactive personal Data collector
print("welcome to the interactive personal data collector!")


# input data
name = input("please enter your name:")
age = int(input("please enter your age:"))
height = float(input("please enter your height in cm:"))
favourite_number= int(input("please enter your favourite_number:"))

# display collected data
print("\nthank you! here is the data we collected:\n")
print("name:",name)
print("type:", type(name), "id:",id(name))
print("age:",age)
print("type:",type(age),"id",id(name))
print("height:",height)
print("type:",type(height),"id:",id(name))
print("favourite number:", favourite_number)
print("type:", type(favourite_number),"id:",id( favourite_number))


# birth year calcilation
current_year = 2025
birth_year = current_year - age

print("\nyour birth year is approximately:",birth_year)


# user- friendly summary
print("\n--------USER SUMMARY---------")
print("hello",name)
print("you are", age,"years old.")
print("your height is",height,"cm.")
print("your favourite numbers is ",fav_number)
print("your estimated birth place year is",birth_year)
print("---------")



#exit message
print("\nthank you for using the personal data collector!")


      



      


               

               
               
