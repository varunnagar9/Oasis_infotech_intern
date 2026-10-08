
import random
import string


def get_password_length():
    """Prompts for and validates password length (minimum 8 characters)."""
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            if length >= 8:
                return length
            print("Error: Length must be at least 8 characters. Please try again.\n")
        except ValueError:
            print("Error: Please enter a valid whole number.\n")


def get_character_preferences():
    """
    Prompts user to select character types and ensures at least 2 are selected.
    Returns:
        character_pool (str): Combined string of all selected characters.
        selected_types (list): List of selected character pools for mandatory inclusion.
    """
    options = {
        "1": ("Uppercase letters (A-Z)", string.ascii_uppercase),
        "2": ("Lowercase letters (a-z)", string.ascii_lowercase),
        "3": ("Numbers (0-9)", string.digits),
        "4": ("Symbols (!@#$%...)", string.punctuation),
    }

    while True:
        print("\nSelect character types to include:")
        for key, (label, _) in options.items():
            print(f"  [{key}] {label}")

        choice_input = input("\nEnter choices separated by commas (e.g., 1,2,3): ")
        choices = [c.strip() for c in choice_input.split(",")]

        selected_pools = []
        for choice in set(choices):
            if choice in options:
                selected_pools.append(options[choice][1])

        # Input Validation: At least 2 character types required
        if len(selected_pools) >= 2:
            character_pool = "".join(selected_pools)
            return character_pool, selected_pools
        
        print("\nError: You must select at least 2 character types. Please try again.")


def generate_password(length, character_pool, selected_pools):
    """
    Generates a password guaranteeing at least one character from each 
    selected type to maintain strength.
    """
    password = []

    # Guarantee at least 1 character from each selected category
    for pool in selected_pools:
        password.append(random.choice(pool))

    # Fill the remainder of the length from the combined pool
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(character_pool))

    # Shuffle to prevent predictable starting characters
    random.shuffle(password)
    return "".join(password)


def main():
    print("=" * 40)
    print("   RANDOM PASSWORD GENERATOR (Python)")
    print("=" * 40)

    while True:
        length = get_password_length()
        character_pool, selected_pools = get_character_preferences()

        # Generate and display password
        password = generate_password(length, character_pool, selected_pools)
        print("\n" + "-" * 40)
        print(f"Generated Password: {password}")
        print("-" * 40 + "\n")

        # Option to generate another password without restarting
        again = input("Do you want to generate another password? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThank you for using Random Password Generator. Goodbye!")
            break
        print("\n")


if __name__ == "__main__":
    main()