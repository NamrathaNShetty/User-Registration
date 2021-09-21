'''
* @Author: Namratha N Shetty
* @Date: 2021-09-21 16:00  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-21 16:23
* @Title: Solve test cases for every user detail for first name, last name, email.
'''

from Validation import Validation 

import unittest 

class TestUserValidation(unittest.TestCase):
    
    def test_givenValidFirstName_shouldReturnTrue(self):
        '''
        Description:
            The given valid first name should return true in this test case.
        '''

        self.assertTrue(Validation.validateFirstName("Namratha"))
        self.assertTrue(Validation.validateFirstName("Nam"))

    def test_givenInvalidFirstName_shouldReturnFalse(self):
        '''
        Desription:
            The given invalid first name should return false in this test case.
        '''

        self.assertFalse(Validation.validateFirstName("Na"))
        self.assertFalse(Validation.validateFirstName("namratha"))
        self.assertFalse(Validation.validateFirstName("NAMRATHA"))
        self.assertFalse(Validation.validateFirstName("Namratha1"))
        self.assertFalse(Validation.validateFirstName("Namratha@"))

    def test_givenValidLastName_shouldReturnTrue(self):
        '''
        Description:
            The given valid last name should return true in this test case.
        '''

        self.assertTrue(Validation.validateLastName("Dinitha"))
        self.assertTrue(Validation.validateLastName("Din"))

    def test_givenInvalidLastName_shouldReturnFalse(self):
        '''
        Desription:
            The given invalid last name should return false in this test case.
        '''

        self.assertFalse(Validation.validateLastName("Di"))
        self.assertFalse(Validation.validateLastName("dinitha"))
        self.assertFalse(Validation.validateLastName("DINITHA"))
        self.assertFalse(Validation.validateLastName("Dinitha1"))
        self.assertFalse(Validation.validateLastName("Dinitha@"))    

    def test_givenValidEmail_shouldReturnTrue(self):
        '''
        Description:
            The given valid email should return true in test case
        Parameter:
            It takes self as a parameter.
        '''

        self.assertTrue(Validation.validateEmail("abc10@yahoo.com"))
        self.assertTrue(Validation.validateEmail("abc-100@yahoo.com"))

    def test_givenInvalidEmail_shouldReturnFalse(self):
        '''
        Description:
            The given invalid Email should return false in test case
        Parameter:
            It takes self as a parameter.
        '''

        self.assertFalse(Validation.validateEmail("abc@.com"))
        self.assertFalse(Validation.validateEmail("abc@gmail.a"))    

    def test_givenValidPhoneNumber_shouldReturnTrue(self):
        """
    Description:
        The given valid Phone number should return true in test case
    Parameter:
        It takes self as a parameter.
    """
        self.assertTrue(Validation.validateNumber("91 9618663565"))
        self.assertTrue(Validation.validateNumber("91 9865123321"))

    
    def test_givenInvalidPhoneNumber_shouldReturnFalse(self):
        """
    Description:
        The given invalid phone number should return true in test case
    Parameter:
        It takes self as a parameter.
    """
        self.assertFalse(Validation.validateNumber("91-874543"))
        self.assertFalse(Validation.validateNumber("91-0432346578"))
        self.assertFalse(Validation.validateNumber("91 572781254324"))
        self.assertFalse(Validation.validateNumber("7865438768"))
        self.assertFalse(Validation.validateNumber("91  6587654324"))
        self.assertFalse(Validation.validateNumber("91-876365r324"))
        self.assertFalse(Validation.validateNumber("91-87656@r324"))    

    def test_givenValidPassword_shouldReturnTrue(self):
        """
        Description:
            The given valid password should return true in test case
        Parameter:
            It takes self as a parameter
        """
        
        self.assertTrue(Validation.validatePassword("A$bcd4ehlkl4"))
        self.assertTrue(Validation.validatePassword("NamrathaN99$"))

    def test_givenInValidPassword_shouldReturnFalse(self):
        """
        Description:
            The given Invalid password should return true in test case
        Parameter:
            It takes self as a parameter
        """
        self.assertFalse(Validation.validatePassword("namrathashetty12"))
        self.assertFalse(Validation.validatePassword("namrathan"))
        self.assertFalse(Validation.validatePassword("1namratha"))
        self.assertFalse(Validation.validatePassword("1234567"))
        self.assertFalse(Validation.validatePassword("!@#$%1a"))    