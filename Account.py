class Account:
    def createAccount(self,accNo,aType, ccNo, ccDate):
        self.__accountNo = accNo
        self.__typeOfAccount = aType
        self.__creditCardNo  = ccNo
        self.__creditCardDate = ccDate

    def getAccountAccNo(self):
        return self.__accountNo
    
    def getAccountType(self):
        return self.__aType
    
    def getCreditCardNo(self):
        return self.__creditCardNo

    def getCreditCardDate (self):
        return self.__creditCardDate

    def setAccountAccNo(self,accNo):
        self.__accountNo = accNo

    def setAccountType(self,aType):
        self.__typeOfAccount = aType

    def setCreditCardNo (self, ccNo):
        self.__creditCardNo = ccNo

    def setCreditCardDate (self, ccDate):
        self.__creditCardDate = ccDate
        
