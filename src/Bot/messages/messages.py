



class Message:

    def __init__(self, message=""):
        self.message = message

    def is_valid(self):
        if self.message.from_user.is_bot:
            return False
        if self.message.content_type != 'text':
            return False
        return True

    def error(self, comando,  exception):
        return f"""
\U0000274C Houve um erro ao processar os dados. \U0000274C 	

    Os sistemas da USP podem estar fora do ar.

    Aguarde um instante e tente novamente:

    {comando}

    Ou digite qualquer coisa para voltar ao menu.

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

    def cardapio(self, unidade: str, items_cardapio: dict):
        return f"""
O cardapio da {unidade} é:

Almoço:

   \U0001F35A - {items_cardapio.get('arroz_feijao')}

   \U0001F357 - {items_cardapio.get('mistura_principal')}

   \U0001F958 - {items_cardapio.get('mistura_secundaria')}

   \U0001F9C6 - {items_cardapio.get('pvt')}

   \U0001F957 - {items_cardapio.get('salada')}

   \U0001F367 - {items_cardapio.get('sobremesa')}
        
"""
        