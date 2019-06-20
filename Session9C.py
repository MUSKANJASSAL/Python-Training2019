# Class Assignment

class FoodItem:
    def __init__(self, itemName, price, quantity):
        self.itemName = itemName
        self.price = price
        self.quantity = quantity

    def showItemDetails(self):
        print("=================")
        print("ItemName:\t", self.itemName)
        print("Price:\t", self.price)
        print("Quantity:\t", self.quantity)
        print("=================")

pr = []
itemList = []
choice = "yes"
while choice == "yes":
    food = FoodItem(None, None, None)
    food.itemName = input("Enter Item Name: ")
    food.price = int(input("Enter Price: "))
    food.quantity = int(input("Enter Quantity: "))
    itemList.append(food)
    pr.append(food.price)
    choice = input("Would you like to add another Address(yes/no): ")


class Order:
    def __init__(self, billNum, customerName, phone, itemList):
        print("Welcome to Oota Restaurant")
        self.billNum = billNum
        self.customerName = customerName
        self.phone = phone
        self.itemList = itemList  # HAS-A | 1 to many

    def showDetails(self):
        print("=================")
        print("Bill Number is:\t", self.billNum)
        print("Customer Name is:\t", self.customerName)
        print("Phone No. is:\t", self.phone)
        print("=================")

        print(">> Items List for {}:".format(self.customerName))
        for f in self.itemList:  # 1 to *
            print(f.showItemDetails())
        print("==================")
        """print(">> Price List for {}:".format(self.customerName))
        for p in self.pr:
            print(p.priceDetails())
         print(">>>>>>>>>>>>>>>>>>>>")"""

    def getTotalAmount(self, amount = 0):
        self.amount = 0
        for f in self.itemList:
            self.amount += f.quantity * f.price
        print("Total price is:", self.amount)

def applyPromoCode(self, promo, final_amount=0):
    self.final_amount = 0
    self.promo = promo
    if self.promo == "FLAT20" and self.amount > 500:
        self.final_amount = self.amount - (self.amount*20//100)
    elif self.promo == "FLAT30" and self.amount <=1000:
        self.final_amount = self.amount - (self.amount*30//100)
    else:
        self.final_amount = self.amount - (self.amount*50//100)
    print("Please Pay: \u20b9", self.final_amount)

"""
    #def showSortedFoodItems(self):
        #pass
"""


o1 = Order(101, "John", "+91 99999 88888", itemList)
oRef = o1
oRef.showDetails()
oRef.getTotalAmount()
oRef.applyPromoCode("FLAT30")