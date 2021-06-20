from random import random

from diagnosticador.diagnosticador import Diagnosticador, Sintomas, LabelSintomas

def mockaDados(sintomas):
    sintomas.ultima_relacao_sexual_vaginal = 5
    sintomas.ultima_relacao_sexual_oral = 5
    sintomas.ultima_relacao_sexual_anal = 5

    sintomas.coceira_genitalia = 60
    sintomas.dor_durante_relacao_sexual = 20
    sintomas.dor_urinar = 90
    sintomas.corrimento_amarelado_claro = 60


if __name__ == '__main__':
    print("Bem vindo")
    diagnosticador = Diagnosticador()
    sintomas = Sintomas()
    mockaDados(sintomas)
    diagnosticador.diagnostico_gonorreia(sintomas)

