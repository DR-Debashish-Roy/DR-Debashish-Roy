import pickle
from Customer import Customer
from InventoryItem import InventoryItem
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

    def loadItem(self, itemId):
        filePath = "Items\\" + itemId + ".obj"
        fileObject = open (filePath, 'rb')
        itemObj = pickle.load(fileObject)
        fileObject.close()
        return itemObj
    def printItem(self,item):
        print(item.getColor())

ldData = loadData()

aCustomer = ldData.loadCustomer("1235")
ldData.printCustomer(aCustomer)

anItem = ldData.loadItem("1")
ldData.printItem(anItem)
