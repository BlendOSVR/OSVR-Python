import osvr.ClientKit

def myButtonCallback(userdata, timestamp, report):
	print("Got report: button is %f" % (report.contents.state))

ctx = osvr.ClientKit.ClientContext("com.osvr.exampleclients.ButtonCallback")
button1 = ctx.getInterface("/controller/left/1")

buttonCallback = osvr.ClientKit.ButtonCallback(myButtonCallback)
iface.registerCallback(buttonCallback, None)

for i in range(0, 1000000):
    ctx.update()

ctx.shutdown()

print("Library shut down, exiting.\n")
