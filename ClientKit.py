from osvrClientKit import *
from Interface import *
class ClientContext:
    def __init__(self, applicationIdentifier):
        self.context = osvrClientInit(applicationIdentifier)
    def checkStatus(self):
        return osvrClientCheckStatus(self.context)
    def update(self):
        return osvrClientUpdate(self.context)
    def getInterface(self, path):
        iface = osvrClientGetInterface(self.context, path)
        return Interface(iface)
    def getStringParameter(self, path):
        length = osvrGetStringParameterLength(self.context, path)
        return osvrGetStringParameter(self.context, path, length)
    def shutdown(self):
        return osvrClientShutdown(self.context)




 
