import osvr.ClientKit

ctx = osvr.ClientKit.ClientContext("com.osvr.exampleclients.DisplayParameter")
path = "/display"
displayDescription = ctx.getStringParameter(path)

print("Got value of %s: \n%s" % (path, displayDescription))
ctx.shutdown()
print("Library shut down, exiting.")