# escrever o passo a passo do meu projeto

# Passo 1 :Entrar no sistema da empresa (https://dlp.hashtagtreinamentos.com/python/intensivao/login)

import pyautogui
import time

# Pressiona a tecla Win
pyautogui.press("win")
time.sleep(5)  # Ajuste o tempo conforme necessário

# Digita "Microsoft Edge" e pressiona Enter
pyautogui.typewrite("Chrome")
pyautogui.press("enter")
time.sleep(5)  # Ajuste o tempo conforme necessário

# Digita o link e pressiona Enter
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.typFakeemailgmail.comewrite(link)
pyautogui.press("enter")

pyautogui.click(x=1225, y=446)
pyautogui.write("Fakeemail@gmail.com")







