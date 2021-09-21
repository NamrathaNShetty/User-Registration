'''
* @Author: Namratha N Shetty
* @Date: 2021-09-21 01:11  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-21 01:23
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
            it takes name as parameter
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