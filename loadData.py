import pickle
from Customer import Customer
class loadData:
    def loadCustomer(self,accountNo):
        filePath="Customer\\" + accountNo + ".obj"
        fileObj = open(filePath, 'rb')
        customerObj = pickle.load(fileObj)
        fileObj.close()
        return customerObj
    
    def printCustomer(self,customer):
        print(customer.getHomePhone())
        print(customer.getCreditCardDate())

ldData = loadData()

aCustomer = ldData.loadCustomer("1235")
ldData.printCustomer(aCustomer)
