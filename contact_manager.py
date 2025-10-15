from colorama import init, Fore, Style

init(autoreset=True)  # Auto-reset colors after each print

def add_contact(contacts, name, phone, email):
    contacts[name] = {"phone": phone, "email": email}
    print(Fore.GREEN + f"✅ Contact {name} added successfully.")

def remove_contact(contacts, name):
    if name not in contacts:
        print(Fore.RED + f"❌ Contact '{name}' not found.")
        return
    else:
        del contacts[name]
        print(Fore.YELLOW + f"🗑️ Contact '{name}' removed.")

def display_contact(contacts):
    if len(contacts) == 0:
        print(Fore.CYAN + "📭 Contact list is empty")
    else:
        print(Fore.BLUE + "📇 List of your Contacts:")
        for index, (key, info) in enumerate(contacts.items()):
            print(
                f"{Fore.MAGENTA}{index}- {Style.BRIGHT}Name:{Style.RESET_ALL} {key}, "
                f"{Style.BRIGHT}Phone:{Style.RESET_ALL} {info['phone']}, "
                f"{Style.BRIGHT}Email:{Style.RESET_ALL} {info['email']}"
            )

def main():
    contacts = {}
    favorite_contacts = set()

    while True:
        print(Fore.CYAN + "\n📞 Contact Management Using CLI")
        print(Fore.WHITE + "1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Add to Favorites")
        print("5. Display Favorites")
        print(Fore.RED + "6. Exit" + Style.RESET_ALL)

        option = input(Fore.YELLOW + "Enter your option (1-6): " + Fore.RESET)

        if option == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(contacts, name, phone, email)
        elif option == "2":
            name = input("Enter exact name to remove (*you can check by display option): ")
            remove_contact(contacts, name)
        elif option == "3":
            display_contact(contacts)
        elif option == "4":
            name = input("Enter name to add to favorites: ")
            if name in contacts:
                favorite_contacts.add(name)
                print(Fore.LIGHTGREEN_EX + f"⭐ {name} added to favorites")
            else:
                print(Fore.RED + f"❌ Contact {name} not found")
        elif option == "5":
            if not favorite_contacts:
                print(Fore.CYAN + "📭 No favorite contacts yet.")
            else:
                print(Fore.YELLOW + "\n⭐ Favorite Contacts:")
                for name in favorite_contacts:
                    print(f"  - {name}")
        elif option == "6":
            print(Fore.GREEN + "👋 Goodbye!")
            break
        else:
            print(Fore.RED + "⚠️ Invalid option. Please try again.")

if __name__ == "__main__":
    main()