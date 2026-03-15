#Banking account system
class Bank:
    def __init__(self,visa_number,Password,balance1,balance2):
        self.visa_number=visa_number
        self.password=Password
        self.balance1=balance1
        self.balance2=balance2

    def get_status(self):
        if self.balance1>self.balance2:
            print("You are in a state of finantial LOSS ")
        elif self.balance1==self.balance2:
            print("You are at EQUILIBRIUM state")
        else:
            print("You are in a state of finantial GAIN")

    def contact_us(self):
        print("PHONE: 01267290894\n")
        print("EMAIL: banque104@gmail.com\n")
        print("OR visit one of our branches:\nBranch 1: Elharam street Giza govertate\nBranch 2: Elmokatam Cairo governate\nBranch 3: Khaled Ibn Elwalid street Alexandria governate\n")
        print("OR visit WWW.banque104.com\n")
    
    
    def show_info(self):
        print("\n--- Bank account Info ---")
        print("Visa number: ",self.visa_number)
        print("Old balance: ",self.balance1)
        print("latest balance: ",self.balance2)
        print("Status",self.get_status())
        print("Contact us",self.contact_us())
        print("---------------------")

        
clients=[]

def transactions():
    visa_no=input("Enter visa number: ")
    ba1=float(input("Enter old balance"))
    ba2=float(input("Enter new balance "))
    trans=ba1-ba2
    print("Transacted money= ",trans)


def add_client():
    print("\nAdd New client")
    visa_no = input("Enter client visa_number: ")
    b1 = float(input("Enter balance 1: "))
    b2 = float(input("Enter balance 2: "))
    password=int(input("Enter password "))
    client = Bank(visa_no,password, b1, b2)
    clients.append(client)

    print(f"\nclient {visa_no} added successfully!")



def show_all_clients():
    if len(clients) == 0:
        print("\nNo clients found.")
    else:
        print("\n=== All clients ===")
        for cli in clients:
             cli.show_info()



def find_client():
    visa_number = input("\nEnter client visa number to search: ")

    found = False
    for cli in clients:
        if cli.visa_number == visa_number:
            cli.show_info()
            found = True
            break

def contact_us():
    visa_number = input("\nEnter client visa number to search: ")

    found = False
    for cli in clients:
        if cli.visa_number == visa_number:
            cli.contact_us()
            found = True
            break

def get_status():
    visa_number = input("\nEnter client visa number to search: ")

    found = False
    for cli in clients:
        if cli.visa_number == visa_number:
            cli.get_status()
            found = True
            break

    if not found:
        print(f"\nStudent '{visa_number}' not found.")

def delete_client():
    visa_number = input("\nEnter visa number to delete: ")

    for cli in clients:
        if cli.visa_number == visa_number:
            clients.remove(cli)
            print(f"\nStudent '{visa_number}' deleted successfully!")
            return

    print(f"\nStudent '{visa_number}' not found.")



def main():
    while True:
        print("\n===== Banking account System =====")
        print("1. Add client")
        print("2. Show All clients")
        print("3. Search client")
        print("4. Delete client")
        print("5. get status")
        print("6. contact us")
        print("7. Show transacted money")
        print("8. EXIT ")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_client()

        elif choice == "2":
            show_all_clients()

        elif choice == "3":
            find_client()

        elif choice == "4":
            delete_client()

        elif choice == "5":
            get_status()
            
        elif choice == "6":
            contact_us()
             
        elif choice==  "7":
            transactions()
        
        elif choice == "8":
            print("\nExiting... Goodbye!")
            break
        else:
            print("\nInvalid choice. Try again.")

main()











