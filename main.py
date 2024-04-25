# import webdriver

from pprint import pprint
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# import KEYS
from selenium.webdriver.common.keys import Keys


# Mantener el navegador abierto después de que el script ha sido ejecutado
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)


# Crear objeto webdriver para Chrome con las opciones configuradas
driver = webdriver.Chrome(options=chrome_options)

# Diccionario donde se guardarán los elementos encontrados
events_dictionary = {}


try:

    # Obtener página web
    driver.get("http://secure-retreat-92358.herokuapp.com/")


    sleep(5)  
   
    
    # Esperar hasta que los elementos estén disponibles
    wait = WebDriverWait(driver, 5)
    
    
    #encontrando el elemento input first name 
    first_name = wait.until(EC.presence_of_element_located((By.NAME, 'fName')))
    
    
    #encontrando el elemento input lastname 
    last_name = wait.until(EC.presence_of_element_located((By.NAME, 'lName')))
    
    
    #encontrando el elemento input email
    email = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
    
    
    #encontrando el boton "sing up"
    sign_up_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'form button')))    
    
    
except Exception as err:
    
    # Imprimir un mensaje de error si ocurre una excepción
    print(f"El elemento no fue encontrado: {err}")  


else:
    
    #si se encontraron los elementos, entonces procedemos a llenar la informacion
    first_name.send_keys("Ricardo", Keys.ENTER)
    
    
    last_name.send_keys("Gomez", Keys.ENTER)
    
    
    email.send_keys("bardack134@gmail.com", Keys.ENTER)
    
      
finally:
    # Cerrar el navegador
    # driver.quit()
    pass