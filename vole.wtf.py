import win32api
import win32con
import math

def drawCircle():
    for a in range(0, 640, 10):
        x = x0 + int(455 * math.cos(float(a)/100.0))
        y = y0 + int(455 * math.sin(float(a)/100.0))
        win32api.SetCursorPos((x,y))
        if a == 0:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.Sleep(20)

# OPT1: Position cursor at screen center
win32api.Sleep(1000)
x0, y0 = win32api.GetCursorPos()

# OPT2: Input screen center coords
# x0 = 960
# y0 = 530

win32api.SetCursorPos((x0,y0))

drawCircle()