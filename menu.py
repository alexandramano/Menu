menu_dict = { }

while True:
    dish = raw_input("Enter meal:")
    price = raw_input("Enter price:")
    menu_dict[dish] = price

    new = raw_input("Would you like to enter new dish? (yes/no) ")

    if new == "no":
        break

print "All dishes: %s" % menu_dict

with open("menu.txt", "w+") as menu_file:  # open the TXT file (or create a new one)
    print "Dishes & Price:"
    menu_file.write("Dishes & Price:\n")  # write into the TXT file
    for dish, price in menu_dict.iteritems():
            print dish, price
            menu_file.write(dish + " " + price + "\n")  # add task into the TXT file
    menu_file.write("\n")

print "END"

