class NotEnoughValuesToUnpack(Exception):
    pass


class DictAreEmpty(Exception):
    pass


class ContactIsNotExists(Exception):
    pass


class NotEnoughName(Exception):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotEnoughName:
            return "Give me name please."
        except NotEnoughValuesToUnpack:
            return "Give me name and phone please."
        except ContactIsNotExists:
            return 'Contact with this name not found.'
        except DictAreEmpty:
            return 'No contacts here yet.'
        except ValueError:
            return "Give me name and phone please."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise NotEnoughValuesToUnpack

    name, phone = args
    normalized_name = name.capitalize()

    if normalized_name in contacts:
        return "A contact with the same name exists. Please enter a different contact name."

    contacts[normalized_name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise NotEnoughValuesToUnpack

    name, phone = args
    if name not in contacts:
        raise ContactIsNotExists

    if name in contacts:
        contacts[name] = phone
    return "Contact changed."


@input_error
def get_phone_number(args, contacts):
    if len(args) < 1:
        raise NotEnoughName

    if len(contacts) == 0:
        raise DictAreEmpty

    name, = args

    if name not in contacts:
        raise ContactIsNotExists

    return contacts[name]


@input_error
def get_all_contacts(contacts):
    if len(contacts) == 0:
        raise DictAreEmpty

    text = ''

    for name, number in contacts.items():
        text += f'{name}: {number}\n'
    return text


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone_number(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
