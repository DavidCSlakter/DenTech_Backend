from operation import Operation

class Receptionist:

    def __init__(self, receptionist_id, name, phone_no):
        self.receptionist_id = receptionist_id
        self.name = name
        self.phone_no = phone_no

    def make_appointment(operation, year, month, day, hour, minutes):
        """ Schedules and makes appointment for operation """
        operation.add_date_time(year, month, day, hour, minutes)

    def collect_fees(patient):
        """ Keep track of patient payments and set amount payable to 0 """

    def report_to_dentist(dentist):
        """ Confirms patient check in and reports to dentist of new patient check in """