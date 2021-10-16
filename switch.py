import win32api
import win32con
import time


def mouse_click(seconds, interval, first_pos, second_pos):

    t_end = time.time() + seconds
    while time.time() < t_end:
        win32api.SetCursorPos((first_pos[0],first_pos[1]))
        time.sleep(interval)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        win32api.SetCursorPos((second_pos[0],second_pos[1]))
        time.sleep(interval)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def get_pos():

    first_click = 0
    second_click = 0

    while True:
        if win32api.GetKeyState(win32con.VK_LSHIFT) < 0:
            first_click = win32api.GetCursorPos()
            continue
        if win32api.GetKeyState(win32con.VK_LCONTROL) < 0:
            second_click = win32api.GetCursorPos()
            continue
        if first_click != 0 and second_click != 0:
            break


    return first_click, second_click
    


def main():
    
    print("Move cursor and press Left SHIFT-key and then Left CTRL-key")
    first, second = get_pos()
    print(f"First position {first}\nSecond position {second}")

    mouse_click(3, 0.2, first, second)

    print("Running...")

main()
print("Cooldown exceeded")
