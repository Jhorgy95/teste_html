from playwright.sync_api import Playwright, sync_playwright
import os 
from clientes import dados_cliente
import time

html_file = os.path.abspath("index_2.html")

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"file://{html_file}")
    for linha in range(len(dados_cliente)):
        page.get_by_role("textbox", name="Nome", exact=True).fill(dados_cliente[linha]["nome"])
        page.get_by_role("textbox", name="Sobrenome").fill(dados_cliente[linha]["sobrenome"])
        page.get_by_placeholder("Idade").fill(dados_cliente[linha]["idade"])
        time.sleep(3)        
        page.get_by_role("button", name="Enviar").click(timeout=5000)
        page.get_by_role("button", name="Novo formulário").click()

        
       
        print('preenchido com sucesso!')

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
