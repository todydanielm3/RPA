from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_safari_and_go_to_google():
    # Configura as opções do Safari, se necessário
    options = webdriver.SafariOptions()

    # Inicia o Safari
    driver = webdriver.Safari(options=options)

    # Acessa o Google
    driver.get("https://www.google.com")
    #driver.get("https://mv.com.br/solucao/soul-mv-hospitalar")


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
    open_safari_and_go_to_google()
