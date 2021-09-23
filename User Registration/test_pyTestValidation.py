

from Validation import Validation 
import pytest
from InputList import InputSamples

class TestUserRegistrationPytest():

    def test_givenValidFirstName_shouldReturnTrue(self):
        """
        Description:
            this function validates name
        """
        for names in InputSamples.validFirstName:
        #    print(names)
           assert Validation.validateFirstName(names) == True

    def test_givenInvalidFirstName_shouldReturnFalse(self):
        """
        Description:
            this function validates inavalid name
        """
        for names in InputSamples.invalidFirstName:
         assert Validation.validateFirstName(names) == False

    def test_givenValidLastName_shouldReturnTrue(self):
        """
        Description:
            this function validate last name
        """
        for names in InputSamples.validLastName:
         assert Validation.validateLastName(names) == True

    def test_givenInalidLastName_shouldReturnFalse(self):
        """
        Description: 
            this function validate invalid last name
        """
        for names in InputSamples.invalidLastName:
         assert Validation.validateLastName(names) == False

    def test_givenValidMail_shouldReturnTrue(self):
        """
        Description:
            this function validate mail
        """
        for email in InputSamples.validEmails:
         assert Validation.validateEmail(email) == True
        

    def test_givenInvalidMail_shouldReturnFalse(self):
        """
        Description:
            this function validate invalid mail
        """
        for email in InputSamples.invalidEmails:
         assert Validation.validateEmail(email) == False
        
    def test_givenValidPhoneNumber_shouldReturnTrue(self):
        """
        Description:
            this function validate mobile number
        """
        for number in InputSamples.validNumber:
         assert Validation.validateNumber(number) == True

    def test_givenInvalidPhoneNumber_shouldReturnFalse(self):
        """
        Description:
            this function validate invalid mobile number
        """
        for number in InputSamples.invalidNumber:
         assert Validation.validateNumber(number) == False   
        
    def test_givenValidPassword_shouldReturnTrue(self):
        """
        Description:
            this function validate password
        """
        for password in InputSamples.validPassword:
         assert Validation.validatePassword(password) == True
        
    def test_givenValidPassword_shouldReturnFalse(self):
        """
        Description:
            this function validate password
        """
        for password in InputSamples.invalidPassword:
         assert Validation.validatePassword(password) == False
        
    
    