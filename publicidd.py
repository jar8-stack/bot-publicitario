from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time


driver= webdriver.Chrome(executable_path="drivers/chromedriver.exe")

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe", chrome_options=chrome_options)

driver.get("https://www.facebook.com")

driver.maximize_window()

time.sleep(1)

userName= driver.find_element_by_name("email")
password= driver.find_element_by_name("pass")


userName.send_keys("georgedelaselva1999@hotmail.com")
password.send_keys("Serranosoto2" + Keys.ENTER)
time.sleep(1)


grupos= ["https://www.facebook.com/groups/vecinosciudadcaucel", "https://www.facebook.com/groups/834450273373156", "https://www.facebook.com/groups/790247394386215", "https://www.facebook.com/groups/577585325647789", "https://www.facebook.com/groups/725543860895039", "https://www.facebook.com/groups/1083544348330563", "https://www.facebook.com/groups/1219062938160519", "https://www.facebook.com/groups/1339481162876710"]

mensaje= "Solicitamos ⚠️NUEVOS CHOFERES⚠️ PARA UBER $500 al día SIN AUTO (se te asigna uno 🚙) SOLO whatsapp 9993-90-9391"

#Recorrido de grupos
i = 1
cantidad_lograda = 0

pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')

for grupo in grupos:
    try:
        link = grupos[i]
        pyautogui.typewrite(link)
        pyautogui.typewrite('\n')

        print("Waiting for 45 seconds\n")
        time.sleep(45)

        print("Realizando posteo")

        pyautogui.typewrite('p')
        time.sleep(2)
        print("Writing post\n")
        pyautogui.typewrite("Hello there, it's a testing post from messy programmers")
        time.sleep(4)

        time.sleep(3)

        pyautogui.write(['f6'])
        time.sleep(10)
        cantidad_lograda += 1
        print(" ")
    except:
        print("Ocurrio un error con el grupo " + str(i) + ". Link: " + grupo)
    i += 1
print("Se logró publicar en " + str(cantidad_lograda) + "/" + str(len(grupos)) + " grupos.")
print("Proceso finalizado")

driver.quit()



