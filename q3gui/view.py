import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# from controller import *
from model import *

qt_creator_file = "form.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Food Selection Tab
        self.rarityBoxHide()
        self.cbRadioButt.toggled.connect(self.rarityBoxHide)
        self.pbRadioButt.toggled.connect(self.rarityBoxHide)
        self.bbRadioButt.toggled.connect(self.rarityBoxShow)

        # ingredient Customisation Tab
        self.LettuceRadioButt.toggle()
        self.LettuceRadioButt.toggled.connect(self.setLettuceOnToggle)
        self.CucumberRadioButt.toggle()
        self.CucumberRadioButt.toggled.connect(self.setCucumberOnToggle)
        self.OnionRadioButt.toggle()
        self.OnionRadioButt.toggled.connect(self.setOnionOnToggle)
        self.sauceBox.activated.connect(self.setSauce)

        # addon Customisation Tab
        self.DrinkSpinBox.valueChanged.connect(self.drinkAmount)
        self.CookieSpinBox.valueChanged.connect(self.cookieAmount)
        self.MuffinSpinBox.valueChanged.connect(self.muffinAmount)

        # checkout tab
        self.tabWidget.currentChanged.connect(self.showTab)

    def rarityBoxHide(self):
        self.steakRarityLabel.setVisible(False)
        self.rarityBox.setVisible(False)

    def rarityBoxShow(self):
        self.steakRarityLabel.setVisible(True)
        self.rarityBox.setVisible(True)

    def setLettuceOnToggle(self, enabled):
        if enabled:
            self.LettuceRadioButt.setText("Opt-In")
            burger.ingredient.pop(0)
            burger.ingredient.insert(0, "Lettuce")
            print(burger.ingredient)
        else:
            self.LettuceRadioButt.setText("Opt-Out")
            burger.ingredient.remove("Lettuce")
            burger.ingredient.insert(0, "No Lettuce")
            print(burger.ingredient)

    def setCucumberOnToggle(self, enabled):
        if enabled:
            self.CucumberRadioButt.setText("Opt-In")
            burger.ingredient.pop(1)
            burger.ingredient.insert(1, "Cucumber")
            print(burger.ingredient)
        else:
            self.CucumberRadioButt.setText("Opt-Out")
            burger.ingredient.remove("Cucumber")
            burger.ingredient.insert(1, "No Cucumber")
            print(burger.ingredient)

    def setOnionOnToggle(self, enabled):
        if enabled:
            self.OnionRadioButt.setText("Opt-In")
            burger.ingredient.pop(2)
            burger.ingredient.append("Onion")
            print(burger.ingredient)
        else:
            self.OnionRadioButt.setText("Opt-Out")
            burger.ingredient.remove("Onion")
            burger.ingredient.insert(2, "No Onion")
            print(burger.ingredient)

    def setSauce(self):
        sauce = self.sauceBox.currentText()
        burger.sauce = sauce
        print(burger.sauce)

    def drinkAmount(self):
        addOn.drink = self.DrinkSpinBox.value()

    def cookieAmount(self):
        addOn.cookies = self.CookieSpinBox.value()

    def muffinAmount(self):
        addOn.muffin = self.MuffinSpinBox.value()

    def showTab(self):
        # declare a variable of burgerPrice to be used later
        burgerPrice = 0
        if self.tabWidget.currentIndex() == 3:

            if self.cbRadioButt.isChecked() is True:
                # initiliaze burger object
                chickenBurger = burger()
                chickenBurger.setBurgerName("Chicken Burger")
                chickenBurger.totaledPriceBurger()
                # set burger name & rarity in checkout menu
                self.BurgerNameLabel.setText(str(chickenBurger.name))
                self.RarityLabel.setText(" ")
                # set ingredient used in checkout screen
                self.Ingredient1Label.setText(
                        str(chickenBurger.ingredient[0]))
                self.Ingredient2Label.setText(
                        str(chickenBurger.ingredient[1]))
                self.Ingredient3Label.setText(
                        str(chickenBurger.ingredient[2]))
                # set burger subtotalprice at checkout
                self.BurgerSubTotalLabel.setText(
                        str(chickenBurger.burgerPrice))
                # easier access for totaling amount
                burgerPrice = chickenBurger.burgerPrice

            elif self.pbRadioButt.isChecked() is True:
                # initiliaze burger object
                porkBurger = burger()
                porkBurger.setBurgerName("Pork Burger")
                porkBurger.totaledPriceBurger()
                # set burger name & rarity in checkout menu
                self.BurgerNameLabel.setText(str(porkBurger.name))
                self.RarityLabel.setText(" ")
                # set ingredient used in checkout screen
                self.Ingredient1Label.setText(
                        str(porkBurger.ingredient[0]))
                self.Ingredient2Label.setText(
                        str(porkBurger.ingredient[1]))
                self.Ingredient3Label.setText(
                        str(porkBurger.ingredient[2]))
                # set burger subtotalprice at checkout
                self.BurgerSubTotalLabel.setText(
                        str(porkBurger.burgerPrice))
                # easier access for totaling amount
                burgerPrice = porkBurger.burgerPrice

            elif self.bbRadioButt.isChecked() is True:
                # initiliaze burger object
                beefBurger = burger()
                beefBurger.setBurgerName("Beef Burger")
                if self.rarityBox.currentText() == "Rare + RM0.50":
                    beefBurger.setRarity("Rare")
                elif self.rarityBox.currentText() == "Medium + RM1.00":
                    beefBurger.setRarity("Medium")
                elif self.rarityBox.currentText() == "Well Done + RM1.50":
                    beefBurger.setRarity("Well")
                beefBurger.totaledPriceBurger()
                # set burger name & rarity in checkout menu
                self.BurgerNameLabel.setText(str(beefBurger.name))
                self.RarityLabel.setText(str(beefBurger.rarityName))
                # set ingredient used in checkout screen
                self.Ingredient1Label.setText(
                        str(beefBurger.ingredient[0]))
                self.Ingredient2Label.setText(
                        str(beefBurger.ingredient[1]))
                self.Ingredient3Label.setText(
                        str(beefBurger.ingredient[2]))
                # set burger subtotalprice at checkout
                self.BurgerSubTotalLabel.setText(
                        str(beefBurger.burgerPrice))
                # easier access for totaling amount
                burgerPrice = porkBurger.burgerPrice

            # create addon object
            addon = addOn()
            # set drink qty label & subtotal
            self.DrinkQtyLabel.setText(str(self.DrinkSpinBox.value()))
            self.DrinkSubTotalLabel.setText(str(addon.drinkPrice()))
            # set cookie qty label & subtotal
            self.CookieQtyLabel.setText(str(self.CookieSpinBox.value()))
            self.CookieSubTotalLabel.setText(str(addon.cookiesPrice()))
            # set muffin qty label & subtotal
            self.MuffinQtyLabel.setText(str(self.MuffinSpinBox.value()))
            self.MuffinSubTotalLabel.setText(str(addon.muffinPrice()))

            # calculate total amount
            totaledPrice = addon.drinkPrice() + addon.cookiesPrice() +\
                addon.muffinPrice() + burgerPrice
            self.totalAmountLabel.setText(str(totaledPrice))
        #print(self.tabWidget.count())
        #print(self.tabWidget.currentWidget())
        print(self.tabWidget.currentIndex())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
