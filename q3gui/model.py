class addOn:
    drink = 0
    cookies = 0
    muffin = 0

    # amount of drink/cookies/muffin user ordered
    def __init__(self):
        self.drink = addOn.drink
        self.cookies = addOn.cookies
        self.muffin = addOn.muffin

    def drinkPrice(self):
        return self.drink * 2.50

    def cookiesPrice(self):
        return self.cookies * 1.10

    def muffinPrice(self):
        return self.muffin * 1.20


class burger:
    ingredient = ["Lettuce", "Cucumber", "Onion"]
    sauce = None

    # ingredient be list, if user choose to opt-out use remove
    # sauce be passing fixed "string" name
    def __init__(self):
        self.name = None
        self.price = 0
        self.rarityName = 0
        self.rarity = 0
        self.ingredient = burger.ingredient
        self.sauce = burger.sauce
        self.burgerPrice = 0

    def setRarity(self, rarity):
        if rarity == "Rare":
            self.rarity = 0.50
            self.rarityName = "Rare"
        elif rarity == "Medium":
            self.rarity = 1.00
            self.rarityName = "Medium"
        elif rarity == "Well":
            self.rarity = 1.50
            self.rarityName = "Well Done"

    def setBurgerName(self, name):
        if name == "Chicken Burger":
            self.name = name
            self.price = 2.50
        elif name == "Pork Burger":
            self.name = name
            self.price = 2.00
        elif name == "Beef Burger":
            self.name = name
            self.price = 3.00

    def totaledPriceBurger(self):
        self.burgerPrice = float(self.price) + float(self.rarity)
