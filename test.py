svar = "ja"

svar = input("Ja/nej: ")

while svar == "ja":
    print("Du är bäst")
    svar = input("Vill du höra igen? ")

if svar == "nej":
    print("Hej då")