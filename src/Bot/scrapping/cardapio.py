from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from functools import cached_property


class Menu:

    def __init__(self, unidade) -> None:
        self.unidade = unidade
        self._url = "https://uspdigital.usp.br/rucard/Jsp/cardapioSAS.jsp?codrtn="

    @property
    def url(self):
        if self.unidade == "central":
            return self._url + 6
        if self.unidade == "prefeitura":
            return self._url + 7
        if self.unidade == "fisica":
            return self._url + 8
        if self.unidade == "quimicas":
            return self._url + 9

    @property
    def page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page_path = self.url
            page.goto(page_path)
            page_content = page.content()
            soup = BeautifulSoup(page_content, features="html.parser")
            browser.close()
        return soup

