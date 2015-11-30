import osvr.ClientKit
def myTrackerCallback(userdata, timestamp, report):
	print("Got POSE report: Position = (%f, %f, %f), orientation = (%f, %f, %f, %f)\n" % (report.contents.pose.translation.data[0], report.contents.pose.translation.data[1], report.contents.pose.translation.data[2], report.contents.pose.rotation.data[0], report.contents.pose.rotation.data[1], report.contents.pose.rotation.data[2], report.contents.pose.rotation.data[3]))

def myOrientationCallback(userdata, timestamp, report):
	print("Got ORIENTATION report: Orientation = (%f, %f, %f, %f)\n" % (report.contents.pose.rotation.data[0], report.contents.pose.rotation.data[1], report.contents.pose.rotation.data[2], report.contents.pose.rotation.data[3]))

def myPositionCallback(userdata, timestamp, report):
	print("Got POSITION report: Position = (%f, %f, %f)\n" % (report.contents.xyz.data[0], report.contents.xyz.data[1], report.contents.xyz.data[2]))

ctx = osvr.ClientKit.ClientContext("com.osvr.exampleclients.TrackerCallback")
lefthand = ctx.getInterface("/me/head")

poseCallback = osvr.ClientKit.PoseCallback(myTrackerCallback)

orientationCallback = osvr.ClientKit.OrientationCallback(myOrientationCallback)

positionCallback = osvr.ClientKit.PositionCallback(myPositionCallback)

lefthand.registerCallback(poseCallback, None)
lefthand.registerCallback(orientationCallback, None)
lefthand.registerCallback(positionCallback, None)

for i in range(0, 1000000):
    ctx.update()

ctx.shutdown()

print("Library shut down, exiting.\n")