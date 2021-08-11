"""
Nessa parte do sistema concentram-se funções responsáveis por fazer a interface com o usuário,
coletando os dados para que sejam enviados para a class diagnosticador e por consequência gerar
as preliminares sobre cada IST. Também foi criado nessa parte, a lógica para que seja executado
vários diagnosticos de forma paralela.
"""

import multiprocessing
from diagnosticador.diagnosticador import Diagnosticador, Sintomas, LabelSintomas

NUM_PROCESS = 3
limit = NUM_PROCESS

def init_process(doencas, sintomas):
    """
    Função responsável por criar uma lista com todos os processos que serão executados. Esses processos são
    diagnósticos de cada IST. Essa e uma lista vazia, processos que ainda serão iniciados, são retornados.

    :param doencas: lista com o objeto de cada função de diagnóstico IST
    :type doencas: list[]
    :param sintomas: Objeto da classe Sintomas
    :type sintomas: Sintomas
    :return: process:
    :rtype: list[]
    :return: process_started:
    :rtype: list[]
    """
    process = []
    process_started = []
    for doenca in doencas:
        p = multiprocessing.Process(target=doenca, args=[sintomas])
        process.append(p)

    return process, process_started

def start_process(process, process_started):
    """
    Função que inicia cada processo de acordo com o limite imposto
    de execuções paralelas. Após iniciar um processo, este será transferido
    para outra lista de processos que foram iniciados.

    :param process: Essa lista possui todos os processos registrados que estão aguardando para serem execudos.
    :type process: list[]
    :param process_started: Lista com todos os processos que foram executados e que ainda se encontram em execução.
    :type process_started: list[]

    """

    global limit
    while limit and process:
        p = process.pop()
        process_started.append(p)
        p.start()
        limit -= 1

def valor(description):
    """
    Função para coletar a intensidade do sintoma sentida pelo usuário. Para isso, é usado uma lista
    de enumeradores contendo todas as intensidades cadastradas no sistema. Após exibir essas opções,
    é mostrado de qual sintoma se trata. Essa informação é coletada e retornada para onde chamou.
    
    :param description: Descrição sobre o sintoma que será coletado a informação.
    :type description: String
    :return: intensidade: Intensidade sentida pelo usuário para o sintoma questionado.
    :rtype: int
    """
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
    """
    Função responsável por coletar informações do usuário para realizar o diagnostico. 
    Perguntas do tipo, 'qual foi a ultima relação sexual desprotegida' e 'quais sintomas
    o usuário está sentindo', são abordadas aqui. 
    O objeto 'sintomas' passado por parâmetro será modificado recebendo os valores informado.
    É utilizado a função valor() como auxiliar.

    :param sintomas: Objeto da classe Sintomas
    :type sintomas: Sintomas
    """
    
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
    """
    Função principal que faz interface com o usuário
    """

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

