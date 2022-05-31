# 1 kilometer is = 0.621371 mile
# 1 mile is = 1.609344 kilometre
# convert mile to kilometre
# convert kilometre to mile

try:
    mile = int(input("Mile :- "))
    convert = 1.609344
    to_kilometer = mile * convert
    print(f"{mile} mile is equal {to_kilometer} kilometer!")
except:
    print("You must be enterd a integer number!")

# try:
#     kilometer = int(input("Kilometer :- "))
#     convert = 0.621371
#     to_mile = kilometer * convert
#     print(f"{kilometer} kilometer is equal {to_mile} mile!")
# except:
#     print("You must be enterd a integer number!")