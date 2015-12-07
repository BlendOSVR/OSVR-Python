import osvr.ClientKit

def myAnalogCallback(userdata, timestamp, report):
	print("Got report: channel is %f" % (report.contents.state))

ctx = osvr.ClientKit.ClientContext("com.osvr.exampleclients.AnalogCallback")
iface = ctx.getInterface("/controller/left/trigger")

analogCallback = osvr.ClientKit.AnalogCallback(myAnalogCallback)
iface.registerCallback(analogCallback, None)

for i in range(0, 1000000):
    ctx.update()

ctx.shutdown()

print("Library shut down, exiting.\n")
