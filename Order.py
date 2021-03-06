class Order:

    def __init__(self, item_list, productPrice, address, status, username, date, unique_id):
        self.__orderID = unique_id
        self.__item_list = item_list
        self.__productPrice = productPrice
        self.__address = address
        self.__status = status
        self.__username = username
        self.__date = date
        #
        self.__order_eta = "5"
        self.__order_log = {}
        self.__order_log_comment = 1
        self.__deliveryType = "Standard"
        self.__paymentMethod = "Paypal"
        self.__userUnitNumber = "user_unit_number"
        self.__userPostalCode = "user_postal_code"
        self.__shippingFee = float(5.99)
        self.__subtotal = float(self.__productPrice) - (self.__shippingFee)
        self.__total = self.__subtotal + self.__shippingFee
        self.__shipment_receiver = "Shipment_Receiver_Name"
        self.__fake_address = self.__address

    def get_item_list(self):
        return self.__item_list

    def get_productPrice(self):
        return self.__productPrice

    def get_orderID(self):
        return self.__orderID

    def fake_address(self):
        return self.__fake_address

    def get_address(self):
        print("address attribute is {} at address before split".format(self.__address))
        display_list = self.__fake_address.split(",")
        print(display_list)
        self.__address = display_list[1]
        print("address attribute is {} at address after split".format(self.__address))
        return self.__address

    def get_status(self):
        return self.__status

    def get_username(self):
        return self.__username

    def get_date(self):
        return self.__date

    def set_item_list(self, item_list):
        self.__item_list = item_list

    def set_productPrice(self, productPrice):
        self.__productPrice = productPrice

    def set_orderID(self, orderID):
        self.__orderID = orderID

    def set_address(self, address):
        self.__address = address

    def set_status(self, status):
        self.__status = status

    def set_username(self, username):
        self.__username = username

    def set_date(self, date):
        self.__date = date

    #
    def get_order_eta(self):
        return self.__order_eta

    def get_order_log(self):
        return self.__order_log

    def get_order_log_time(self, commentnumber):
        return self.__order_log[commentnumber][0]

    def get_order_log_comment(self, commentnumber):
        return self.__order_log[commentnumber][1]

    def get_deliveryType(self):
        return self.__deliveryType

    def get_paymentMethod(self):
        return self.__paymentMethod

    def get_userUnitNumber(self):
        print("address attribute is {} at userUnitNumber".format(self.__address))
        display_list = self.__fake_address.split(",")
        self.__userUnitNumber = display_list[3]
        return self.__userUnitNumber

    def get_userPostalCode(self):
        print("address attribute is {} at userPostalCode".format(self.__address))
        display_list = self.__fake_address.split(",")
        self.__userPostalCode = display_list[2]
        return self.__userPostalCode

    def get_shipment_receiver(self):
        print("address attribute is {} at shipment_receiver".format(self.__address))
        display_list = self.__fake_address.split(",")
        self.__shipment_receiver = display_list[0]
        return self.__shipment_receiver

    def get_subtotal(self):
        return self.__subtotal

    def get_shippingFee(self):
        return self.__shippingFee

    def get_total(self):
        return self.__total

    def add_comment(self, time, comment):
        self.__order_log[self.__order_log_comment] = [time, comment]
        self.__order_log_comment += 1

