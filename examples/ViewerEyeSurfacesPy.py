import osvr.ClientKit
from osvr.ClientKitRaw import ReturnError


ctx = osvr.ClientKit.ClientContext("com.osvr.example.ViewerEyeSurfaces")
while True:
	print("Trying to get the display config")
	ctx.update()
	try:
		display = ctx.getDisplayConfig()
	except ReturnError:
		continue
	else:
		break
viewers = display.getNumViewers()

for viewer in range(0, viewers.value):
	 print("Viewer %d" % (viewer))
	 eyes = display.getNumEyesForViewer(viewer)
	 for eye in range(0, eyes.value):
	 	print("\tEye %d" % (eye))
 		surfaces = display.getNumSurfacesForViewerEye(viewer, eye)
 		for surface in range(0, surfaces.value):
 			print("\t\tSurface %d" % (surface))
display.dispose()
ctx.shutdown()
print("Library shut down, exiting")