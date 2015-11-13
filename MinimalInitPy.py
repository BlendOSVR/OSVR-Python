from ClientKit import *

ctx = ClientContext("com.osvr.exampleclients.MinimalInit")

for i in range(0, 1000000):
	ctx.update()
ctx.shutdown()