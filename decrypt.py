

# Constants
ENCRYPTION_SOURCE = r"7elL2GJVkrv0dQ%Eb?N6uw*#t!@hYAop&O^a3FWCyKUT4PR5zBjDH8XgZnf9qMm1cSIsi$x "

# Utility Functions
def shift_text(text, shift):
    """Decrypts text using a Caesar cipher based on ENCRYPTION_SOURCE."""
    shifted_text = ""
    source_length = len(ENCRYPTION_SOURCE)
    for char in text:
        if char in ENCRYPTION_SOURCE:
            old_index = ENCRYPTION_SOURCE.index(char)
            new_index = (old_index + shift) % source_length
            shifted_text += ENCRYPTION_SOURCE[new_index]
        else:
            shifted_text += char
    return shifted_text

def load_and_decrypt_file(file_name):
    """Loads the encrypted file and decrypts its contents."""
    with open(file_name, "r") as file:
        lines = file.readlines()

    shift_key = int(lines[0].strip())
    data = lines[1:]

    decrypted_data = {}
    for i in range(0, len(data), 2):
        website = shift_text(data[i].strip(), shift_key)
        password = shift_text(data[i + 1].strip(), shift_key)
        decrypted_data[website] = password

    return decrypted_data

def main():
    file_name = input("Enter filename: ").strip()

    
    decrypted_data = load_and_decrypt_file(file_name)

    while True:
        website = input("\nEnter a website: ").strip().lower()
        if website in decrypted_data:
            print(f"Password for {website} is '{decrypted_data[website]}'")
        else:
            print("The website doesn’t exist. Please try again.")

        another = input("Get another password? (y/n): ").strip().lower()
        if another != 'y':
            break

    print("\nGoodbye!")

if __name__ == "__main__":
    main()
