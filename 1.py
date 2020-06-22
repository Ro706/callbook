def print_numbers(numbers):
    print "Telephone Numbers:"
    for x in numbers.keys():
        print "Name:", x, "\tNumber:", numbers[x]
    print
 
def add_number(numbers, name, number):
    numbers[name] = number
 
def lookup_number(numbers, name):
    if name in numbers:
        return "The number is " + numbers[name]
    else:
        return name + " was not found"
 
def remove_number(numbers, name):
    if name in numbers:
        del numbers[name]
    else:
        print name," was not found"
 
def load_numbers(numbers, filename):
    in_file = open(filename, "r")
    while True:
        in_line = in_file.readline()
        if not in_line:
            break
        in_line = in_line[:-1]
        name, number = in_line.split(",")
        numbers[name] = number
    in_file.close()
 
def save_numbers(numbers, filename):
    out_file = open(filename, "w")
    for x in numbers.keys():
        out_file.write(x + "," + numbers[x] + "\n")
    out_file.close()
 
def print_menu():
    print '1. Print Phone Numbers'
    print '2. Add a Phone Number'
    print '3. Remove a Phone Number'
    print '4. Lookup a Phone Number'
    print '5. Load numbers'
    print '6. Save numbers'
    print '7. Quit'
    print
 
phone_list = {}
menu_choice = 0
print_menu()
while True:
    menu_choice = input("Type in a number (1-7): ")
    if menu_choice == 1:
        print_numbers(phone_list)
    elif menu_choice == 2:
        print "Add Name and Number"
        name = raw_input("Name: ")
        phone = raw_input("Number: ")
        add_number(phone_list, name, phone)
    elif menu_choice == 3:
        print "Remove Name and Number"
        name = raw_input("Name: ")
        remove_number(phone_list, name)
    elif menu_choice == 4:
        print "Lookup Number"
        name = raw_input("Name: ")
        print lookup_number(phone_list, name)
    elif menu_choice == 5:
        filename = raw_input("Filename to load: ")
        load_numbers(phone_list, filename)
    elif menu_choice == 6:
        filename = raw_input("Filename to save: ")
        save_numbers(phone_list, filename)
    elif menu_choice == 7:
        break
    else:
        print_menu()
 
print "Goodbye"
