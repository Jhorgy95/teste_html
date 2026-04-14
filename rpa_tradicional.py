import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("file:///C:/RPA/pj_teste_html/index.html")
    page.get_by_role("textbox", name="Cliente").fill("1234567890")
    page.get_by_role("textbox", name="Valor do Pedido").fill("1000")
    page.get_by_role("textbox", name="CNPJ").fill("12345678901234")
    page.get_by_role("textbox", name="Observações").fill("Teste de observações")
    time.sleep(10)
    page.get_by_role("button", name="Submeter formulário").click(timeout=2000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
