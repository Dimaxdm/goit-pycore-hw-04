MIN_DIGITS_IN_PHONE_NUMBER: int = 10
MESSAGE_INVALID_PHONE_NUMBER: str = f"|ERROR|: Phone must contain only digits (min. {MIN_DIGITS_IN_PHONE_NUMBER} digits)"

# Ensure user phone number contains 10 or more digits 
def is_valid_phone_number(phone: str) -> bool:
    return phone.isdigit() and len(phone) >= MIN_DIGITS_IN_PHONE_NUMBER


def parse_input(user_input: str) -> tuple[str | None, list[str]]:
    # Handle case where no values are provided by user
    try:
        command, *args = user_input.split()
        return command.strip().lower(), *args
    except ValueError:
        return None, []


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        return "|ERROR|: Invalid format. |USE|: \"add [Name] [Phone number]\"."
    
    user_name, user_phone_number = args[0].strip(), args[1].strip()
 
    if user_name in contacts:
        return f"|ERROR|: Contact \"{user_name}\" already exists. |USE|:  \"change [Name] [Phone number]\" to update."
    
    if not is_valid_phone_number(user_phone_number):
        return MESSAGE_INVALID_PHONE_NUMBER
    
    contacts[user_name] = user_phone_number
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str: 
    if len(args) != 2:
        return "|ERROR|: Invalit format. |USE|: \"change [Name] [Phone number]\"."
    
    user_name, user_phone_number = args[0].strip(), args[1].strip()

    if not user_name in contacts:
        return f"|ERROR|: Contact \"{user_name}\" not found."
    
    if not is_valid_phone_number(user_phone_number):
        return MESSAGE_INVALID_PHONE_NUMBER
    
    contacts[user_name] = user_phone_number
    return "Contact updated."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 1:
        return "|ERROR|: Invalid format. |USE|: \"phone [Name]\"."
    
    user_name : str = args[0].strip()

    if user_name in contacts:
        return contacts[user_name]
    return f"|ERROR|: Contact \"{user_name}\" not found."


def show_all(contacts: dict[str, str]) -> dict[str, str]:
    if not contacts:
        return "No contacts saved."
    
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    # dict{"user name": "phone_number"}
    contacts: dict[str, str] = {}
    print("Welcome to the assistance bot!")
    while True:
        user_input: str = input("Enter a command: ")
        command, *args = parse_input(user_input)

        # Handle empty input
        if command is None:
            continue
        
        # Exit commands
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        match command:
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "all":
                print(show_all(contacts))
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()