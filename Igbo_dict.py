# Dictionary Project
igbo_dict = {
    "Water": "Mmiri",
    "House": "Ulo",
    "Food": "Nri",
    "Mother": "Nne",
    "Father": "Nna",
    "Child": "Nwa",
    "Sun": "Anyanwu",
    "Rain": "Mmiri Ozuzo",
    "Road": "Uzo",
    "Book": "Akwukwo",
    "Work": "Oria",
    "Friend": "Enyi",
    "Dog": "Nkita",
    "Cat": "Pusi",
    "Fish": "Azụ",
    "Town": "Obodo",
    "Forest": "Ohia",
    "Cloth": "Uwe",
    "Morning": "Ututu",
    "Car": "Ugboala"
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
    print("=== IGBO LANGUAGE DICTIONARY ===")
    print("1. Igbo Dictionary")
    print("2. Exit")

    option = input("Choose a dictionary (1-2): ")

    if  option == "1":
        show_dictionary(igbo_dict)
    elif option == "2":
        print("Thank you for using the dictionary.")
        break
    else:
        print("Invalid choice. Try again.")