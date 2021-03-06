
class Patient:

    def __init__(self, userID, name, address, phoneNo):
        self.userID = userID
        self.name = name
        self.address = address
        self.phoneNo = phoneNo
        self.checkedIn = False

    def check_in():
        """ Allows patient to check in """
        self.checkedIn = True

    def change_address(new_address):
        self.address = new_address

    def change_phone_no(new_phone_no):
        self.phoneNo