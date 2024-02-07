from selenium import webdriver
from selenium.webdriver.safari.options import Options

def open_safari_and_go_to_google():
    # Configura as opções do Safari, se necessário
    options = Options()

    # Inicia o Safari
    driver = webdriver.Safari(options=options)

    # Acessa o Google
    driver.get("https://www.google.com")

    # Mantém o navegador aberto por 10 segundos
    # Você pode remover ou ajustar esse tempo conforme necessário
    driver.implicitly_wait(10)

    # Fecha o navegador
    # Remova esta linha se quiser que o navegador permaneça aberto
    driver.quit()

if __name__ == "__main__":
    open_safari_and_go_to_google()


