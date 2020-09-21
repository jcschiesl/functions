KPM = 1.609344 #Kilometers per mile
GPL = 0.2641720524 # Galons per liter

def mpg2kpl(mpg):



    return mpg * KPM * GPL

mpg = input("What is the MPG?")

mpg = float(mpg)

print(round(mpg2kpl(mpg),2),"KPL")
