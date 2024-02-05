# -*- coding: iso-8859-1 -*-
import time
from selenium import webdriver

# Define o caminho para o driver do Chrome
driver_path = "/chromedriver_mac_arm64/chromedriver"

# Cria uma instância do navegador
driver = webdriver.Chrome(executable_path=driver_path)

# Abre o Google
driver.get("https://www.google.com")

# Encontra o campo de busca e o botão de pesquisa
search_box = driver.find_element_by_name("q")
search_button = driver.find_element_by_name("btnK")

# Digita "Python" na caixa de busca e clica no botão de pesquisa
search_box.send_keys("Python")
search_button.click()

# Tira um print da página e salva em um arquivo
time.sleep(5) # Aguarda 5 segundos
driver.save_screenshot("screenshot.png")

# Fecha o navegador
driver.quit()

