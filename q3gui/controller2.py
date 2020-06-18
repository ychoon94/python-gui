from model import *


def showMenuBurger():
    print("Welcome to xyz burger chain restaurant.")
    print("Choose your burger.")
    print("1. Chicken Burger")
    print("2. Pork Burger")
    print("3. Beef Burger")


def showBeefBurgerRarity():
    print("How would you like your steak?")
    print("1. Rare")
    print("2. Medium")
    print("3. Well Done")


def showMenuIngredient():
    print("Burger will have default toppings of")
    print("1. Lettuce")
    print("2. Cucumber")
    print("3. Onion")
    print("If you wish to opt-out in any of this ingredient,")
    print("Please choose below.")


def showMenuSauce():
    print("Please choose your sauce.")
    print("Every order is limited to one type of sauce.")
    print("1. Chilli")
    print("2. Tomato")
    print("3. Mustard")


def showMenuAddOn():
    print("Do you wishes to add some add-on?")
    print("There are 3 types of add-on.")
    print("Drinks, Cookies and Muffin.")


def foodSelection():
    showMenuBurger()
    choice = input("Choice (1/2/3): ")
    if choice == "1":
        chickenBurger = chicken()
        showMenuIngredient()
        choiceLet = input("Do you want to opt-out lettuce? y/n: ")
        if choiceLet.upper() == "Y":
            chickenBurger.ingredient.remove("lettuce")
        elif choiceLet.upper() == "N":
            pass
        else:
            print("Wrong input. Y/N only.")  # dialog box
        choiceCuc = input("Do you want to opt-out cucumber? y/n: ")
        if choiceCuc.upper() == "Y":
            chickenBurger.ingredient.remove("cucumber")
        elif choiceCuc.upper() == "N":
            pass
        else:
            print("Wrong input. Y/N only.")  # dialog box
        choiceOni = input("Do you want to opt-out onion? y/n: ")
        if choiceOni.upper() == "Y":
            chickenBurger.ingredient.remove("onion")
        elif choiceOni.upper() == "N":
            pass
        else:
            print("Wrong input. Y/N only.")  # dialog box
        showMenuSauce()
        choiceSauce = input("Choice (1/2/3): ")
        if choiceSauce == "1":
            chickenBurger.sauce = "Chilli Sauce"
        elif choiceSauce == "2":
            chickenBurger.sauce = "Tomato Sauce"
        elif choiceSauce == "3":
            chickenBurger.sauce = "Mustard"
        else:
            print("Wrong input. Y/N only.")  # dialog box
        showMenuAddOn()
        choiceDrinks = int(input("How many drinks: "))
        choiceCookies = int(input("How many cookies: "))
        choiceMuffin = int(input("How many muffins: "))
        addon1 = addOn(choiceDrinks, choiceCookies, choiceMuffin)
        chickenBurger.addAddOn(addon1)
        addonPrice = chickenBurger.addedAddOn[0].drinkPrice() + \
            chickenBurger.addedAddOn[0].cookiesPrice() + \
            chickenBurger.addedAddOn[0].muffinPrice()
        totalPrice = addonPrice + chickenBurger.price
        print("Total Amount: RM {:.2f}" .format(totalPrice))
    elif choice == "2":
        porkBurger = pork()
        showMenuIngredient()
        choiceLet = input("Do you want to opt-out lettuce? y/n: ")
        if choiceLet.upper() == "Y":
            porkBurger.ingredient.remove("lettuce")
        elif choiceLet.upper() == "N":
            pass
        else:
            print("Wrong input. Y/N only.")  # dialog box
        choiceCuc = input("Do you want to opt-out cucumber? y/n: ")
        if choiceCuc.upper() == "Y":
            porkBurger.ingredient.remove("cucumber")
        elif choiceCuc.upper() == "N":
            pass
        else:
            print("Wrong input. Y/N only.")  # dialog box
        choiceOni = input("Do you want to opt-out onion? y/n: ")
        if choiceOni.upper() == "Y":
            porkBurger.ingredient.remove("onion")
        elif choiceOni.upper() == "N":
            pass
        else:
            print("Wrong input. Y/N only.")  # dialog box
        showMenuSauce()
        choiceSauce = input("Choice (1/2/3): ")
        if choiceSauce == "1":
            porkBurger.sauce = "Chilli Sauce"
        elif choiceSauce == "2":
            porkBurger.sauce = "Tomato Sauce"
        elif choiceSauce == "3":
            porkBurger.sauce = "Mustard"
        else:
            print("Wrong input. Y/N only.")  # dialog box
        showMenuAddOn()
        choiceDrinks = int(input("How many drinks: "))
        choiceCookies = int(input("How many cookies: "))
        choiceMuffin = int(input("How many muffins: "))
        addon1 = addOn(choiceDrinks, choiceCookies, choiceMuffin)
        porkBurger.addAddOn(addon1)
        addonPrice = porkBurger.addedAddOn[0].drinkPrice() + \
            porkBurger.addedAddOn[0].cookiesPrice() + \
            porkBurger.addedAddOn[0].muffinPrice()
        totalPrice = addonPrice + porkBurger.price
        print("Total Amount: RM {:.2f}" .format(totalPrice))
    elif choice == "3":
        beefBurger = beef()
        showBeefBurgerRarity()
        choiceRarity = input("Choice (1/2/3): ")
        if choiceRarity == "1":
            beefBurger.setRarity("Rare")
        elif choiceRarity == "2":
            beefBurger.setRarity("Medium")
        elif choiceRarity == "3":
            beefBurger.setRarity("Well")
        else:
            print("Wrong input. Y/N only.")  # dialog box
        showMenuIngredient()
        choiceLet = input("Do you want to opt-out lettuce? y/n: ")
        if choiceLet.upper() == "Y":
            beefBurger.ingredient.remove("lettuce")
        elif choiceLet.upper() == "N":
            pass
        else:
            print("Wrong input. Y/N only.")  # dialog box
        choiceCuc = input("Do you want to opt-out cucumber? y/n: ")
        if choiceCuc.upper() == "Y":
            beefBurger.ingredient.remove("cucumber")
        elif choiceCuc.upper() == "N":
            pass
        else:
            print("Wrong input. Y/N only.")  # dialog box
        choiceOni = input("Do you want to opt-out onion? y/n: ")
        if choiceOni.upper() == "Y":
            beefBurger.ingredient.remove("onion")
        elif choiceOni.upper() == "N":
            pass
        else:
            print("Wrong input. Y/N only.")  # dialog box
        showMenuSauce()
        choiceSauce = input("Choice (1/2/3): ")
        if choiceSauce == "1":
            beefBurger.sauce = "Chilli Sauce"
        elif choiceSauce == "2":
            beefBurger.sauce = "Tomato Sauce"
        elif choiceSauce == "3":
            beefBurger.sauce = "Mustard"
        else:
            print("Wrong input. Y/N only.")  # dialog box
        showMenuAddOn()
        choiceDrinks = int(input("How many drinks: "))
        choiceCookies = int(input("How many cookies: "))
        choiceMuffin = int(input("How many muffins: "))
        addon1 = addOn(choiceDrinks, choiceCookies, choiceMuffin)
        beefBurger.addAddOn(addon1)
        addonPrice = beefBurger.addedAddOn[0].drinkPrice() + \
            beefBurger.addedAddOn[0].cookiesPrice() + \
            beefBurger.addedAddOn[0].muffinPrice()
        totalPrice = addonPrice + beefBurger.price + beefBurger.rarity
        print("Total Amount: RM {:.2f}" .format(totalPrice))


if __name__ == "__main__":
    foodSelection()
