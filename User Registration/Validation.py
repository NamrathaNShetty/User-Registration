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
            
            if (re.match("^[a-z0-9]{3,}(.[0-9a-z]+)*@[a-z]{2,15}.(com|bl)(co.in)*$", email)):
                return True
            else:
                return False

        except Exception as e:
            logger.error(e)           