'''
* @Author: Namratha N Shetty
* @Date: 2021-09-21 20:00  
* @Last Modified by: Namratha N Shetty
* @Last Modified time: 2021-09-21 20:23
* @Title: To pass all the email samples given in the list.
'''
class EmailSamples:

    validEmails = ["abc@yahoo.com","abc-100@yahoo.com", "abc.100@yahoo.com", 
                   "abc111@abc.com", "abc-100@abc.net", "abc.100@abc.com.au", 
                   "abc@1.com", "abc@gmail.com.com","abc+100@gmail.com"]
    
    inValidEmails = ["abc","abc@.com.my","abc123@gmail.a","abc123@.com",
                   "abc123@.com.com",".abc@abc.com","abc()*@gmail.com","abc@%*.com",
                   "abc..2002@gmail.com","abc.@gmail.com","abc@abc@gmail.com",
                   "abc@gmail.com.1a","abc@gmail.com.aa.au"]