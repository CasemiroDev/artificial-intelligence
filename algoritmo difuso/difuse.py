import numpy as np
import skfuzzy
from skfuzzy import control as ctrl
import time

qualidade = ctrl.Antecedent(np.arange(0,11,1),'qualidade')
servico = ctrl.Antecedent(np.arange(0,11,1),'serviço')
gorjeta = ctrl.Consequent(np.arange(0,21,1),'gorjeta')

#Membership function
qualidade.automf(number=3, names=['ruim','média','boa'])
servico.automf(number=3, names=['ruim','médio','bom'])

gorjeta['baixa'] = skfuzzy.sigmf(gorjeta.universe,5,-1)
gorjeta['média'] = skfuzzy.gaussmf(gorjeta.universe,10,3)
gorjeta['alta'] = skfuzzy.pimf(gorjeta.universe,10,20,25,50)

regra1 = ctrl.Rule(qualidade['ruim'] | servico['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule(servico['médio'], gorjeta['média'])
regra3 = ctrl.Rule(servico['bom'] | qualidade['boa'], gorjeta['alta'])

sistema_controle = ctrl.ControlSystem([regra1,regra2,regra3])

sistema = ctrl.ControlSystemSimulation(sistema_controle)

sistema.input['qualidade'] = 9
sistema.input['servico'] = 8
sistema.compute()

print(sistema.output['gorjeta'])
gorjeta.view(sim=sistema)