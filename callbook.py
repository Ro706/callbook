class PhoneBook:
  """
  A class to manage a phone book with functionalities like adding, removing,
  looking up, printing, loading, and saving phone numbers.
  """

  def __init__(self):
    """
    Initializes the phone book with an empty dictionary to store contacts.
    """
    self.contacts = {}

  def print_numbers(self):
    """
    Prints all contacts in the phone book.
    """
    print("Telephone Numbers:")
    for name, number in self.contacts.items():
      print(f"Name: {name}\tNumber: {number}")
    print()

  def add_number(self, name, number):
    """
    Adds a new contact to the phone book.
    """
    self.contacts[name] = number
    print(f"Contact for {name} added successfully!")

  def lookup_number(self, name):
    """
    Looks up a contact's phone number in the phone book.
    """
    if name in self.contacts:
      return f"The number for {name} is {self.contacts[name]}"
    else:
      return f"{name} was not found"

  def remove_number(self, name):
    """
    Removes a contact from the phone book.
    """
    if name in self.contacts:
      del self.contacts[name]
      print(f"Contact for {name} removed successfully!")
    else:
      print(f"{name} was not found")

  def load_numbers(self, filename):
    """
    Loads phone numbers from a file into the phone book.
    - Each line in the file should be in the format "name,number".
    """
    try:
      with open(filename, "r") as in_file:
        for line in in_file:
          name, number = line.strip().split(",")
          self.contacts[name] = number
      print(f"Phone numbers loaded successfully from {filename}")
    except FileNotFoundError:
      print(f"Error: File {filename} not found")

  def save_numbers(self, filename):
    """
    Saves phone numbers from the phone book to a file.
    - Each line in the file will be in the format "name,number".
    """
    try:
      with open(filename, "w") as out_file:
        for name, number in self.contacts.items():
          out_file.write(f"{name},{number}\n")
      print(f"Phone numbers saved successfully to {filename}")
    except FileNotFoundError:
      print(f"Error: Could not create or write to file {filename}")

  def print_menu(self):
    """
    Prints the menu options for interacting with the phone book.
    """
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Load numbers')
    print('6. Save numbers')
    print('7. Quit')
    print()

# Create an instance of the PhoneBook class
phone_book = PhoneBook()

# Main program loop
menu_choice = 0
phone_book.print_menu()
while True:
  menu_choice = input("Type in a number (1-7): ")

  try:
    menu_choice = int(menu_choice)
  except ValueError:
    print("Invalid input. Please enter a number (1-7).")
    continue

  if menu_choice == 1:
    phone_book.print_numbers()
  elif menu_choice == 2:
    print("Add Name and Number")
    name = input("Name: ")
    number = input("Number: ")
    phone_book.add_number(name, number)
  elif menu_choice == 3:
    print("Remove Name and Number")
    name = input("Name: ")
    phone_book.remove_number(name)
  elif menu_choice == 4:
    print("Lookup Number")
    name = input("Name: ")
    print(phone_book.lookup_number(name))
  elif menu_choice == 5:
    filename = input("Filename to load: ")
    phone_book.load_numbers(filename)
  elif menu_choice == 6
