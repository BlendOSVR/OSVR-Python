from osvr.ClientKitRaw import *
class Interface:
    def __init__(self, iface, ctx):
        self.interface = iface
        self.context = ctx
        self.freed = False
    def registerCallback(self, cb, userdata):
        if isinstance(cb, OSVR_PoseCallback):
            osvrRegisterPoseCallback(self.interface, cb, userdata)
        if isinstance(cb, OSVR_PositionCallback):
            osvrRegisterPositionCallback(self.interface, cb, userdata)
        if isinstance(cb, OSVR_ButtonCallback):
            osvrRegisterButtonCallback(self.interface, cb, userdata)
        if isinstance(cb, OSVR_AnalogCallback):
            osvrRegisterAnalogCallback(self.interface, cb, userdata)
        if isinstance(cb, OSVR_Location2DCallback):
            osvrRegisterLocation2DCallback(self.interface, cb, userdata)
        if isinstance(cb, OSVR_DirectionCallback):
            osvrRegisterDirectionCallback(self.interface, cb, userdata)
        if isinstance(cb, OSVR_EyeTracker2DCallback):
            osvrRegisterEyetracker2DCallback(self.interface, cb, userdata)
        if isinstance(cb, OSVR_EyeTracker3DCallback):
            osvrRegisterEyeTracker3DCallback(self.interface, cb, userdata)
        if isinstance(cb, OSVR_EyeTrackerBlinkCallback):
            osvrRegisterEyeTrackerBlinkCallback(self.interface, cb, userdata)
        if isinstance(cb, OSVR_NaviVelocityCallback):
            osvrRegisterNaviVelocityCallback(self.interface, cb, userdata)
        if isinstance(cb, OSVR_NaviPositionCallback):
            osvrRegisterNaviPositionCallback(self.interface, cb, userdata)
    def getPoseState(self):
        return osvrGetPoseState(self.interface)
    def getPositionState(self):
        return osvrGetPositionState(self.interface)
    def getOrientationState(self):
        return osvrGetOrientationState(self.interface)
    def getButtonState(self):
        return osvrGetButtonState(self.interface)
    def getAnalogState(self):
        return osvrGetAnalogState(self.interface)
    def getLocation2DState(self):
        return osvrGetLocation2DState(self.interface)
    def getDirectionState(self):
        return osvrGetDirectionState(self.interface)
    def getEyeTracker2DState(self):
        return osvrGetEyeTracker2DState(self.interface)
    def getEyeTracker3DState(self):
        return osvrGetEyeTracker3DState(self.interface)
    def getEyeTrackerBlinkState(self):
        return osvrGetEyeTrackerBlinkState(self.interface)
    def getNaviVelocityState(self):
        return osvrGetNaviVelocityState(self.interface)
    def getNaviPositionState(self):
        return osvrGetNaviPositionState(self.interface)
    def dispose(self):
        if self.freed == False:
            return osvrClientFreeInterface(self.context, self.interface)
    def __del__(self):
        self.dispose()