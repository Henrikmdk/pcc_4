#4-1 looping through a list of pizzas
count = 1
pizzas = ["Meat lover", "Bianca", "Milan", "Quattro stagione", "Havaii", "Pronto"]
print("Our Pizzas")
for pizza in pizzas:
    print(f"No {count} {pizza}")
    count += 1
print("Happy hour every wednesday 3-4am\n")

#4-2 looping through a list of animals
dwelling_fish =["Fjæsing", "Tunge", "Tobis"]
descriptions = [" - Har giftpigge på rygfinne og gællelåg. Den er forøvrigt yderst velsmagende som spisefisk",
                " - En meget velsmagende fladfisk med stor nytteværdi pga et lille hoved. Den giver relativt "
                "store filetter", " - Brugt af lystfiskere som agnfisk og af fiskeindustrien til olie og dyrefodder",
                "Disse tre fisk findes nedgravet i sandet om dagen og kan være svære at se. Om natten svømmer de i "
                "den fri vandsøjle!\n"]
for fish in dwelling_fish:
    if fish == "Fjæsing":
        print(fish + descriptions[0])
    elif fish == "Tunge":
        print(fish + descriptions[1])
    elif fish == "Tobis":
        print(fish + descriptions[2])
print(descriptions[3])

#4-3 counting to twenty using a range list and for-loop
numbers = list(range(1, 21))
for number in numbers:
    print(number)
print("\n")

'''4-4 one million
more_numbers = list(range(1, 1_000_001))
for number in more_numbers:
    print(number)
print("\n")'''

#4-5 one million worked on
even_more_numbers = list(range(1, 1_000_001))
print(min(even_more_numbers))
print(max(even_more_numbers))
print(sum(even_more_numbers)/1_000_000)
print("\n")

#4-6 odd numbers
odd_numbers = list(range(1,21,2))
for odds in odd_numbers:
    print(odds)
print("\n")
#4-7 threes, list of multiples from 3 to 30
threes_numbers = list(range(3, 31, 3))
for threes in threes_numbers:
    print(threes)
print("\n")

#4-8 cubes
cubes =[]
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)
    print(cube)
print("\n")

#4-9 cubes with comprehension
cubes_comp = [value**3 for value in range(1, 11)]
for cube in cubes_comp:
    print(cube)
print("\n")

#4-10 slices
#using existing list from 4-1
print(f"The first three items in the list 'pizzas' are: {pizzas[:3]}")
middle = len(pizzas)//2
print(f"three items from the middle of 'pizzas' {pizzas[middle-1:middle+2]}")
print(f"three items from the end of the list 'pizzas' {pizzas[-3:]}")
print("\n")

#4-11 my pizzas, your pizzas
#creating a copy of pizzas
friend_pizzas = pizzas[:]
#adding to the origin
pizzas.append("Godfather of pizzas")
#adding to friend_pizzas
friend_pizzas.append("Vegan savior")

print("Here's my pizza origin:")
for pizza in pizzas:
    print(pizza)
print("\n")
print("Here's my friends who tried to copy me")
for pizza in friend_pizzas:
    print(pizza)
print("\n")

#4-12 more loops
#I believe i added the for-loops correctly in the first place?!

#4-13 tuple buffet
buffet = ("Oksetyndsteg med fuglegræs, syltede skalotter og timianstøv", "Rødvinssauce med madargaskarpeber",
          "Honningglasserede gulerødder med salvie", "ovnstegte kartofler vendt i mos og olivenolie",
          "Bagte tomater, semidried, thai basilikum og emmenthaler")
print("Buffet:")
for element in buffet:
    print(element)
print("\n")

#menu change
buffet = ("Sprængt kalkun cuvette, syltede skalotter og grillet citron", "Skysauce med madargaskarpeber",
          "Honningglasserede gulerødder med salvie", "ovnstegte kartofler vendt i mos og olivenolie",
          "Bagte tomater, semidried, thai basilikum og emmenthaler")
print("Buffet:")
for element in buffet:
    print(element)
print("\n")