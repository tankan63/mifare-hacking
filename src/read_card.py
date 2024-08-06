import os


def main():
    file_num = 0
    while True:
        # Read input from user
        print("-" * 25)
        user_input = input("What would you like to do with your MiFare card? : ").strip().lower()
        print("-" * 25)

        if user_input == "help":
            print("Commands: \n"
                  "1. info - Get some details about your card\n"
                  "2. read - Read the data from your card\n"
                  "3. crack - Retrieve the keys from your card\n"
                  "4. dump -  Get all the data on the card in hex format\n"
                  "5. help - Show this help message\n"
                  "6. exit - Exit the program\n")
        elif user_input == "info":
            # Run nfc-poll to get the card details and print the output
            os.system("nfc-poll -v ")
        elif user_input == "exit":
            break
        elif user_input == "dump":
            c_choice = input("Do you have a premade key to try? (y/n): ")
            if c_choice.lower() == "y":
                spec_key = input("Enter the key: (format: 12 letter hex")
                os.system(f"mfoc -k {spec_key} -O {file_num}.mfd")
            else:
                os.system(f"mfoc -O {file_num}.mfd")
            file_num += 1
        elif user_input == "crack":
            os.system("mfcuk -C -R 0 -v 2")
        elif user_input == "read":
            # Check if a file with .mfd extension exists
            if not os.path.isfile("0.mfd"):
                c_check = input("No recent data file found! Would you like to dump an example card? (y/n): ")
                if c_check.lower() == "y":
                    os.system("hexdump -C example.mfd")
            else:
                os.system(f"hexdump -C {file_num - 1}.mfd")
        else:
            print("Invalid command! Refer to the list below for your options:\n")
            print("Commands: \n"
                  "1. info - Get some details about your card\n"
                  "2. read - Read the data from your card\n"
                  "3. crack - Retrieve the keys from your card\n"
                  "4. dump -  Get all the data on the card in hex format\n"
                  "5. help - Show this help message\n"
                  "6. exit - Exit the program\n")


if __name__ == "__main__":
    main()
