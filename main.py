

pizzas = ["Meat lover", "Bianca", "Milan", "Quattro stagione", "Havaii", "Pronto"]
dwelling_fish =["Fjæsing", "Tunge", "Tobis"]
descriptions = [" - Har giftpigge på rygfinne og gællelåg. Den er forøvrigt yderst velsmagende som spisefisk", " - En meget velsmagende fladfisk med stor nytteværdi pga et lille hoved. Den giver relativt store filetter", " - Brugt af lystfiskere som agnfisk og af fiskeindustrien til olie og dyrefodder", "Disse tre fisk findes nedgravet i sandet om dagen og kan være svære at se. Om natten svømmer de i den fri vandsøjle!\n"]


'''4-1 looping through a list of pizzas'''
count = 1
print("Our Pizzas")
for pizza in pizzas:
    print(f"No {count} {pizza}")
    count += 1
print("Happy hour every wednesday 3-4am\n")

'''4-2 looping through a list of animals'''
for fish in dwelling_fish:
    if fish == "Fjæsing":
        print(fish + descriptions[0])
    elif fish == "Tunge":
        print(fish + descriptions[1])
    elif fish == "Tobis":
        print(fish + descriptions[2])
print(descriptions[3])



