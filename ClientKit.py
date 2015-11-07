from osvrClientKit import *
def class ClientContext(self):
    def __init__(self, applicationIdentifier):
        self.context = osvrClientInit(applicationIdentifier)
    def checkStatus(self):
        return osvrClientCheckStatus(self.context)
    def update(self):
        return osvrClientUpdate(self.context);
    def getInterface(self, path):
        osvrClientGetInterface(self.context, path, iface)
        return new Interface(iface)
    def getStringParameter(self, path):
        osvrGetStringParameter(self.context, path, buf, length)
        return path

 
