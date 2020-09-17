import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
        # TODO add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
        # TODO you'll need to modify PhoneAssignments.add_phone() to make this test pass
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)


    def test_create_and_add_new_employee(self):
        # TODO write this test and then remove the self.fail() statement
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        employee1 = Employee(1, 'Zion')
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(employee1)
        self.assertIn(employee1, testAssignmentMgr.employees)  



    def test_create_and_add_employee_with_duplicate_id(self):
        # TODO write this test and then remove the self.fail() statement
        # TODO you'll need to fix the add_employee method in PhoneAssignments to make this test PhoneAssignments
        # This method will be similar to test_create_and_add_phone_with_duplicate_id
        testAssignmentMgr = PhoneAssignments()
        employee1 = Employee(1, 'Zion') #create employee 1
        testAssignmentMgr.add_employee(employee1) #add employee 1
        employee2 = Employee(1, 'Acadia') #this employee has same ID as empl 1
        with self.assertRaises(PhoneError):#trying to add an employee w/ dupl Id should raise a Phone Error
            testAssignmentMgr.add_employee(employee2)




    def test_assign_phone_to_employee(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments
        testAssignmentMgr = PhoneAssignments()
        employee1 = Employee(1, 'Zion') #create an employee
        testAssignmentMgr.add_employee(employee1) #add employee
        
        testPhone3 = Phone(3, 'Apple', 'iPhone 7') #create a phone
        testAssignmentMgr.add_phone(testPhone3) #add the phone
        testAssignmentMgr.assign(testPhone3.id, employee1) #assign phoneID 3 to employee1
        #assert that when phone info is called for empl 1, the phoneID is 3
        self.assertEqual(3, testAssignmentMgr.phone_info(employee1).id ) 
        


    def test_assign_phone_that_has_already_been_assigned_to_an_employee(self):
        # If a phone is already assigned to an employee, it is an error to assign it to a different employee. A PhoneError should be raised.
        # TODO you'll need to fix the assign method in PhoneAssignments so it throws an exception if the phone is alreaady assigned.
        employee1 = Employee(1, 'Zion') #create an employee
        employee2 = Employee(2, 'Voyageurs')
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(employee1) #add employee
        testAssignmentMgr.add_employee(employee2)
        testPhone1 = Phone(1, 'Apple', 'iPhone 6') #create a phone
        #testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1) #add the phone
        testAssignmentMgr.assign(testPhone1.id, employee1) #assign phoneID 1 to employee1
        #testAssignmentMgr.assign(testPhone1.id, employee2)  #assign phoneID 1 to empl 2
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testPhone1.id, employee2)  #try to assign phoneID 1 to empl 2
        


    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.
        testAssignmentMgr = PhoneAssignments()
        employee1 = Employee(1, 'Yosemite') #create an employee
        testAssignmentMgr.add_employee(employee1) #add employee
        
        testPhone1 = Phone(1, 'Apple', 'iPhone 6') #create a phone
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')
        testAssignmentMgr.add_phone(testPhone1) #add the phone
        testAssignmentMgr.add_phone(testPhone2)
        testAssignmentMgr.assign(testPhone1.id, employee1) #assign phoneID 1 to employee1
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testPhone2.id, employee1) #try to assign phone 2 to empl1, who already has a phone should raise Error
        


    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # TODO The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.
        testAssignmentMgr = PhoneAssignments()
        employee1 = Employee(1, 'Bryce') #create an employee
        testAssignmentMgr.add_employee(employee1) #add employee
        
        testPhone1 = Phone(1, 'Apple', 'iPhone 6') #create a phone
        testAssignmentMgr.add_phone(testPhone1) #add the phone
        testAssignmentMgr.assign(testPhone1.id, employee1) #assign phoneID 1 to employee1
        testAssignmentMgr.assign(testPhone1.id, employee1)  #assign same phone to same employee
        self.assertEqual(1, testAssignmentMgr.phone_info(employee1).id) #asserting that the phone belonging to emp1 is phone 1
        


    def test_un_assign_phone(self):
        # TODO write this test and remove the self.fail() statement
        # Assign a phone, unasign the phone, verify the employee_id is None
        testPhone1 = Phone(1, 'Apple', 'iPhone 6') #create a phone object
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1) #add phone
        employee1 = Employee(1, 'Zion') #create and add an employee
        testAssignmentMgr.add_employee(employee1)
        testAssignmentMgr.assign(testPhone1.employee_id,employee1) #assign  phone ID 1 to employee1
        testAssignmentMgr.un_assign(testPhone1.id) #unassign phone ID 1
        self.assertIsNone(testAssignmentMgr.un_assign(testPhone1.id)) #assert that emp_id is None for phone 1
        


    def test_get_phone_info_for_employee(self):
        # TODO write this test and remove the self.fail() statement
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned
        testAssignmentMgr = PhoneAssignments()
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')
        testAssignmentMgr.add_phone(testPhone1)#add the two phones
        testAssignmentMgr.add_phone(testPhone2) 
        employee1 = Employee(1, 'Zion') #create some employees
        employee2 = Employee(2, 'Acadia')
        testAssignmentMgr.add_employee(employee1) #add the employees
        testAssignmentMgr.add_employee(employee2)
        testAssignmentMgr.assign(testPhone2.id, employee1) #assign phone 2 to employee1
        testAssignmentMgr.assign(testPhone1.id, employee2) #assign phone 1 to empl 2
        
        self.assertEqual('iPhone 5', testAssignmentMgr.phone_info(employee1).model)
        self.assertEqual('iPhone 6', testAssignmentMgr.phone_info(employee2).model)

    # TODO check that the method returns None if the employee does not have a phone
    def test_get_phone_info_for_employee_with_no_phone(self):
        testAssignmentMgr = PhoneAssignments()
        employee1 = Employee(1, 'Zion') #create some employees
        testAssignmentMgr.add_employee(employee1) #add the employee
        self.assertEqual(None, testAssignmentMgr.phone_info(employee1) )
        
        # TODO check that the method raises an PhoneError if the employee does not exist

        #self.fail()


