class Utils:

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
        