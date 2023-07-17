import pickle
class dataDump:
    def saveData(fileName, folder, objectData):
        filePath = folder + "\\" + fileName + ".obj"
        fileObject = open(filePath, 'wb')
        pickle.dump(objectData, fileObject)
        fileObject.close()
