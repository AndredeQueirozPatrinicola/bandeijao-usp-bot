from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from functools import cached_property
from datetime import datetime
from .utils import Utils


class Crawler:

    def __init__(self, unidade) -> None:
        self._dia = datetime.now().weekday()
        self.unidade = unidade
        self._url = "https://uspdigital.usp.br/rucard/Jsp/cardapioSAS.jsp?codrtn="

    @property
    def dia(self):
        return Utils().pega_dia_da_semana(self._dia)

    @property
    def url(self):
        if self.unidade == "/Central":
            return self._url + '6'
        if self.unidade == "/Prefeitura":
            return self._url + '7'
        if self.unidade == "/Fisica":
            return self._url + '8'
        if self.unidade == "/Quimicas":
            return self._url + '9'

    @property
    def page(self):
        with sync_playwright() as p:
            browser = p.firefox.launch()
            page = browser.new_page()
            page_path = self.url
            page.goto(page_path)
            page.wait_for_selector(".itensCardapio")
            page_content = page.content()
            soup = BeautifulSoup(page_content, features="html.parser")
            browser.close()
            return soup

    def pega_refeicao(self, refeicao):
        soup = self.page
        return soup.find_all(id=f'{refeicao}{self.dia}')

    def trata_dados(self, refeicao):
        try:
            dados = str(self.pega_refeicao(refeicao))
            template = f'[<td id="{refeicao}{self.dia}">'
            dados = dados.split('<br/>')
            primeiro_item = dados[0].split(template)
            dados[0] = primeiro_item[1].replace('/', ',')
            dados.pop()
            labels = ['arroz_feijao', 'mistura_principal', 'pvt', 'mistura_secundaria','salada','sobremesa','pao_refresco']

            resultado = {}
            x = 0
            for dado in dados:
                resultado[labels[x]] = dado
                x += 1

            if not resultado:
                raise Exception("No-Data")

            return resultado
        except:
            raise Exception("No-data")

        

            

