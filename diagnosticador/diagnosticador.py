from enum import Enum

import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def acc(*args):
    return np.sum(args)

# Possibilidade de ter a doença
class LabelDoencas(Enum):
    NENHUMA = 0
    MUITO_BAIXA = 20
    BAIXA = 40
    MEDIO = 60
    ALTA = 80
    MUITO_ALTA = 100

#Intensidaade do sintomas
class LabelSintomas(Enum):
    NENHUMA = 0
    MUITO_BAIXA = 20
    BAIXA = 40
    MEDIO = 60
    ALTA = 80
    MUITO_ALTA = 100

class Diagnosticador:

    def __init__(self, in_met_defuzz = "centroid", acuracia = 0.01) -> None:
        self.in_met_defuzz = in_met_defuzz
        self.acuracia = acuracia

    def diagnostico_gonorreia(self, sintomas):
        return

    def diagnostico_sifilis_estagio1(self):
        return

    def diagnostico_sifilis_estagio2(self):
        return

    def diagnostico_sifilis_estagio3(self):
        return

    def diaagnostico_cancro_mole(self):
        return

    def diagnosticado_tricomoniase(self):
        return

class Sintomas:
    def __init__(self):
        self.ultima_relacao_sexual_vaginal = 0
        self.ultima_relacao_sexual_oral = 0
        self.ultima_relacao_sexual_anal = 0
        self.dor_urinar = 0
        self.corrimento_amarelado_claro = 0
        self.sangramento_durante_relacao_sexual = 0
        self.dor_durante_relacao_sexual = 0
        self.coceira_genitalia = 0
        self.sangramento_anus = 0
        self.dor_garganta = 0
        self.febre = 0
        self.ferida_genitalia = 0
        self.ingua_virilha = 0
        self.ferida_cicatrizada_genitalia = 0
        self.manchas_corpo = 0
        self.mal_estar = 0
        self.dor_cabeca = 0
        self.inguas_pelo_corpo = 0
        self.dor_muscular = 0
        self.perda_peso = 0
        self.falta_apetidade = 0
        self.descamacao_pele = 0
        self.lesoes_pele = 0
        self.vomito = 0
        self.rigidez_pescoco = 0
        self.convulsoes = 0
        self.perda_auditiva = 0
        self.insonia = 0
        self.pupila_dilatada = 0
        self.reflexos_exagerados = 0
        self.delirios = 0
        self.diminuicao_memoria_recente = 0
        self.feridas_pequenas_com_pus = 0
        self.dor_genitalia = 0
        self.corrimento_anormal = 0
        self.sangramento_urinar = 0
        self.irritacao_vulvar = 0
        self.vermelhidao_genitalia = 0

