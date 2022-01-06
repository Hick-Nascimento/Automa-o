import pyautogui
import time

pyautogui.alert("O código vai começar. Não use o seu computador enquanto o código está rodando")
pyautogui.PAUSE = 0.5

# ABRIR O GOOGLE DRIVE NO MEU COMPUTADOR
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')

#ENTRAR NA MINHA ÁREA DE TRABALHO
pyautogui.hotkey('winleft', 'd')
#CLICAR NO ARQUIVO QUE EU QUERO FAZER BACKUP E ARRASTEI ELE
pyautogui.moveTo(265, 644)
pyautogui.mouseDown()
pyautogui.moveTo(997, 639)
#ENQUANTO EU ARRASTO, MUDO PARA GOOGLE DRIVE
pyautogui.hotkey('alt','tab')
time.sleep(1)
#LARGUEI O ARQUIVO NO GOOGLE DRIVE
pyautogui.mouseUp()
#ESPERAR 5 SEGUNDOS
time.sleep(5)

pyautogui.alert("Pode usar seu computador")


