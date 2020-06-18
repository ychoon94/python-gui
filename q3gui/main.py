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
        self.burgerPushButtHide()
        self.cbRadioButt.toggled.connect(self.rarityBoxHide)
        self.cbRadioButt.toggled.connect(self.burgerPushButtShow)
        self.pbRadioButt.toggled.connect(self.rarityBoxHide)
        self.pbRadioButt.toggled.connect(self.burgerPushButtShow)
        self.bbRadioButt.toggled.connect(self.rarityBoxShow)
        self.bbRadioButt.toggled.connect(self.burgerPushButtShow)
        self.BurgerPushButton.clicked.connect(self.nextPageToppings)

        # ingredient Customisation Tab
        self.ingredientPushButtHide()
        self.LettuceRadioButt.toggle()
        self.LettuceRadioButt.toggled.connect(self.setLettuceOnToggle)
        self.CucumberRadioButt.toggle()
        self.CucumberRadioButt.toggled.connect(self.setCucumberOnToggle)
        self.OnionRadioButt.toggle()
        self.OnionRadioButt.toggled.connect(self.setOnionOnToggle)
        self.sauceBox.activated.connect(self.setSauce)
        self.sauceBox.activated.connect(self.ingredientPushButtShow)
        self.IngredientPushButton.clicked.connect(self.nextPageAddon)

        # addon Customisation Tab
        self.addOnPushButtHide()
        self.DrinkSpinBox.valueChanged.connect(self.drinkAmount)
        self.DrinkSpinBox.valueChanged.connect(self.addOnPushButtShow)
        self.CookieSpinBox.valueChanged.connect(self.cookieAmount)
        self.CookieSpinBox.valueChanged.connect(self.addOnPushButtShow)
        self.MuffinSpinBox.valueChanged.connect(self.muffinAmount)
        self.MuffinSpinBox.valueChanged.connect(self.addOnPushButtShow)
        self.AddOnPushButton.clicked.connect(self.nextPageCheckout)

        # checkout tab
        self.tabWidget.currentChanged.connect(self.showTab)

    # hide or show the next page push button for burger tab
    def burgerPushButtHide(self):
        self.BurgerPushButton.setVisible(False)

    def burgerPushButtShow(self):
        self.BurgerPushButton.setVisible(True)

    def nextPageToppings(self):
        self.tabWidget.setCurrentIndex(1)

    # hide or show the rarity choose box
    def rarityBoxHide(self):
        self.steakRarityLabel.setVisible(False)
        self.rarityBox.setVisible(False)

    def rarityBoxShow(self):
        self.steakRarityLabel.setVisible(True)
        self.rarityBox.setVisible(True)

    # hide or show the next page push button for ingredient tab
    def ingredientPushButtHide(self):
        self.IngredientPushButton.setVisible(False)

    def ingredientPushButtShow(self):
        self.IngredientPushButton.setVisible(True)

    def nextPageAddon(self):
        self.tabWidget.setCurrentIndex(2)

    # hide or show the next page push button for addon tab
    def addOnPushButtHide(self):
        self.AddOnPushButton.setVisible(False)

    def addOnPushButtShow(self):
        self.AddOnPushButton.setVisible(True)

    def nextPageCheckout(self):
        self.tabWidget.setCurrentIndex(3)

    def setLettuceOnToggle(self, enabled):
        if enabled:
            self.LettuceRadioButt.setText("Opt-In")
            burger.ingredient.pop(0)
            burger.ingredient.insert(0, "Lettuce")
        else:
            self.LettuceRadioButt.setText("Opt-Out")
            burger.ingredient.remove("Lettuce")
            burger.ingredient.insert(0, "No Lettuce")

    def setCucumberOnToggle(self, enabled):
        if enabled:
            self.CucumberRadioButt.setText("Opt-In")
            burger.ingredient.pop(1)
            burger.ingredient.insert(1, "Cucumber")
        else:
            self.CucumberRadioButt.setText("Opt-Out")
            burger.ingredient.remove("Cucumber")
            burger.ingredient.insert(1, "No Cucumber")

    def setOnionOnToggle(self, enabled):
        if enabled:
            self.OnionRadioButt.setText("Opt-In")
            burger.ingredient.pop(2)
            burger.ingredient.append("Onion")
        else:
            self.OnionRadioButt.setText("Opt-Out")
            burger.ingredient.remove("Onion")
            burger.ingredient.insert(2, "No Onion")

    def setSauce(self):
        sauce = self.sauceBox.currentText()
        burger.sauce = sauce

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
                # set sauce label
                self.SauceLabel.setText(chickenBurger.sauce)
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
                # set sauce label
                self.SauceLabel.setText(porkBurger.sauce)
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
                # set sauce label
                self.SauceLabel.setText(beefBurger.sauce)
                # easier access for totaling amount
                burgerPrice = beefBurger.burgerPrice

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
