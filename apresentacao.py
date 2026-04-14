import time
from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("file:///C:/RPA/pj_copilot/front_exemplo_2/index.html")
    page.get_by_role("textbox", name="Cliente").fill("FBT")
    page.get_by_role("textbox", name="Valor do Pedido").fill("100,00")
    page.get_by_role("textbox", name="CNPJ").fill("134579846468484")
    page.get_by_role("textbox", name="Observações").fill("fatura de cobrança")
    time.sleep(10)
    page.get_by_role("button", name="Submeter formulário").click(timeout=1000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
