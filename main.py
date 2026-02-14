import time
import webbrowser
import pyautogui
import pyperclip

username = "username"
message_text = "text"

print("start...")
time.sleep(5)

webbrowser.open(f"https://www.tiktok.com/@{username}")

time.sleep(15)

message_button = pyautogui.locateCenterOnScreen("M.png", confidence=0.8)

if message_button:
    pyautogui.click(message_button)
    time.sleep(5)
    textbox = pyautogui.locateCenterOnScreen("T.png", confidence=0.8)
    if textbox:
        pyautogui.click(textbox)
        time.sleep(1)

        pyperclip.copy(message_text)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.press("enter")
    else:
        print("i'm not see a Message Box")
else:
    print("i'm not see a Message")
