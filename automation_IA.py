import os
import re
import time

from playwright.sync_api import Playwright, sync_playwright

from clientes import dados_cliente

html_file = os.path.abspath("index.html")

CLICK_TIMEOUT_MS = 5000


def _form(page):
    return page.locator("#formulario")


def clicar_enviar(page) -> None:
    """Envia: data-action, classes (.btn-enviar, .btn-enviar-seta) ou nome acessível (Enviar, send, etc.)."""
    form = _form(page)
    alvo = (
        form.locator('[data-action="enviar"]')
        .or_(form.locator(".btn-enviar"))
        .or_(form.locator(".btn-enviar-seta"))
        .or_(
            form.get_by_role(
                "button",
                name=re.compile(r"enviar|send|submit|salvar|ok", re.I),
            )
        )
    )
    alvo.first.click(timeout=CLICK_TIMEOUT_MS)


def clicar_novo_formulario(page) -> None:
    """Novo formulário: data-action, .btn-novo ou texto parcial no botão."""
    form = _form(page)
    alvo = (
        form.locator('[data-action="novo-formulario"]')
        .or_(form.locator(".btn-novo"))
        .or_(
            form.get_by_role(
                "button",
                name=re.compile(r"novo|limpar|reset|outro|cadastro", re.I),
            )
        )
    )
    alvo.first.click(timeout=CLICK_TIMEOUT_MS)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"file://{html_file}")

    for linha in range(len(dados_cliente)):
        d = dados_cliente[linha]
        page.get_by_role("textbox", name="Nome", exact=True).fill(d["nome"])
        page.get_by_role("textbox", name="Sobrenome").fill(d["sobrenome"])
        page.get_by_placeholder("Idade").fill(str(d["idade"]))
        time.sleep(3)
        clicar_enviar(page)
        clicar_novo_formulario(page)
        print("preenchido com sucesso!")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
