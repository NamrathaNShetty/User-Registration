'''
* @Author: Namratha N Shetty
* @Date: 2021-09-21 01:11  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-21 01:25
* @Title: Program Aim is to validate user entered details using regular expression.
'''

import re

from Loggers import logger

class Validation:

    def validateFirstName(firstName):
        '''
        Description:
            This method is used for validating name with regex pattern.
        Parameter:
            it takes firstname as parameter
        Return:
            It return a valid true if name is valid and false if it's invalid.
        '''

        try:
            if (re.match("^[A-Z]{1}[a-z]{2,}$",firstName)):
                return True
            else:
                return False
        
        except Exception as e:
            logger.error(e)

    def validateLastName(lastName):
        '''
        Description:
            This method is used for validating name with regex pattern.
        Parameter:
            it takes last name as parameter
        Return:
            It return a valid true if lastname is valid and false if it's invalid.
        '''

        try:
            if (re.match("^[A-Z]{1}[a-z]{2,}$",lastName)):
                return True
            else:
                return False
        
        except Exception as e:
            logger.error(e)    

    def validateEmail(email):
        '''
        Description:
            This function is used for validating email with regex pattern.
        Parameter:
            it takes self, email as parameters
        Return:
            It return a valid true if email is valid and false if it's invalid.
        '''

        try:
            
            if (re.match("^[0-9A-Za-z]+(([._+-]?)[0-9A-Za-z]+)*@[0-9A-Za-z]+.[a-z]{2,4}.([a-z]{2,3})*$", email)):
                return True
            else:
                return False

        except Exception as e:
            logger.error(e)   

    def validateNumber(phone):
        '''
        Description:
            This function is used for validating mobile number with regex pattern.
        Parameter:
            it takes self, phone as parameters
        Return:
            It return a valid true if phone is valid and false if it's invalid.
        '''

        try:

            if(re.match("^[0-9]{2}[\\s][0-9]{10}$", phone)):
                return True
            else:
                return False

        except Exception as e:
            logger.error(e)                

    def validatePassword(password):
        '''
        Description: 
            This function is used for validating password with regex pattern.
        Parameter:
            it takes self, password as parameters
        Return:
            It return a valid true if password is valid and false if it's invalid.
        '''

        try:

            if(re.match("^(?=.*\\d)([a-z])*(?=.*[A-Z])(?=.*[@#$%^&+=]).{8,}$", password)):
                return True
            else:
                return False
        
        except Exception as e:
            logger.error(e)        