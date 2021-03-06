import datetime

class Operation:

    def __init__(self, operation_id, operation_type, patient_id, dentist_id, amount):
        self.operation_id = operation_id
        self.operation_type = operation_type
        self.patient_id = patient_id
        self.dentist_id = dentist_id
        self.amount = amount
        self.date = datetime.date(0, 0, 0)
        self.time = datetime.time(0, 0)

    def add_date_time(year, month, day, hour, minutes):
        self.date = datetime.date(year, month, day)
        self.time = datetime.time(hour, minutes) 