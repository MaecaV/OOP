class Phone:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    def update_brand(self, new_brand):
        self.brand = new_brand

    def update_model(self, new_model):
        self.model = new_model

    def update_year(self, new_year):
        self.year = new_year

    def delete_brand(self):
        del self.brand

    def delete_model(self):
        del self.model

    def delete_year(self):
        del self.year


def display_menu():
    print("\nPhone Management System")
    print("1. Create Phone")
    print("2. Modify Phone")
    print("3. Delete Phone")
    print("4. List Phones")
    print("5. Exit")


def create_phone(phone_list):
    brand = input("Enter phone brand: ")
    model = input("Enter phone model: ")
    year = input("Enter phone year: ")
    phone = Phone(brand, model, year)
    phone_list.append(phone)
    print("Phone created successfully!")


def modify_phone(phone_list):
    list_phones(phone_list)
    index = int(input("Enter the index of the phone to modify: ")) - 1
    if 0 <= index < len(phone_list):
        phone = phone_list[index]
        print("1. Update Brand")
        print("2. Update Model")
        print("3. Update Year")
        choice = int(input("Choose an option: "))
        if choice == 1:
            new_brand = input("Enter new brand: ")
            phone.update_brand(new_brand)
        elif choice == 2:
            new_model = input("Enter new model: ")
            phone.update_model(new_model)
        elif choice == 3:
            new_year = input("Enter new year: ")
            phone.update_year(new_year)
        else:
            print("Invalid choice.")
        print("Phone updated successfully!")
    else:
        print("Invalid index.")


def delete_phone(phone_list):
    list_phones(phone_list)
    index = int(input("Enter the index of the phone to delete: ")) - 1
    if 0 <= index < len(phone_list):
        del phone_list[index]
        print("Phone deleted successfully!")
    else:
        print("Invalid index.")


def list_phones(phone_list):
    if phone_list:
        index = 1
        for phone in phone_list:
            print(f"{index}. {phone}")
            index += 1
    else:
        print("No phones available.")


def main():
    phone_list = []
    while True:
        display_menu()
        choice = int(input("Choose an option: "))
        if choice == 1:
            create_phone(phone_list)
        elif choice == 2:
            modify_phone(phone_list)
        elif choice == 3:
            delete_phone(phone_list)
        elif choice == 4:
            list_phones(phone_list)
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
