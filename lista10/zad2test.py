import unittest

import zadanie2class

class Test_Employee(unittest.TestCase):

    def setUp(self):
        first_name = "Jakub"
        last_name = "Piotrowski"
        annual_salary =  15000
        self.employee = zadanie2class.Employee(first_name, last_name, annual_salary)

    def test_give_default_raise(self):
        annual_salary_to_test = self.employee.annual_salary + 2000
        self.employee.give_raise()

        self.assertEqual(self.employee.annual_salary, annual_salary_to_test)

    def test_give_custom_raise(self):
        annual_salary_to_test = self.employee.annual_salary + 1234
        self.employee.give_raise(1234)

        self.assertEqual(self.employee.annual_salary, annual_salary_to_test)
