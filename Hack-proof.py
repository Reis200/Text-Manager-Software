from random import randint

class Program:
    def __init__(self):
        self.run()


    def open_text_file(self):
        try:
            with open("text document.txt","x") as file:
                print("The file is created...")
                print("There is no current content to access")
        except:
            with open("text document.txt","r") as file:
                for line in file:
                    print(line)

    def modify_text_file(self):
        user_input_mode = input("Select a mode (a= append, w=write over original):")
        if user_input_mode in ("a","A"):
            with open("text document.txt","a") as file:
                user_entry_to_append = input("Type information to append; include '\n' for new lines: ")
                user_entry_to_append = user_entry_to_append + '\n'
                file.write(user_entry_to_append)
        elif user_input_mode in ("w","W"):
            with open("text document.txt","w") as file:
                user_entry_to_append = input(f"Type information to append; include \ followed by n for new lines: ")
                user_entry_to_append = user_entry_to_append + '\n'
                file.write(user_entry_to_append)

    def open_password_file(self):
        try:
            with open("password.txt","x") as file:
                print("There is no current set password")
                user_input = input("Please enter a password to set for file access: ")
                file.write(user_input)
                self.file_password = user_input
                return True
        except: 
            with open("password.txt","r") as file:
                password_entry = input("Enter in the password to access the text file: ")
                password = str(file.read())
                if password_entry == password:
                    return True
                else:
                    return False


    def run(self):
        if self.open_password_file():
            self.open_text_file()

            while True:
                
                modify_file = input("Do you want to modify the file (type y/yes/ok): ")
                if modify_file in ("y","yes","ok","yeah", "yea", "y"):
                    self.modify_text_file()

                self.open_text_file()

        
            
        
Program = Program()
