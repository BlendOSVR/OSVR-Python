from osvr.ClientKitRaw import *
from osvr.Interface import *
from osvr.Display import *
class ClientContext:
    def __init__(self, applicationIdentifier):
        self.context = osvrClientInit(applicationIdentifier)
        self.objList = []
    def checkStatus(self):
        return osvrClientCheckStatus(self.context)
    def update(self):
        return osvrClientUpdate(self.context)
    def getInterface(self, path):
        iface = osvrClientGetInterface(self.context, path)
        ret = Interface(iface, self.context)
        self.objList.append(ret)
        return ret
    def getDisplayConfig(self):
        disp = osvrClientGetDisplay(self.context)
        ret = DisplayConfig(disp, self.context)
        self.objList.append(ret)
        return ret
    def getStringParameter(self, path):
        length = osvrClientGetStringParameterLength(self.context, path)
        return osvrClientGetStringParameter(self.context, path, length)
    def shutdown(self):
        for object in self.objList:
            object.freed = True
        return osvrClientShutdown(self.context)
def PoseCallback(cb):
    return OSVR_PoseCallback(cb) 
def PositionCallback(cb):
    return OSVR_PositionCallback(cb)
def OrientationCallback(cb):
    return OSVR_OrientationCallback(cb)
def ButtonCallback(cb):
    return OSVR_ButtonCallback(cb)
def AnalogCallback(cb):
    return OSVR_AnalogCallback(cb)
def Location2DCallback(cb):
    return OSVR_Location2DCallback(cb)
def DirectionCallback(cb):
    return OSVR_DirectionCallback(cb)
def EyeTracker2DCallback(cb):
    return OSVR_EyeTracker2DCallback(cb)
def EyeTracker3DCallback(cb):
    return OSVR_EyeTracker3DCallback(cb)
def EyeTrackerBlinkCallback(cb):
    return OSVR_EyeTrackerBlinkCallback(cb)
def NaviVelocityCallback(cb):
    return OSVR_NaviVelocityCallback(cb)
def NaviPositionCallback(cb):
    return OSVR_NaviPositionCallback(cb)

