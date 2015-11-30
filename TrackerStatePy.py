import osvr.ClientKit
from osvr.ClientKitRaw import ReturnError

ctx = osvr.ClientKit.ClientContext("com.osvr.exampleclients.TrackerState")
head = ctx.getInterface("/me/head")


for i in range (0, 1000000):
    ctx.update()
    if(i%100 == 0):
        try:
            state, timestamp = head.getPoseState()
        except ReturnError:
            pass
        else:
            print("Got pose state: Position = (%f, %f, %f), orientation = (%f, %f, %f, %f)" % (state.translation.data[0], state.translation.data[1], state.translation.data[2], state.rotation.data[0], state.rotation.data[1], state.rotation.data[2], state.rotation.data[3]))
ctx.shutdown()
print("Library shut down, exiting.")