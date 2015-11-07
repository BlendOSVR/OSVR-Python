from osvrClientKit import *

def class DisplayConfig
    def __init__(self, display):
        self.disp = display
    def checkDisplayStartup():
        return osvrCheckDisplayStartup(self.disp):
    def getNumDisplayInputs(self):
        osvrGetNumDisplayInputs(self.disp, ret)
        return ret
    def getDisplayDimensions(self, displayInputIndex):
         osvrClientGetDisplayDimensions(self.disp, displayInputIndex, width, height)
        return OSVR_DisplayDimensions(width, height)
    def getNumViewers(self):
        osvrClientGetNumViewers(self.disp, ret)
        return ret
    def getViewerPose(self, viewer):
        osvrClientGetViewerPose(self.disp, viewer, ret)
        return ret
    def getNumEyesForViewer(self, viewer):
        osvrClientGetNumEyesForViewer(self.disp, viewer, ret)
        return ret
    def getViewerEyePose(self, viewer, eye):
        osvrClientGetViewerEyePose(self.disp, viewer, ret)
        return ret
    def getViewerEyeViewMatrixd(self, viewer, eye, flags):
        osvrGetViewerEyeViewMatrixd(self.disp, viewer, eye, flags, ret)
        return ret
    def getViewerEyeViewMatrixf(self, viewer, eye, flags):
        osvrGetViewerEyeViewMAtrixf(self.disp, viewer, eye flags, ret)
    def getNumSurfacesForViewerEye(self, viewer, eye):
        osvrGetNumSurfacesForViewerEye(self.disp, viewer, eye, ret)
        return ret
    def getRelativeViewportForViewerEyeSurface(self, viewer, eye, surface):
        osvrGetRelativeViewportForViewerEyeSurface(self.disp, viewer, eye, ret)
        return ret
    def getViewerEyeSurfaceDisplayInputIndex(self, viewer, eye, surface):
        osvrGetViewerEyeSurfaceDisplayInputIndex(self.disp, viewer, eye, surface, ret)
        return ret
    def getProjectionMatrixForViewerEyeSurfaced(self, viewer, eye, surface, near, far, flags):
        osvrGetViewerEyeSurfaceProjectionMatrixd(self.disp, viewer, eye, surface, near, far, flags, ret)
        return ret
    def getProjectionMatrixForViewerEyeSurfacef(self, viewer, eye, surface, near, far, flags):
        osvrGetViewerEyeSurfaceProjectionMatrixf(self.disp, viewer, eye, surface, near, far, flags, ret)
        return ret
    def getViewerEyeSurfaceProjectionClippingPlanes(self, viewer, eye, surface):
        osvrGetViewerEyeSurfaceProjectionClippingPlanes(self.disp, viewer, eye, surface, ret)
        return ret
    def doesViewerEyeSurfaceWantDistortion(self, viewer, eye, surface):
        osvrDoesViewerEyeSurfaceWantDistortion(self.disp, viewer, eye, surface, ret):
        return ret
     