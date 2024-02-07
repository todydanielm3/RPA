# Antes de rodar o código, você deve:
#
# Baixar o Microsoft Edge Driver correspondente à versão do navegador Edge instalada na máquina Windows. Você pode encontrar o driver no site oficial do Edge WebDriver.
# Colocar o executável do driver (msedgedriver.exe) em um local conhecido ou adicionar o local do driver ao PATH do sistema Windows.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_edge_and_go_to_google():
    # Configura as opções do Edge, se necessário
    options = webdriver.EdgeOptions()

    # Se o Edge Driver não estiver no PATH, especifique o caminho diretamente
    # driver = webdriver.Edge(options=options, executable_path=r'C:\path\to\msedgedriver.exe')

    # Inicia o Edge
    driver = webdriver.Edge(options=options)

    # Acessa o Google
    driver.get("https://www.google.com")

    # Espera até que o elemento da página seja carregado
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Mantém o navegador aberto
    try:
        while True:
            # Verifica se o navegador foi fechado
            if not driver.window_handles:
                break
    except KeyboardInterrupt:
        # Permite que o usuário interrompa o loop com Ctrl+C
        pass
    finally:
        # Fecha o navegador quando o loop terminar
        driver.quit()

if __name__ == "__main__":
    open_edge_and_go_to_google()

