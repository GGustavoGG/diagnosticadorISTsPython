from random import random
import multiprocessing

from diagnosticador.diagnosticador import Diagnosticador, Sintomas, LabelSintomas

NUM_PROCESS = 3
limit = NUM_PROCESS

def init_process(doencas, sintomas):
    process = []
    process_started = []
    for doenca in doencas:
        p = multiprocessing.Process(target=doenca, args=[sintomas])
        process.append(p)

    return process, process_started

def start_process(process, process_started):
    global limit
    while limit and process:
        p = process.pop()
        process_started.append(p)
        p.start()
        # print(f"{p}")
        limit -= 1
        
def mockaDados(sintomas):
    sintomas.ultima_relacao_sexual_vaginal = 15
    sintomas.ultima_relacao_sexual_oral = 15
    sintomas.ultima_relacao_sexual_anal = 15

    sintomas.primeira_relacao_sexual_vaginal = 2500
    sintomas.primeira_relacao_sexual_oral = 2500
    sintomas.primeira_relacao_sexual_anal = 2500

    sintomas.corrimento_amarelado_claro = 60

    sintomas.ferida_genitalia = 70

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

    sintomas.corrimento_anormal = 80
    sintomas.dor_durante_relacao_sexual = 80
    sintomas.dor_urinar = 0
    sintomas.coceira_genitalia = 10
    
    sintomas.corrimento_vaginal_secrecao_peniana = 60
    sintomas.sangramento_vaginal_dor_testicular = 80
    sintomas.febre = 60

    sintomas.ganglio_inchado = 70
    sintomas.bolhas_regiao_genital = 60
    sintomas.ardor = 50

    sintomas.dor_cabeca = 30
    sintomas.cansaco_excessivo = 60


if __name__ == '__main__':
    diagnosticador = Diagnosticador()
    sintomas = Sintomas()
    mockaDados(sintomas)

    doencas = [
        diagnosticador.diagnostico_herpes_genital, 
        diagnosticador.diagnostico_clamidia, 
        diagnosticador.diagnostico_gonorreia, 
        diagnosticador.diagnostico_sifilis_estagio1, 
        diagnosticador.diagnostico_sifilis_estagio2, 
        diagnosticador.diagnostico_sifilis_estagio3, 
        diagnosticador.diagnostico_cancro_mole, 
        diagnosticador.diagnostico_tricomoniase,
        diagnosticador.diagnostico_hiv
    ]

    process, process_started = init_process(doencas=doencas, sintomas=sintomas)

    while process:
        start_process(process, process_started)

        for p in process_started:
            if not p.is_alive():
                process_started.remove(p)
                limit += 1
                start_process(process, process_started)

