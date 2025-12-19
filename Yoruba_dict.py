# Dictionary Project
yoruba_dict = {
    "Water": "Omi",
    "House": "Ile",
    "Food": "Ounje",
    "Mother": "Iya",
    "Father": "Baba",
    "Child": "Omo",
    "Rain": "Ojo",
    "Sun": "Oorun",
    "Road": "Ona",
    "Cloth": "Aso",
    "Book": "Iwe",
    "Farm": "Oko",
    "Work": "Ise",
    "Friend": "Ore",
    "Dog": "Aja",
    "Cat": "Ologbo",
    "Fish": "Eja",
    "Forest": "Igbo",
    "City": "Ilu",
    "Morning": "Owuro"
}


def show_dictionary(dictionary):
    print("Available words:")
    for word in dictionary:
        print(word)

    choice = input("Enter a word to see its meaning: ")

    if choice in dictionary:
        print("Meaning:", dictionary[choice])
    else:
        print("Word not found.")

while True:
    print("=== YORUBA LANGUAGE DICTIONARY ===")
    print("1. Yoruba Dictionary")
    print("2. Exit")

    option = input("Choose a dictionary (1-2): ")

    if option == "1":
        show_dictionary(yoruba_dict)
    elif option == "2":
        print("Thank you for using the dictionary.")
        break
    else:
        print("Invalid choice. Try again.")