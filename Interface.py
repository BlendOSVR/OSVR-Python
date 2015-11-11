from osvrClientKit import *
class Interface(self):
    def __init__(self, iface):
        self.interface = iface
    def registerCallback(self, cb, userdata):
        if isinstance(cb, OSVR_PoseCallback):
            osvrRegisterPoseCallback(self.interface, cb, userdata)
        if isinstance(cb, OSVR_PositionCallback):
            osvrRegisterPositionCallback(self.interface, cb, userdata)
        if isinstance(cb, OSVR_ButtonCallback):
            osvrRegisterButtonCallback(self.interface, cb, userdata)
        if isinstance(cb, OSVR_AnalogCallback):
            osvrRegisterAnalogCallback(self.interface, cb, userdata)
        if isinstance(cb, OSVR_LocationCallback):
            osvrRegisterLocationCallback(self.interface, cb, userdata)
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
