from Address import Address
from Account import Account
from dataDump import dataDump
import datetime

class Customer(Address, Account):
    
    def createNewCustomer(self,accountNo,name,mobilePhone, homePhone, status):
        self.__accountNo = accountNo
        self.__name= name
        self.__mobilePhone= mobilePhone
        self.__homePhone = homePhone
        self.__status= status

    def enterAddress(self, aType, stNo, street, city, state, aZip):
        self.createAddress(self.__accountNo,aType, stNo, street, city, state, aZip)
    
    def enterAccount(self,aType, ccNo, ccDate):
        self.createAccount(self.__accountNo, aType, ccNo, ccDate)
    
    def getName(self):
        return self.__name
    
    def getAccountNo(self):
        return self.__accountNo
    
    def getMobilePhone(self):
        return self.__mobilePhone
    
    def getHomePhone(self):
        return self.__homePhone
    
    def getStatus(self):
        return self.__status
    
    def setName(self,name):
        self.__name= name
        
    def setAccountNo(self,accountNo):
        self.__accountNo= accountNo
    
    def setMobilePhone(self,mobilePhone):
        self.__mobilePhone= mobilePhone

    def setHomePhone (self, homePhone):
        self.__homePhone = homePhone
    def setStatus(self, status):
        self.__status = status

        


newCustomer = Customer()
newCustomer.createNewCustomer("1235","DR", "647-123-4561", "647-201-3210","New")
newCustomer.enterAddress("Mailing","255","Dundas St. East","Toronto", "ON", "M2L KR2")
newCustomer.enterAccount("Current","4050 3301 1243 6210", datetime.date(2023, 7, 16))

'''
fileObj = open('newCustomer.obj', 'wb')
pickle.dump(newCustomer,fileObj)
fileObj.close()
'''
dataDump.saveData("1235", "Customer",newCustomer)









        
