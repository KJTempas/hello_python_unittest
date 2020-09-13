# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone():

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None


    def assign(self, employee_id):
        self.employee_id = employee_id


    def is_assigned(self):
        return self.employee_id is not None


    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)



class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)



class PhoneAssignments():

    def __init__(self):
        self.phones = []
        self.employees = []


    def add_employee(self, employee):
        # TODO raise exception if two employees with same ID are added
         #if the id assoc w/ this employee is not already in the employees list, add it
        
        for employee in self.employees:#loop though employees in list
            if employee.id == employee.id: #if you find this id already assoc w/ an employee
                raise PhoneError('That ID is already associated with an employee')  
        self.employees.append(employee) 
       
            

    def add_phone(self, phone):
        # TODO raise exception if two phones with same ID are added
        for phone in self.phones: #loop through phones list
            if phone.id == phone.id:  #if a phone has the same id as the phone you are adding
                raise PhoneError('That ID is already associated with a phone')
        
        self.phones.append(phone) 
            


    def assign(self, phone_id, employee):
        # Find phone in phones list
        for phone in self.phones:
           # if phone.id !=phone_id:
        # TODO if phone is already assigned to an employee, do not change list, raise exception
            if employee.id in self.phones:
                raise PhoneError('This phone is already assigned to an employee')
        # TODO if employee already has a phone, do not change list, and raise exception
            if phone.id in self.phones: # meaning this phoneID is already assigned 
           # if employee.id == employee_id:
                raise PhoneError('This employee has already been assigned a phone')
        # TODO if employee already has this phone, don't make any changes. This should NOT raise an exception.
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(employee.id)
                return
           

    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None


    def phone_info(self, employee):
        # find phone for employee in phones list

        # TODO  should return None if the employee does not have a phone
        if self.phones == []:
            return None
        # TODO  the method should raise an exception if the employee does not exist
        if employee not in self.employees:
            raise PhoneError('Employee not in the system')

        for phone in self.phones:
            if phone.employee_id == employee.id:
                return phone


        return None


class PhoneError(Exception):
    pass
