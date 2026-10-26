class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        if bill_amount < 0:
            print("Bill amount cannot be negative.")
        else:
            self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount

    def display_bill(self):
        print("Patient:", self.get_name())
        print("Original Bill: ₱", self.get_bill_amount(), sep="")
        print("Amount Due: ₱", self.calculate_bill(), sep="")
        print()


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85

patients = [
    Patient("Juan Dela Cruz", 15000),
    SeniorPatient("Maria Santos", 15000),
    PhilHealthPatient("Pedro Reyes", 15000)
]

for patient in patients:
    patient.display_bill()
