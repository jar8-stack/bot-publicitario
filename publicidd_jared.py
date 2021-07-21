from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time
import pyperclip



for j in range(10): 
    

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


    userName.send_keys("9997721849")
    password.send_keys("jaredserrano02" + Keys.ENTER)
    time.sleep(1)


    grupos= ["https://www.facebook.com/groups/940754222633449", "https://www.facebook.com/groups/1414974468704256", "https://www.facebook.com/groups/1210601969007059", "https://www.facebook.com/groups/834450273373156", "https://www.facebook.com/groups/747410515709877", "https://www.facebook.com/groups/382819609621203", "https://www.facebook.com/groups/785296869067527", "https://www.facebook.com/groups/662218077984422"]

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

            if link == "https://www.facebook.com/groups/1210601969007059" or link== "https://www.facebook.com/groups/834450273373156" or link== "https://www.facebook.com/groups/747410515709877" or link=="https://www.facebook.com/groups/382819609621203": 

                for i in range(22):
                    pyautogui.keyDown('tab')
                    pyautogui.keyUp('tab') 

                pyautogui.keyDown('enter')
                pyautogui.keyUp('enter')

            elif link=="https://www.facebook.com/groups/785296869067527":
                for i in range(20):
                    pyautogui.keyDown('tab')
                    pyautogui.keyUp('tab') 

                pyautogui.keyDown('enter')
                pyautogui.keyUp('enter')

            else:
                for i in range(21):
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
    time.sleep(1800)

print("Se logró publicar en " + str(cantidad_lograda) + "/" + str(len(grupos)) + " grupos.")
print("Proceso finalizado")