'''
* @Author: Namratha N Shetty
* @Date: 2021-09-21 01:11  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-21 01:23
* @Title: Solve test cases to validate first name.
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