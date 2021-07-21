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

def valor(description):
    intensidade = [
        LabelSintomas.NENHUMA,
        LabelSintomas.BAIXA,
        LabelSintomas.MEDIA,
        LabelSintomas.ALTA
    ]
    resultado = 4
    print("\n")
    print("------------------------------------------------------------------")
    for item in enumerate(intensidade):
        print(f"{item[0]} - {item[1].name}")

    while resultado > 3:
        resultado = int(input(f"INTENSIDADE DO SINTOMA [{description}]: "))
    return intensidade[resultado].value

def mockaDados(sintomas):
    
    sintomas.ultima_relacao_sexual_vaginal = int(input(f"Última relação sexual vaginal [DIAS]: "))
    sintomas.ultima_relacao_sexual_oral = int(input(f"Última relação sexual oral [DIAS]: "))
    sintomas.ultima_relacao_sexual_anal = int(input(f"Última relação sexual anal [DIAS]: "))

    sintomas.primeira_relacao_sexual_vaginal = int(input(f"Primeira relação sexual vaginal [DIAS]: "))
    sintomas.primeira_relacao_sexual_oral = int(input(f"Primeira relação sexual oral [DIAS]: "))
    sintomas.primeira_relacao_sexual_anal = int(input(f"Primeira relação sexual anal [DIAS]: "))
    
    sintomas.corrimento_amarelado_claro = valor("Corrimento amarelado")
    sintomas.ferida_genitalia = valor("Ferida genital")
    sintomas.ingua_virilha = valor("Ingua na virilha")
    sintomas.ferida_cicatrizada_genitalia = valor("Ferida genital cicatrizada")
    sintomas.manchas_corpo = valor("Manchas no corpo")
    sintomas.descamacao_pele = valor("Descamação da pele")
    sintomas.inguas_pelo_corpo = valor("Inguas pelo corpo")
    sintomas.lesoes_pele = valor("Lesões na pele")
    sintomas.vomito = valor("Vômitos")
    sintomas.convulsoes = valor("Convulsões")
    sintomas.delirios = valor("Delírios")
    sintomas.feridas_pequenas_com_pus = valor("Pequenas feridas com pus")
    sintomas.dor_genitalia = valor("Dor genital")
    sintomas.corrimento_anormal = valor("Corrimento anormal")
    sintomas.dor_durante_relacao_sexual = valor("Dor durante a relação sexual")
    sintomas.dor_urinar = valor("Dor ao urinar")
    sintomas.coceira_genitalia = valor("Coceira genital")
    sintomas.corrimento_vaginal_secrecao_peniana = valor("Corrimento vaginal ou secreção peniana")
    sintomas.sangramento_vaginal_dor_testicular = valor("Sangramento vaginal ou dor testicular")
    sintomas.febre = valor("Febre")
    sintomas.ganglio_inchado = sintomas.inguas_pelo_corpo
    sintomas.bolhas_regiao_genital = valor("Bolhas na região genital")
    sintomas.ardor = valor("Ardor")
    sintomas.dor_cabeca = valor("Dor de cabeça")
    sintomas.cansaco_excessivo = valor("Cansaço em excesso")



if __name__ == '__main__':
    diagnosticador = Diagnosticador()
    sintomas = Sintomas()

    print("----------------------------------------")
    print("PARA DESCOBRIRMOS O QUE VOCÊ PODE TER, \nPREENCHA ALGUMAS INFORMAÇÕES BASE E \nOUTRAS RELACIONADAS AOS SINTOMAS")
    print("----------------------------------------")
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

