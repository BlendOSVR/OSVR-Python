from osvrClientKit import *

class DisplayConfig
    def __init__(self, display):
        self.disp = display
    def checkDisplayStartup():
        return osvrCheckDisplayStartup(self.disp)
    def getNumDisplayInputs(self):
        return osvrGetNumDisplayInputs(self.disp)
    def getDisplayDimensions(self, displayInputIndex):
        return osvrClientGetDisplayDimensions(self.disp, displayInputIndex)
    def getNumViewers(self):
        return osvrClientGetNumViewers(self.disp)
    def getViewerPose(self, viewer):
        return osvrClientGetViewerPose(self.disp, viewer)
    def getNumEyesForViewer(self, viewer):
        return osvrClientGetNumEyesForViewer(self.disp, viewer)
    def getViewerEyePose(self, viewer, eye):
        return osvrClientGetViewerEyePose(self.disp, viewer, eye)
    def getViewerEyeViewMatrixd(self, viewer, eye, flags):
        return osvrGetViewerEyeViewMatrixd(self.disp, viewer, eye, flags)
    def getViewerEyeViewMatrixf(self, viewer, eye, flags):
        return osvrGetViewerEyeViewMatrixf(self.disp, viewer, eye flags)
    def getNumSurfacesForViewerEye(self, viewer, eye):
        return osvrGetNumSurfacesForViewerEye(self.disp, viewer, eye)
    def getRelativeViewportForViewerEyeSurface(self, viewer, eye, surface):
        return osvrGetRelativeViewportForViewerEyeSurface(self.disp, viewer, eye, surface)
    def getViewerEyeSurfaceDisplayInputIndex(self, viewer, eye, surface):
        return osvrGetViewerEyeSurfaceDisplayInputIndex(self.disp, viewer, eye, surface)
    def getProjectionMatrixForViewerEyeSurfaced(self, viewer, eye, surface, near, far, flags):
        return osvrGetViewerEyeSurfaceProjectionMatrixd(self.disp, viewer, eye, surface, near, far, flags)
    def getProjectionMatrixForViewerEyeSurfacef(self, viewer, eye, surface, near, far, flags):
        return osvrGetViewerEyeSurfaceProjectionMatrixf(self.disp, viewer, eye, surface, near, far, flags)
    def getViewerEyeSurfaceProjectionClippingPlanes(self, viewer, eye, surface):
        return osvrGetViewerEyeSurfaceProjectionClippingPlanes(self.disp, viewer, eye, surface)
    def doesViewerEyeSurfaceWantDistortion(self, viewer, eye, surface):
        return osvrDoesViewerEyeSurfaceWantDistortion(self.disp, viewer, eye, surface):
