def reverse_text(text):
    return text[::-1]

def to_uppercase(text):
    return text.upper()

def to_lowercase(text):
    return text.lower()

def replace_text(text, old, new):
    return text.replace(old, new)

def main():
    print("Text Modifier Tool")
    print("1. Reverse Text")
    print("2. Uppercase")
    print("3. Lowercase")
    print("4. Replace Text")
    
    choice = input("Choose an option: ")
    text = input("Enter your text: ")
    
    if choice == "1":
        print("Reversed:", reverse_text(text))
    elif choice == "2":
        print("Uppercase:", to_uppercase(text))
    elif choice == "3":
        print("Lowercase:", to_lowercase(text))
    elif choice == "4":
        old = input("Enter text to replace: ")
        new = input("Enter new text: ")
        print("Modified: ", replace_text(text, old, new))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
