from datetime import datetime


class Message:

    def __init__(self, message=""):
        self.message = message

    def is_valid(self):
        if self.message.from_user.is_bot:
            return False
        if self.message.content_type != 'text':
            return False
        return True

    def pega_dia_da_semana(self, dia):
        dias = {
            0 : 'Segunda',
            1 : 'Terca',
            2 : 'Quarta',
            3 : 'Quinta',
            4 : 'Sexta',
            5 : 'Sabado',
            6 : "Domingo",
        }
        return dias.get(dia)

    def formata_data(self):
        dia = int(datetime.now().day)
        mes = int(datetime.now().month)
        ano = datetime.now().year
        
        if dia < 10:
            dia = f'0{dia}'
        if mes < 10:
            mes = f'0{mes}'

        return f'{dia}/{mes}/{ano}'


    def error(self, comando):
        return f"""
\U0000274C Houve um erro ao processar os dados. \U0000274C 	

    Os sistemas da USP podem estar fora do ar.

    Aguarde um instante e tente novamente:

    {comando}

    Ou volte para o /Menu.

        """

    def menu(self):
        return """
Bem vindo ao Bot do Bandeijão da USP! \U0001F601

Escolha a opção para visualizar o cardápio:

    \U0001F9EA /Quimicas

    \U0001F3EB /Central

    \U0001F52D /Fisica

    \U0001F3DB /Prefeitura

"""

    def cardapio(self, unidade: str, cardapio: dict):
        items_cardapio_almoco = cardapio[0]
        items_cardapio_jantar = cardapio[1]
        return f"""
\U0001F4C5 {self.pega_dia_da_semana(datetime.now().weekday())} - {self.formata_data()}

\U0001F9FE O cardapio da {unidade} é:

Almoço:

   \U0001F35A - {items_cardapio_almoco.get('arroz_feijao')}

   \U0001F357 - {items_cardapio_almoco.get('mistura_principal')}

   \U0001F958 - {items_cardapio_almoco.get('mistura_secundaria')}

   \U0001F9C6 - {items_cardapio_almoco.get('pvt')}

   \U0001F957 - {items_cardapio_almoco.get('salada')}

   \U0001F367 - {items_cardapio_almoco.get('sobremesa')}

Jantar:

   \U0001F35A - {items_cardapio_jantar.get('arroz_feijao')}

   \U0001F357 - {items_cardapio_jantar.get('mistura_principal')}

   \U0001F958 - {items_cardapio_jantar.get('mistura_secundaria')}

   \U0001F9C6 - {items_cardapio_jantar.get('pvt')}

   \U0001F957 - {items_cardapio_jantar.get('salada')}

   \U0001F367 - {items_cardapio_jantar.get('sobremesa')}


\U0001F449 Voltar ao /Menu
"""
        