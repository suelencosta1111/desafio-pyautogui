import pyautogui

# Posição de algo - use o mouseInfo
# Fazer algo com essa posição
pyautogui.moveTo(2107,504, duration=0.5)
for i in range(1000):
    pyautogui.click()