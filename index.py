# Shopping Cart Design
class User:
    user_lst = [] # class variable
    def __init__(self,username, password):
        self.username = username # instance variable
        self.password = password

class Item:
    def __init__(self, itemID,price, description,quantity):
        self.itemID = itemID
        self.price = price
        self.description = description
        self.quantity = quantity

class ShoppingBasket:
    # {{"name":'rahat} }
    user_lst = [] # [{"name": "rahat", "password": "123"}, {"name": "naim", "password": "124"}] --> dictionary
                  # [["rahat", "1234"], ["naim", "1234"]] --> list
    user_ordered_data = {} # {"rahat" : [{"itemID" : 12, "price" : 200, "description" : 'abdc', "quantity" : 12}, {"itemID" : 13, "price" : 200, "description" : 'abdc', "quantity" : 12}]}
    itemsDB = [] # [{"itemID": itemID, "price": price, "description": description},{"itemID": itemID, "price": price, "description": description}]
    
    def get_userslst(self):
        return self.user_lst
    
    def create_account(self):
        name = input("Enter your username: ")
        # password = input("Enter your password: ")
        isNameExist = False # True mane hocche user already ache, False mane hocche notun user
        for user in self.get_userslst(): # user already ache kina seta check
            if user['username'] == name:
                print("Bhai tomar to account kholay ache!!!!!")
                isNameExist = True
                break
            
        if isNameExist == False:  # notun ekjon user uni, unake misty khawao
            password = input("Enter your password: ")
            self.new_user = User(name, password)
            self.user_lst.append(vars(self.new_user))
            print("Account created successfully")
        
    def addItemToCart(self, username):
        itemid = input("Enter Item Id : ")
        quantity = int(input("Enter item Quantity : "))
        flag = 0 # item unavailable
        price = 0
        for i in self.itemsDB:
            if i['itemID'] == itemid and i['quantity'] >= quantity:
                price = i['price']
                flag = 1 # item available
                break
        if flag == 0: # item unavailable
            print("Items not available")
        else: # item available
            if self.user_ordered_data.get(username) == None:
                self.user_ordered_data[username] = []
            
            self.user_ordered_data[username] += [{'itemID': itemid, 'price': price,'quantity': quantity}]
                
    def updateProductCart(self, username):
        itemid = input("Enter item ID : ")
        quantity = int(input("Enter updated quantity Number : ")) 
        for i in self.user_ordered_data[username]:
            if i.get('itemID') == itemid:
                if quantity <= i['quantity']:
                    i['quantity'] += quantity 
                else:
                    print("out of stock")
                    break
    def deleteProductCart(self, username, itemid):
        flag = 0 # item unavailable
        for i in self.itemsDB:
            if i['itemID'] == itemid:
                flag = 1 # item available
                print("available")
                break
        if flag: # item available
            for i in self.user_ordered_data[username]:
                if i['itemID'] == itemid : # searching the itemID
                    self.user_ordered_data[username].remove(i)
                    
    def showCart(self, username):
        print("Item ID \t Item Price \t Item Quantity")
        total_price = 0
        if self.user_ordered_data.get(username) is not None:
            for i in self.user_ordered_data[username]:
                print(f"{i['itemID']} \t\t {i['price']} \t\t {i['quantity']}")   
                total_price += i['price']*i['quantity']
            print("______________________________________________________")
            print(f"Total Price = {total_price}")
        else:
            print("\nEmpty Cart\n")
            
            
    # for admin only
    def addItemToDatabase(self): # admin product create korben
        itemId = input("Enter itemId: ")
        isItemAvailable = False
        for i in self.itemsDB:
            if i['itemID'] == itemId:
                isItemAvailable = True
                break
        if isItemAvailable == False:
            description = input("Enter item description: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity : "))
            self.new_item = Item(itemId,price, description, quantity)
            self.itemsDB.append(vars(self.new_item))  
        else:
            print("\nitem already added\n")
    def delProductFromDatabase(self):
        itemId = input("Enter itemId : ")         
        for i in self.itemsDB:
            if i['itemID'] == itemId:
                self.itemsDB.remove(i)
                print("\nItem Removed Successfull\n")
    
    def showItemsTable(self):
        print("Item ID \t Item Description \t Item Price \t Item Quantity")
        for i in self.itemsDB:
            print(f"{i['itemID']}\t\t {i['description']} \t\t\t {i['price']} \t\t\t {i['quantity']}")


basket = ShoppingBasket()

while True:
    print("\n1. Create an Account\n2. Login to Your Account \n3. EXIT\n")
    user_choice = int(input("Enter your choice : "))
    
    if user_choice == 3:
        break
    elif user_choice == 1:
        basket.create_account()
    elif user_choice == 2:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        isAdmin = False # normal
        flag = 0
        if name == "admin" and password == "123":
            isAdmin = True # se ekjon admin
        if isAdmin == False: #normal user/customer
            isNameExist = False # True mane hocche amar customer, False mane hocche fraud
            for user in basket.user_lst:
                if user['username'] == name and user['password'] == password:
                    isNameExist = True
                    break
            if isNameExist: # se hocche amar customer
                while True:
                    print("\nWelcome to Phitron Shopping Cart")
                    print("\n1. Add item to your cart \n2. Update your cart\n3. Delete your cart\n4. show your cart \n5. EXIT\n")
                    choice = int(input("Enter your choice : "))
                    if choice == 1:
                        basket.addItemToCart(name)
                    elif choice == 2:
                        basket.updateProductCart(name)
                    elif choice == 3:
                        item = input("Enter item id : ")
                        basket.deleteProductCart(name, item)
                    elif choice == 4:
                        basket.showCart(name)
                    else:
                        break
        else:
            while True:
                print(f"\nHello Admin, welcome back\n")
                print(f"1. Add New Item \n2. Show Items Table \n3. Delete Item\n4. Exit")
                a = int(input("Enter Your Choice : "))
                if a == 5:
                    break
                elif a == 1:
                    basket.addItemToDatabase()
                elif a == 2:
                    basket.showItemsTable()
                elif a == 3:
                    basket.delProductFromDatabase()
                elif a == 4:
                    break     
                
        


        
                
# 1. Add item to your Cart
# 2. show your cart
# 3. update your cart
# 4. deleteProductCart
            
        
        
            
# b = ShoppingBasket()                
# b.create_account()
# print(b.get_userslst())
# {}, {}
# a = [{"itemID": 12, "price": 300, "description": "description", "quantity": 4},{"itemID": 13, "price": 300, "description": "description", "quantity" : 5}]

# flag = 0 # item unavailable
# for i in a:
#     if i['itemID'] == 15 and i['quantity'] <= 4:
#         print("Items available")
#         flag = 1 # item available
#         break
    
# if not flag: # item unavailable
#     print("Items not available")

# a = {"rahat" : [{"itemID" : 12, "price" : 200, "description" : 'abdc', "quantity" : 12}]}
# # for i in a['rahat']:
# #     if i['itemID'] == 12:
# #         i['quantity'] = 134 
# # print(a['rahat'])

# for i in a['rahat']:
#     if i['itemID'] == 12: # searching the itemID
#         a['rahat'].remove(i)
# print(a['rahat'])

# b = {"rahat" : [{"itemID" : 12, "price" : 200, "description" : 'abdc', "quantity" : 12}, {"itemID" : 13, "price" : 200, "description" : 'abdc', "quantity" : 12}], "naim" : [{"itemID" : 12, "price" : 200, "description" : 'abdc', "quantity" : 12}, {"itemID" : 13, "price" : 200, "description" : 'abdc', "quantity" : 12}]}

# print(b.keys())
