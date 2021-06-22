from random import random

from diagnosticador.diagnosticador import Diagnosticador, Sintomas, LabelSintomas

def mockaDados(sintomas):
    sintomas.ultima_relacao_sexual_vaginal = 5
    sintomas.ultima_relacao_sexual_oral = 5
    sintomas.ultima_relacao_sexual_anal = 5

    sintomas.primeira_relacao_sexual_vaginal = 2500
    sintomas.primeira_relacao_sexual_oral = 2500
    sintomas.primeira_relacao_sexual_anal = 2500

    sintomas.coceira_genitalia = 60
    sintomas.dor_durante_relacao_sexual = 20
    sintomas.corrimento_amarelado_claro = 60

    sintomas.ferida_genitalia = 70

    sintomas.dor_urinar = 60
    sintomas.ingua_virilha = 60

    sintomas.ferida_cicatrizada_genitalia = 70
    sintomas.manchas_corpo = 80
    sintomas.descamacao_pele = 90
    sintomas.inguas_pelo_corpo = 80

    sintomas.lesoes_pele = 0
    sintomas.vomito = 100
    sintomas.convulsoes = 100
    sintomas.delirios = 0

    sintomas.feridas_pequenas_com_pus = 90
    sintomas.dor_genitalia = 20

if __name__ == '__main__':
    print("Bem vindo")
    diagnosticador = Diagnosticador()
    sintomas = Sintomas()
    mockaDados(sintomas)
    #diagnosticador.diagnostico_gonorreia(sintomas)
    #diagnosticador.diagnostico_sifilis_estagio1(sintomas)
    #diagnosticador.diagnostico_sifilis_estagio2(sintomas)
    #diagnosticador.diagnostico_sifilis_estagio3(sintomas)
    diagnosticador.diagnostico_cancro_mole(sintomas)

