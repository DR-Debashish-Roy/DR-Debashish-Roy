from dataDump import dataDump
class InventoryItem:
    def createInventoryItem(self, invId, prodId,size,color,options,qoh,avgCost,reorderQty,dateLastOrder, dateLstShpmnt):
        self.__inventoryID=invId
        self.__productID = prodId
        self.__size = size
        self.__color=color
        self.__options=options
        self.__quantityOnHand=qoh
        self.__averageCost=avgCost
        self.__reorderQuantity = reorderQty
        self.__dateLastOrder = dateLastOrder
        self.__dateLastShipment = dateLstShpmnt
    def updateQty(self,qty):
        self.__quantityOnHand= self.__quantityOnHand - qty
        return "Updated"

    def getInventoryID (self):
        return self.__inventoryID
    
    def getProductionID (self):
        return self.__productID

    def getSize(self):
        return self.__size
    
    def getColor(self):
        return self.__color
    
    def getOptions(self):
        return self.__options

    def getQuantityOnHand(self):
        return self.__quantityOnHand
    
    def getAverageCost(self):
        return self.__averageCost

    def getReorderQuantity(self):
        return self.__reorderQuantity

    def getLastOrderDate(self):
        return self.__dateLastOrder

    def getLastShipmentDate(self):
        return self.__dateLastShipment

    def setInventoryID (self,invId):
        self.__inventoryID=invId
    
    def setProductionID (self,prodId):
        self.__productID=prodId

    def setSize(self,size):
        self.__size=size
    
    def setColor(self,color):
        self.__color=color
    
    def setOptions(self,options):
        self.__options=options

    def setQuantityOnHand(self,qoh):
        self.__quantityOnHand=qoh
    
    def setAverageCost(self,avgCost):
        self.__averageCost=avgCost

    def setReorderQuantity(self,reorderQty):
        self.__reorderQuantity=reorderQty

    def setLastOrderDate(self,dateLastOrder):
        self.__dateLastOrder=dateLastOrder

    def setLastShipmentDate(self,dateLstShpmnt):
        self.__dateLastShipment=dateLstShpmnt

invItem = InventoryItem()
invItem.createInventoryItem("2","1","L","Red","M/L/XL",40,30.45,5,"20/06/2023","10/07/2023")
dataDump.saveData("2", "Items",invItem)



    
        
        
        
    
