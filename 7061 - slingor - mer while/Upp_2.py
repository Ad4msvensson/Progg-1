svar = int(input("Gissa på ett tal: "))
antal_gissningar = 0

while antal_gissningar < 5:
    if svar > 42:
        print("För stort. ")
        svar = int(input("Gissa igen: "))

    if svar < 42:
        print("För litet")
        svar = int(input("Gissa igen: "))
    antal_gissningar = antal_gissningar + 1
print("Du behövde: ", antal_gissningar)





