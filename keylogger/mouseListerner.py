from pynput.mouse import Listener

def writeTofile(x,y):
    print("The position of mouse {0}".format((x,y)))

with Listener (on_move = writeTofile) as listener:
    listener.join()