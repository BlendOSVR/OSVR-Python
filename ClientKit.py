from osvrClientKit import *
from Interface import *
class ClientContext:
    objList = []
    def __init__(self, applicationIdentifier):
        self.context = osvrClientInit(applicationIdentifier)
    def checkStatus(self):
        return osvrClientCheckStatus(self.context)
    def update(self):
        return osvrClientUpdate(self.context)
    def getInterface(self, path):
        iface = osvrClientGetInterface(self.context, path)
        ret = Interface(iface, self.context))
        objList.append(ret)
        return ret
    def getDisplayConfig(self):
        return osvrClientGetDisplay(self.context)
    def getStringParameter(self, path):
        length = osvrGetStringParameterLength(self.context, path)
        return osvrGetStringParameter(self.context, path, length)
    def shutdown(self):
        for object in objList:
            object.freed = True
        return osvrClientShutdown(self.context)




 
