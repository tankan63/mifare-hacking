import os


def main():
    file_num = 0
    while True:
        # Read input from user
        print("-" * 25)
        user_input = input("What would you like to do with your MiFare card? : ")
        print("-" * 25)

        if user_input.lower() == "help":
            print("Commands: \n"
                  "1. info - Get some details about your card\n"
                  "2. read - Read the data from your card\n"
                  "3. crack - Retrieve the keys from your card\n"
                  "4. help - Show this help message\n"
                  "5. exit - Exit the program\n")
        elif user_input == "info":
            # Run nfc-poll to get the card details and print the output
            os.system("nfc-poll -v ")
        elif user_input == "exit":
            break
        elif user_input == "crack":
            c_choice = input("Do you have a premade key to try? (y/n): ")
            if c_choice.lower() == "y":
                spec_key = input("Enter the key: (format: 12 letter hex")
                os.system(f"mfoc -k {spec_key} -O {file_num}.mfd")
            else:
                os.system(f"mfoc -O {file_num}.mfd")
            file_num += 1
        else:
            print("Invalid command! Refer to the list below for your options:\n")
            print("Commands: \n"
                  "1. info - Get some details about your card\n"
                  "2. read - Read the data from your card\n"
                  "3. crack - Unlock the data from the sectors on your card\n"
                  "4. help - Show this help message\n"
                  "5. exit - Exit the program\n")


if __name__ == "__main__":
    main()
