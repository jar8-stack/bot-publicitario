from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time
import pyperclip
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())


for j in range(7): 
    grupos= ["https://www.facebook.com/groups/vecinosciudadcaucel", "https://www.facebook.com/groups/834450273373156", "https://www.facebook.com/groups/790247394386215", "https://www.facebook.com/groups/577585325647789", "https://www.facebook.com/groups/725543860895039", "https://www.facebook.com/groups/1219062938160519", "https://www.facebook.com/groups/747410515709877"]

    driver= webdriver.Chrome(executable_path="chromedriver.exe")

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)

    driver.get("https://www.facebook.com")

    driver.maximize_window()

    time.sleep(1)

    userName= driver.find_element_by_name("email")
    password= driver.find_element_by_name("pass")


    userName.send_keys("georgedelaselva1999@hotmail.com")
    password.send_keys("Serranosoto2" + Keys.ENTER)
    time.sleep(1)


    grupos= ["https://www.facebook.com/groups/vecinosciudadcaucel", "https://www.facebook.com/groups/834450273373156", "https://www.facebook.com/groups/790247394386215", "https://www.facebook.com/groups/577585325647789", "https://www.facebook.com/groups/725543860895039", "https://www.facebook.com/groups/1219062938160519", "https://www.facebook.com/groups/173443696161082", "https://www.facebook.com/groups/747410515709877"]

    mensaje= "Solicitamos ⚠️NUEVOS CHOFERES⚠️ PARA UBER $500 al día SIN AUTO (se te asigna uno 🚙) SOLO whatsapp 9993-90-9391"
    

    time.sleep(5)


    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('t')
    pyautogui.keyUp('t')
    pyautogui.keyUp('ctrl')

    i = 1
    cantidad_lograda = 0

    for i in range(len(grupos)):

        try: 
            pyautogui.keyDown('esc')
            pyautogui.keyUp('esc')
            link = grupos[i]
            pyautogui.typewrite(link)
            pyautogui.typewrite('\n')

            print("Waiting for 45 seconds\n")
            time.sleep(25)

            if link== "https://www.facebook.com/groups/577585325647789" or link=="https://www.facebook.com/groups/1219062938160519" or link=="https://www.facebook.com/groups/173443696161082":
                for i in range(23):
                    pyautogui.keyDown('tab')
                    pyautogui.keyUp('tab') 

                pyautogui.keyDown('enter')
                pyautogui.keyUp('enter')
            else:
            
                for i in range(24):
                    pyautogui.keyDown('tab')
                    pyautogui.keyUp('tab') 

                pyautogui.keyDown('enter')
                pyautogui.keyUp('enter')



            
            time.sleep(7)
            print("Writing post\n")

            pyperclip.copy(mensaje)
            pyautogui.hotkey('ctrl', 'v', interval = 0.15)

            #pyautogui.typewrite(mensaje)
            

            time.sleep(7)

            for i in range(9):
                pyautogui.keyDown('tab')
                pyautogui.keyUp('tab') 

            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')

            time.sleep(7)

            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            pyautogui.keyUp('ctrl')

            time.sleep(3)

            pyautogui.write(['f6'])
            time.sleep(1)
            cantidad_lograda += 1
            print(" ")
        except:
            print("Ocurrio un error con el grupo " + str(i) + ". Link: " + link)
    driver.quit()
    time.sleep(1800)

print("Se logró publicar en " + str(cantidad_lograda) + "/" + str(len(grupos)) + " grupos.")
print("Proceso finalizado")