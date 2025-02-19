import webbrowser
import pyautogui
import time

url = "https://www.rdv-prefecture.interieur.gouv.fr/rdvpref/reservation/demarche/4564/"
url_image_txt = "https://products.aspose.ai/total/fr/image-to-text/"
webbrowser.open(url)

time.sleep(1)  # Attendre 3 secondes pour te laisser le temps de sélectionner la fenêtre

# Appuyer sur TAB trois fois
for _ in range(3):
    pyautogui.press('tab')
    time.sleep(0.5)  # Pause pour éviter d'aller trop vite

# Appuyer sur ENTER
pyautogui.press('enter')

# Appuyer sur TAB trois fois
for _ in range(7):
    pyautogui.press('tab')
    time.sleep(0.5)  # Pause pour éviter d'aller trop vite

time.sleep(1)

# 截图并保存
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

webbrowser.open(url_image_txt)
for _ in range(10):
    pyautogui.press('tab')
    time.sleep(0.5)  # Pause pour éviter d'aller trop vite

# Appuyer sur ENTER
pyautogui.press('enter')