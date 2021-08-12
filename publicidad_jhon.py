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


for j in range(5): 
    grupos= ["https://www.facebook.com/groups/567934064125211/?multi_permalinks=867170400868241", "https://www.facebook.com/groups/577585325647789/?multi_permalinks=6045729865499947", "https://www.facebook.com/groups/348602298874004", "https://www.facebook.com/groups/703177203897461", "https://www.facebook.com/groups/131320474089419", "https://www.facebook.com/groups/834450273373156", "https://www.facebook.com/groups/557100551126319", "https://www.facebook.com/groups/415363229051752", "https://www.facebook.com/groups/568213340208048", "https://www.facebook.com/groups/2328913390466801"]

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


    userName.send_keys("9993572921")
    password.send_keys("Serranosoto1" + Keys.ENTER)
    time.sleep(1)



    grupos= ["https://www.facebook.com/groups/567934064125211/?multi_permalinks=867170400868241", "https://www.facebook.com/groups/577585325647789/?multi_permalinks=6045729865499947", "https://www.facebook.com/groups/348602298874004", "https://www.facebook.com/groups/703177203897461", "https://www.facebook.com/groups/131320474089419", "https://www.facebook.com/groups/834450273373156", "https://www.facebook.com/groups/557100551126319", "https://www.facebook.com/groups/415363229051752", "https://www.facebook.com/groups/568213340208048", "https://www.facebook.com/groups/2328913390466801"]

    mensaje= "https://www.facebook.com/109643408001996/posts/127080959591574/?d=n"
    

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

            if link== "https://www.facebook.com/groups/703177203897461":
                for i in range(23):
                    pyautogui.keyDown('tab')
                    pyautogui.keyUp('tab') 

                pyautogui.keyDown('enter')
                pyautogui.keyUp('enter')

            elif link=="https://www.facebook.com/groups/415363229051752" or link=="https://www.facebook.com/groups/568213340208048": 
                for i in range(22):
                    pyautogui.keyDown('tab')
                    pyautogui.keyUp('tab') 

                pyautogui.keyDown('enter')
                pyautogui.keyUp('enter')

            elif link== "https://www.facebook.com/groups/834450273373156": 
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

            pyautogui.keyDown('shift')

            for i in range(67):
                pyautogui.keyDown('left')
                pyautogui.keyUp('left') 

            pyautogui.keyUp('shift')

            pyautogui.keyDown('backspace')
            pyautogui.keyUp('backspace') 

            time.sleep(7)

            pyautogui.keyDown('mayus')

            time.sleep(7)

            for i in range(3):
                pyautogui.keyDown('tab')
                pyautogui.keyUp('tab') 

            pyautogui.keyUp('mayus')

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