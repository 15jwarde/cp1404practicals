COLOUR_TO_HEX = {"Chrome Yellow": "#ffa700", "Bittersweet Shimmer": "#bf4f51", "Bright Cerulean": "#1dacd6",
                 "Deep Fuchsia": "#c154c1", "Cherry Blossom Pink": "#ffb7c5", "Oxford Blue": "#002147",
                 "Metallic Seaweed": "#0a7e8c", "Bright Lavender": "#bf94e4", "Byzantium": "#702963",
                 "Sap Green": "#507d2a"}

print(COLOUR_TO_HEX)

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_HEX[colour_name])
    except KeyError:
        print("Invalid colour")
    colour_name = input("Enter colour name: ").title()

for colour, hex in COLOUR_TO_HEX.items():
    print(f"{colour:<3} is {hex}")
