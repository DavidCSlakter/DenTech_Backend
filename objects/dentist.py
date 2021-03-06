from operation import Operation

class Dentist:

    def __init__(self, dentist_id, name, address, phone_no):
        self.dentist_id = dentist_id
        self.name = name
        self.address = address
        self.phone_no = phone_no

    def check_patient(patient_id):
        """ Checks patient in and should set patient checked_in attribute to false """

    def plan_operation(operation_id, operation_type, patient_id, dentist_id, amount):
        """ Creates an operation and returns it """
        return Operation(operation_id, operation_type, patient_id, dentist_id, amount)