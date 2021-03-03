'''
Task -----------------condition------------------------------
Weight converter:
  Input the weight of a perosn in either kg or lbs. If the person provides his/her
  weight in kg then convert it into lbs
  else convert it to kg.
'''

weight = int(input("Enter the weight of the person : "))

unit = input("(L)bs or (K)g : ")

if unit.upper() == "L":
    converted_lbs = weight * 0.45
    print(f"The person weight is {converted_lbs} kilos")
else:
    converted_kg = weight / 0.45
    print(f"The person weight is {converted_kg} pounds")


'''
 ------------------Condition---------------------
'''

