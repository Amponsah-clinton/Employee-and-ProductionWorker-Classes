# parent class
class employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

# mutators
    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def set_new_name(self, name):
        self.name = name

    def set_new_number(self, number):
        self.number = number

# child class of employee 
class production_worker(employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate

# accessing  shift number
    def get_shift_number(self):
        return self.get_shift_number

# accessing  hourly pay rate
    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate

# setting 1 of shift_number to day and 2 of shift_number to night
    def set_shift_number(self, shift_number):
        self.shift_number = shift_number
        if self.shift_number == 1:
            print("Day shift")
        elif self.shift_number == 2:
            print("Night shift")
        else:
            print("Error, wrong input")

# setting hourly pay rate
    def set_hourly_pay_rate(self, hourly_pay_rate):
         self.hourly_pay_rate = hourly_pay_rate
    
# printing users details
    def worker_details(self):
        print("------Your Details------")
        print("Name :", self.name)
        print("Employee number :", self.number)
        print("Shift number :", self.shift_number)
        print("Hourly pay rate :", self.hourly_pay_rate)
       

#Prompt for user for details
name = input("Enter the name of the employee: ")
number = input("Enter employee number : ")
shift_number = int(input("Enter shift (1 = Day shift and 2 = Night shift): "))
hourly_pay_rate = float(input("Enter hourly pay rate: "))



productionworker = production_worker(name,number,shift_number,hourly_pay_rate)
productionworker.worker_details()



