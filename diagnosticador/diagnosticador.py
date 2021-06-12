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
    MEDIA = 60
    ALTA = 80
    MUITO_ALTA = 100

class Diagnosticador:

    def __init__(self, in_met_defuzz = "centroid", acuracia = 0.01) -> None:
        self.in_met_defuzz = in_met_defuzz
        self.acuracia = acuracia

    def diagnostico_gonorreia(self, sintomas):
        MUDA_DEZ = 10
        MUDA_VINTE = 20

        #==============================================================================================================#
        #====================================== Antecedentes e Conseqquentes ==========================================#
        #==============================================================================================================#
        ultima_relacao_sexual_vaginal = ctrl.Antecedent(np.arange(0, 11, self.acuracia), 'ultima_relacao_sexual_vaginal')
        ultima_relacao_sexual_oral = ctrl.Antecedent(np.arange(0, 11, self.acuracia), 'ultima_relacao_sexual_oral')
        ultima_relacao_sexual_anal = ctrl.Antecedent(np.arange(0, 11, self.acuracia), 'ultima_relacao_sexual_anal')

        dor_urinar = ctrl.Antecedent(np.arange(LabelSintomas.NENHUMA.value, LabelSintomas.MUITO_ALTA.value, self.acuracia), 'dor_urinar')
        corrimento_amarelado_claro = ctrl.Antecedent(np.arange(LabelSintomas.NENHUMA.value, LabelSintomas.MUITO_ALTA.value, self.acuracia), 'corrimento_amarelado_claro')
        sangramento_durante_relacao_sexual = ctrl.Antecedent(np.arange(LabelSintomas.NENHUMA.value, LabelSintomas.MUITO_ALTA.value, self.acuracia), 'sangramento_durante_relacao_sexual')
        dor_durante_relacao_sexual = ctrl.Antecedent(np.arange(LabelSintomas.NENHUMA.value, LabelSintomas.MUITO_ALTA.value, self.acuracia), 'dor_durante_relacao_sexual')
        coceira_genitalia = ctrl.Antecedent(np.arange(LabelSintomas.NENHUMA.value, LabelSintomas.MUITO_ALTA.value, self.acuracia), 'coceira_genitalia')
        sangramento_anus = ctrl.Antecedent(np.arange(LabelSintomas.NENHUMA.value, LabelSintomas.MUITO_ALTA.value, self.acuracia), 'coceira_genitalia')
        dor_garganta = ctrl.Antecedent(np.arange(LabelSintomas.NENHUMA.value, LabelSintomas.MUITO_ALTA.value, self.acuracia), 'dor_garganta')
        febre = ctrl.Antecedent(np.arange(LabelSintomas.NENHUMA.value, LabelSintomas.MUITO_ALTA.value, self.acuracia), 'febre')

        possibilidade_gonorreia = ctrl.Consequent(np.arange(LabelDoencas.NENHUMA.value, LabelDoencas.MUITO_ALTA.value, self.acuracia), 'possibilidade_gonorreia', defuzzify_method = self.in_met_defuzz)

        # ==============================================================================================================#
        # ====================================== Funções das Variáveis =================================================#
        # ==============================================================================================================#
        # Ultima relaação sexual vaginal
        ultima_relacao_sexual_vaginal['INSUFICIENTE'] = fuzz.trimf(ultima_relacao_sexual_vaginal.universe, [0, 0, 2])
        ultima_relacao_sexual_vaginal['SUFICIENTE'] = fuzz.trapmf(ultima_relacao_sexual_vaginal.universe, [0, 2, 9, 11])
        ultima_relacao_sexual_vaginal['INSUFICIENTE_ALTO'] = fuzz.trimf(ultima_relacao_sexual_vaginal.universe, [9, 11, 11])

        # Ultima relaação sexual anal
        ultima_relacao_sexual_anal['INSUFICIENTE'] = fuzz.trimf(ultima_relacao_sexual_anal.universe, [0, 0, 2])
        ultima_relacao_sexual_anal['SUFICIENTE'] = fuzz.trapmf(ultima_relacao_sexual_anal.universe, [0, 2, 9, 11])
        ultima_relacao_sexual_anal['INSUFICIENTE_ALTO'] = fuzz.trimf(ultima_relacao_sexual_anal.universe, [9, 11, 11])

        # Ultima relação sexual oral
        ultima_relacao_sexual_oral['INSUFICIENTE'] = fuzz.trimf(ultima_relacao_sexual_oral.universe, [0, 0, 2])
        ultima_relacao_sexual_oral['SUFICIENTE'] = fuzz.trapmf(ultima_relacao_sexual_oral.universe, [0, 2, 9, 11])
        ultima_relacao_sexual_oral['INSUFICIENTE_ALTO'] = fuzz.trimf(ultima_relacao_sexual_oral.universe,[9, 11, 11])

        #dor ao urinar
        dor_urinar[LabelSintomas.NENHUMA.name] = fuzz.trimf(dor_urinar.universe, [LabelSintomas.NENHUMA.value, LabelSintomas.NENHUMA.value, (LabelSintomas.NENHUMA.value + MUDA_DEZ)])
        dor_urinar[LabelSintomas.MUITO_BAIXA.name] = fuzz.trimf(dor_urinar.universe, [LabelSintomas.NENHUMA.value, LabelSintomas.MUITO_BAIXA.value, (LabelSintomas.MUITO_BAIXA.value + MUDA_VINTE)])
        dor_urinar[LabelSintomas.BAIXA.name] = fuzz.trimf(dor_urinar.universe, [LabelSintomas.BAIXA.value - MUDA_VINTE, LabelSintomas.BAIXA.value, LabelSintomas.BAIXA.value + MUDA_VINTE])
        dor_urinar[LabelSintomas.MEDIA.name] = fuzz.trimf(dor_urinar.universe, [LabelSintomas.MEDIA.value - MUDA_VINTE, LabelSintomas.MEDIA.value, LabelSintomas.MEDIA.value + MUDA_VINTE])
        dor_urinar[LabelSintomas.ALTA.name] = fuzz.trimf(dor_urinar.universe, [LabelSintomas.ALTA.value - MUDA_VINTE, LabelSintomas.ALTA.value, LabelSintomas.ALTA.value + MUDA_VINTE])
        dor_urinar[LabelSintomas.MUITO_ALTA.name] = fuzz.trimf(dor_urinar.universe, [ LabelSintomas.MUITO_ALTA - MUDA_DEZ,  LabelSintomas.MUITO_ALTA , LabelSintomas.MUITO_ALTA])

        #Corrimento amarelo claro
        corrimento_amarelado_claro[LabelSintomas.NENHUMA.name] = fuzz.trimf(corrimento_amarelado_claro.universe,[LabelSintomas.NENHUMA.value, LabelSintomas.NENHUMA.value,(LabelSintomas.NENHUMA.value + MUDA_DEZ)])
        corrimento_amarelado_claro[LabelSintomas.MUITO_BAIXA.name] = fuzz.trimf(corrimento_amarelado_claro.universe, [LabelSintomas.NENHUMA.value, LabelSintomas.MUITO_BAIXA.value, (LabelSintomas.MUITO_BAIXA.value + MUDA_VINTE)])
        corrimento_amarelado_claro[LabelSintomas.BAIXA.name] = fuzz.trimf(corrimento_amarelado_claro.universe, [LabelSintomas.BAIXA.value - MUDA_VINTE, LabelSintomas.BAIXA.value, LabelSintomas.BAIXA.value + MUDA_VINTE])
        corrimento_amarelado_claro[LabelSintomas.MEDIA.name] = fuzz.trimf(corrimento_amarelado_claro.universe, [LabelSintomas.MEDIA.value - MUDA_VINTE, LabelSintomas.MEDIA.value, LabelSintomas.MEDIA.value + MUDA_VINTE])
        corrimento_amarelado_claro[LabelSintomas.ALTA.name] = fuzz.trimf(corrimento_amarelado_claro.universe, [LabelSintomas.ALTA.value - MUDA_VINTE, LabelSintomas.ALTA.value, LabelSintomas.ALTA.value + MUDA_VINTE])
        corrimento_amarelado_claro[LabelSintomas.MUITO_ALTA.name] = fuzz.trimf(corrimento_amarelado_claro.universe, [ LabelSintomas.MUITO_ALTA - MUDA_DEZ,  LabelSintomas.MUITO_ALTA , LabelSintomas.MUITO_ALTA])

        #Sangramento Durante Relação sexual
        sangramento_durante_relacao_sexual[LabelSintomas.NENHUMA.name] = fuzz.trimf(sangramento_durante_relacao_sexual.universe,[LabelSintomas.NENHUMA.value, LabelSintomas.NENHUMA.value,(LabelSintomas.NENHUMA.value + MUDA_DEZ)])
        sangramento_durante_relacao_sexual[LabelSintomas.MUITO_BAIXA.name] = fuzz.trimf(sangramento_durante_relacao_sexual.universe, [LabelSintomas.NENHUMA.value, LabelSintomas.MUITO_BAIXA.value, (LabelSintomas.MUITO_BAIXA.value + MUDA_VINTE)])
        sangramento_durante_relacao_sexual[LabelSintomas.BAIXA.name] = fuzz.trimf(sangramento_durante_relacao_sexual.universe, [LabelSintomas.BAIXA.value - MUDA_VINTE, LabelSintomas.BAIXA.value, LabelSintomas.BAIXA.value + MUDA_VINTE])
        sangramento_durante_relacao_sexual[LabelSintomas.MEDIA.name] = fuzz.trimf(sangramento_durante_relacao_sexual.universe, [LabelSintomas.MEDIA.value - MUDA_VINTE, LabelSintomas.MEDIA.value, LabelSintomas.MEDIA.value + MUDA_VINTE])
        sangramento_durante_relacao_sexual[LabelSintomas.ALTA.name] = fuzz.trimf(sangramento_durante_relacao_sexual.universe, [LabelSintomas.ALTA.value - MUDA_VINTE, LabelSintomas.ALTA.value, LabelSintomas.ALTA.value + MUDA_VINTE])
        sangramento_durante_relacao_sexual[LabelSintomas.MUITO_ALTA.name] = fuzz.trimf(sangramento_durante_relacao_sexual.universe, [ LabelSintomas.MUITO_ALTA - MUDA_DEZ,  LabelSintomas.MUITO_ALTA , LabelSintomas.MUITO_ALTA])

        #Dor Durante Relação sexual
        dor_durante_relacao_sexual[LabelSintomas.NENHUMA.name] = fuzz.trimf(dor_durante_relacao_sexual.universe,[LabelSintomas.NENHUMA.value, LabelSintomas.NENHUMA.value,(LabelSintomas.NENHUMA.value + MUDA_DEZ)])
        dor_durante_relacao_sexual[LabelSintomas.MUITO_BAIXA.name] = fuzz.trimf(dor_durante_relacao_sexual.universe, [LabelSintomas.NENHUMA.value, LabelSintomas.MUITO_BAIXA.value, (LabelSintomas.MUITO_BAIXA.value + MUDA_VINTE)])
        dor_durante_relacao_sexual[LabelSintomas.BAIXA.name] = fuzz.trimf(dor_durante_relacao_sexual.universe, [LabelSintomas.BAIXA.value - MUDA_VINTE, LabelSintomas.BAIXA.value, LabelSintomas.BAIXA.value + MUDA_VINTE])
        dor_durante_relacao_sexual[LabelSintomas.MEDIA.name] = fuzz.trimf(dor_durante_relacao_sexual.universe, [LabelSintomas.MEDIA.value - MUDA_VINTE, LabelSintomas.MEDIA.value, LabelSintomas.MEDIA.value + MUDA_VINTE])
        dor_durante_relacao_sexual[LabelSintomas.ALTA.name] = fuzz.trimf(dor_durante_relacao_sexual.universe, [LabelSintomas.ALTA.value - MUDA_VINTE, LabelSintomas.ALTA.value, LabelSintomas.ALTA.value + MUDA_VINTE])
        dor_durante_relacao_sexual[LabelSintomas.MUITO_ALTA.name] = fuzz.trimf(dor_durante_relacao_sexual.universe, [ LabelSintomas.MUITO_ALTA - MUDA_DEZ,  LabelSintomas.MUITO_ALTA , LabelSintomas.MUITO_ALTA])

        #Coceira Genital
        coceira_genitalia[LabelSintomas.NENHUMA.name] = fuzz.trimf(coceira_genitalia.universe,[LabelSintomas.NENHUMA.value, LabelSintomas.NENHUMA.value,(LabelSintomas.NENHUMA.value + MUDA_DEZ)])
        coceira_genitalia[LabelSintomas.MUITO_BAIXA.name] = fuzz.trimf(coceira_genitalia.universe, [LabelSintomas.NENHUMA.value, LabelSintomas.MUITO_BAIXA.value, (LabelSintomas.MUITO_BAIXA.value + MUDA_VINTE)])
        coceira_genitalia[LabelSintomas.BAIXA.name] = fuzz.trimf(coceira_genitalia.universe, [LabelSintomas.BAIXA.value - MUDA_VINTE, LabelSintomas.BAIXA.value, LabelSintomas.BAIXA.value + MUDA_VINTE])
        coceira_genitalia[LabelSintomas.MEDIA.name] = fuzz.trimf(coceira_genitalia.universe, [LabelSintomas.MEDIA.value - MUDA_VINTE, LabelSintomas.MEDIA.value, LabelSintomas.MEDIA.value + MUDA_VINTE])
        coceira_genitalia[LabelSintomas.ALTA.name] = fuzz.trimf(coceira_genitalia.universe, [LabelSintomas.ALTA.value - MUDA_VINTE, LabelSintomas.ALTA.value, LabelSintomas.ALTA.value + MUDA_VINTE])
        coceira_genitalia[LabelSintomas.MUITO_ALTA.name] = fuzz.trimf(coceira_genitalia.universe, [ LabelSintomas.MUITO_ALTA - MUDA_DEZ,  LabelSintomas.MUITO_ALTA , LabelSintomas.MUITO_ALTA])

        #sangramento no anus
        sangramento_anus[LabelSintomas.NENHUMA.name] = fuzz.trimf(sangramento_anus.universe,[LabelSintomas.NENHUMA.value, LabelSintomas.NENHUMA.value,(LabelSintomas.NENHUMA.value + MUDA_DEZ)])
        sangramento_anus[LabelSintomas.MUITO_BAIXA.name] = fuzz.trimf(sangramento_anus.universe, [LabelSintomas.NENHUMA.value, LabelSintomas.MUITO_BAIXA.value, (LabelSintomas.MUITO_BAIXA.value + MUDA_VINTE)])
        sangramento_anus[LabelSintomas.BAIXA.name] = fuzz.trimf(sangramento_anus.universe, [LabelSintomas.BAIXA.value - MUDA_VINTE, LabelSintomas.BAIXA.value, LabelSintomas.BAIXA.value + MUDA_VINTE])
        sangramento_anus[LabelSintomas.MEDIA.name] = fuzz.trimf(sangramento_anus.universe, [LabelSintomas.MEDIA.value - MUDA_VINTE, LabelSintomas.MEDIA.value, LabelSintomas.MEDIA.value + MUDA_VINTE])
        sangramento_anus[LabelSintomas.ALTA.name] = fuzz.trimf(sangramento_anus.universe, [LabelSintomas.ALTA.value - MUDA_VINTE, LabelSintomas.ALTA.value, LabelSintomas.ALTA.value + MUDA_VINTE])
        sangramento_anus[LabelSintomas.MUITO_ALTA.name] = fuzz.trimf(sangramento_anus.universe, [ LabelSintomas.MUITO_ALTA - MUDA_DEZ,  LabelSintomas.MUITO_ALTA , LabelSintomas.MUITO_ALTA])

        #Dor de garganta
        dor_garganta[LabelSintomas.NENHUMA.name] = fuzz.trimf(dor_garganta.universe,[LabelSintomas.NENHUMA.value, LabelSintomas.NENHUMA.value,(LabelSintomas.NENHUMA.value + MUDA_DEZ)])
        dor_garganta[LabelSintomas.MUITO_BAIXA.name] = fuzz.trimf(dor_garganta.universe, [LabelSintomas.NENHUMA.value, LabelSintomas.MUITO_BAIXA.value, (LabelSintomas.MUITO_BAIXA.value + MUDA_VINTE)])
        dor_garganta[LabelSintomas.BAIXA.name] = fuzz.trimf(dor_garganta.universe, [LabelSintomas.BAIXA.value - MUDA_VINTE, LabelSintomas.BAIXA.value, LabelSintomas.BAIXA.value + MUDA_VINTE])
        dor_garganta[LabelSintomas.MEDIA.name] = fuzz.trimf(dor_garganta.universe, [LabelSintomas.MEDIA.value - MUDA_VINTE, LabelSintomas.MEDIA.value, LabelSintomas.MEDIA.value + MUDA_VINTE])
        dor_garganta[LabelSintomas.ALTA.name] = fuzz.trimf(dor_garganta.universe, [LabelSintomas.ALTA.value - MUDA_VINTE, LabelSintomas.ALTA.value, LabelSintomas.ALTA.value + MUDA_VINTE])
        dor_garganta[LabelSintomas.MUITO_ALTA.name] = fuzz.trimf(dor_garganta.universe, [ LabelSintomas.MUITO_ALTA - MUDA_DEZ,  LabelSintomas.MUITO_ALTA , LabelSintomas.MUITO_ALTA])

        #febre
        febre[LabelSintomas.NENHUMA.name] = fuzz.trimf(febre.universe,[LabelSintomas.NENHUMA.value, LabelSintomas.NENHUMA.value,(LabelSintomas.NENHUMA.value + MUDA_DEZ)])
        febre[LabelSintomas.MUITO_BAIXA.name] = fuzz.trimf(febre.universe, [LabelSintomas.NENHUMA.value, LabelSintomas.MUITO_BAIXA.value, (LabelSintomas.MUITO_BAIXA.value + MUDA_VINTE)])
        febre[LabelSintomas.BAIXA.name] = fuzz.trimf(febre.universe, [LabelSintomas.BAIXA.value - MUDA_VINTE, LabelSintomas.BAIXA.value, LabelSintomas.BAIXA.value + MUDA_VINTE])
        febre[LabelSintomas.MEDIA.name] = fuzz.trimf(febre.universe, [LabelSintomas.MEDIA.value - MUDA_VINTE, LabelSintomas.MEDIA.value, LabelSintomas.MEDIA.value + MUDA_VINTE])
        febre[LabelSintomas.ALTA.name] = fuzz.trimf(febre.universe, [LabelSintomas.ALTA.value - MUDA_VINTE, LabelSintomas.ALTA.value, LabelSintomas.ALTA.value + MUDA_VINTE])
        febre[LabelSintomas.MUITO_ALTA.name] = fuzz.trimf(febre.universe, [ LabelSintomas.MUITO_ALTA - MUDA_DEZ,  LabelSintomas.MUITO_ALTA , LabelSintomas.MUITO_ALTA])

        #==========================================Possibilidade de Gonorreia==========================================#
        possibilidade_gonorreia[LabelDoencas.NENHUMA.name] = fuzz.trimf(possibilidade_gonorreia.universe,[LabelDoencas.NENHUMA.value, LabelDoencas.NENHUMA.value,(LabelDoencas.NENHUMA.value + MUDA_DEZ)])
        possibilidade_gonorreia[LabelDoencas.MUITO_BAIXA.name] = fuzz.trimf(possibilidade_gonorreia.universe, [LabelDoencas.NENHUMA.value, LabelDoencas.MUITO_BAIXA.value, (LabelDoencas.MUITO_BAIXA.value + MUDA_VINTE)])
        possibilidade_gonorreia[LabelDoencas.BAIXA.name] = fuzz.trimf(possibilidade_gonorreia.universe, [LabelDoencas.BAIXA.value - MUDA_VINTE, LabelDoencas.BAIXA.value, LabelDoencas.BAIXA.value + MUDA_VINTE])
        possibilidade_gonorreia[LabelDoencas.MEDIA.name] = fuzz.trimf(possibilidade_gonorreia.universe, [LabelDoencas.MEDIA.value - MUDA_VINTE, LabelDoencas.MEDIA.value, LabelDoencas.MEDIA.value + MUDA_VINTE])
        possibilidade_gonorreia[LabelDoencas.ALTA.name] = fuzz.trimf(possibilidade_gonorreia.universe, [LabelDoencas.ALTA.value - MUDA_VINTE, LabelDoencas.ALTA.value, LabelDoencas.ALTA.value + MUDA_VINTE])
        possibilidade_gonorreia[LabelDoencas.MUITO_ALTA.name] = fuzz.trimf(possibilidade_gonorreia.universe, [ LabelDoencas.MUITO_ALTA - MUDA_DEZ,  LabelDoencas.MUITO_ALTA , LabelDoencas.MUITO_ALTA])

        # ==============================================================================================================#
        # ============================================= Regras =========================================================#
        # ==============================================================================================================#

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

