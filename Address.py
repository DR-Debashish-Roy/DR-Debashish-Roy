class Address:
    def createAddress(self, accNo, aType, stNo, street, city, state, aZip):
        self.__accountNo= accNo
        self.__typeOfAddress= aType
        self.__number= stNo
        self.__street= street
        self.__city=city
        self.__state=state
        self.__postalCode= aZip
    
    def getAddressAccNo(self):
        return self.__acountNo
    def getAddressType(self):
        return self.__aType
    def getStNo(self):
        return self.__stNo
    def getStreet(self):
        return self.__street
    def getCity(self):
        return self.__city
    def getState(self):
        return self.__state
    def getPostalCode(self):
        return self.__postalCode
    
    def setAddressAccountNo(self, accNo):
        self.__accountNo= accNo
    def setAddressType(self, aType):
        self.__typeOfAddress= aType
    def setStNo(self, stNo):
        self.__number= stNo
    def setStreet(self, street):
        self.__street= street
    def setCity(self, city):
        self.__city=city
    def setState(self, state):
        self.__state=state
    def setPostalCode(self, aZip):
        self.__postalCode= aZip

    
        
        
        
        

    
        
        
    
    
