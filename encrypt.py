

# Constants
ENCRYPTION_SOURCE = r"7elL2GJVkrv0dQ%Eb?N6uw*#t!@hYAop&O^a3FWCyKUT4PR5zBjDH8XgZnf9qMm1cSIsi$x "
SPECIAL_CHARACTERS = "!@#$%^&*?"
VALID_CHARACTERS = ENCRYPTION_SOURCE
SAVED_PASSWORDS_FILE = "saved_passwords.txt"

# Utility Functions
def validate_password(password):
    """Validates the password based on given criteria."""
    issues = []
    invalid_chars = [ch for ch in password if ch not in VALID_CHARACTERS]
    if len(password) < 8:
        issues.append("Password should be at least 8 characters")
    if " " in password:
        issues.append("Password cannot have spaces")
    if not any(ch.islower() for ch in password):
        issues.append("Missing a lowercase letter in the password")
    if not any(ch.isupper() for ch in password):
        issues.append("Missing an uppercase letter in the password")
    if not any(ch.isdigit() for ch in password):
        issues.append("Missing a digit in the password")
    if not any(ch in SPECIAL_CHARACTERS for ch in password):
        issues.append("Missing a special character in the password")
    if invalid_chars:
        issues.append(f"{', '.join(invalid_chars)} are not allowed in the password")
    return issues

def shift_text(text, shift):
    """Encrypts or decrypts text using a Caesar cipher based on ENCRYPTION_SOURCE."""
    shifted_text = ""
    source_length = len(ENCRYPTION_SOURCE)
    for char in text:
        if char in ENCRYPTION_SOURCE:
            old_index = ENCRYPTION_SOURCE.index(char)
            new_index = (old_index - shift) % source_length
            shifted_text += ENCRYPTION_SOURCE[new_index]
        else:
            shifted_text += char
    return shifted_text

def save_passwords(shift_key, passwords):
    """Saves the encrypted passwords to a file."""
    with open(SAVED_PASSWORDS_FILE, "w") as file:
        file.write(f"{shift_key}\n")
        for website, encrypted_password in passwords:
            file.write(f"{website}\n{encrypted_password}\n")

# Main Program
def main():
    shift_key = int(input("Enter the Encryption key: "))
    passwords = []

    while True:
        website = input("\nEnter website: ").strip().lower()
        
        while True:
            password = input("Enter password: ")
            issues = validate_password(password)
            if issues:
                print("\nIssues:")
                for issue in issues:
                    print(f"\t{issue}")
                print("\nPlease enter a strong valid password")
            else:
                break

        encrypted_website = shift_text(website, shift_key)
        encrypted_password = shift_text(password, shift_key)
        passwords.append((encrypted_website, encrypted_password))
        print(f"\nPassword for {website} has been encrypted and stored successfully")

        another = input("Add another password? (y/n): ").strip().lower()
        if another != 'y':
            break

    save_passwords(shift_key, passwords)
    print("\nGoodbye!")

if __name__ == "__main__":
    main()
