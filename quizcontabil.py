import os


def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, o Balanço tem como função demonstrar a situação financeira e patrimonial da empresa, detalhando o que a empresa possui entre bens, direitos e obrigações.{os.linesep}')
    if resposta == '2':
        print(f'{os.linesep}{nome}, a Demonstração do Resultado do Exercício é elaborado para que se demonstre as operações realizadas dentro do período que agregaram rendimentos ou gastos para a empresa. A DRE serve também para o apuramento dos impostos, principalmente o Imposto de Renda, além de saber se a empresa obteve lucro ou prejuízo no período.{os.linesep}')
    if resposta == '3':
        print(f'{os.linesep}{nome}, a Demonstração dos Fluxos de Caixa é responsável pelas entradas e saídas de dinheiro, durante o período, no caixa da empresa. A conta caixa já deve aparecer no Balanço Patrimonial, porém apenas com o seu valor final.{os.linesep}')
    if resposta == '4':
        print(f'{os.linesep}{nome}, este demonstrativo tem como função apresentar as alterações no patrimônio líquido, ou seja, o quanto aumentou ou diminuiu a "riqueza" da organização durante o período. A DMPL já possui integrada a Demonstração dos Lucros ou Prejuízos Acumulados (DLPA), uma demonstração mais simplificada apenas para as alterações que levaram ao lucro da organização.{os.linesep}')
    if resposta == '5':
        print(f'{os.linesep}{nome}, a Demonstração do Valor Adicionado tem como objetivo evidenciar a criação de riqueza durante o período, e a forma que ela foi distribuída. O que a DVA faz é detalhar de que forma essa riqueza foi distribuída entre funcionários, fornecedores, agentes financiadores, acionistas e governo, ou seja, entre todos os setores que participaram, diretamente ou indiretamente, da sua geração.{os.linesep}')
    else:
        ('Digite apenas 1, 2, 3, 4 ou 5')


def start():
    # Apresentar o quiz
    print('Olá, bem-vindo ao Quiz Contábil!') 
    # pedir o nome
    nome = input('Digite seu nome: ')
    while True:
        # Oferer o menu de opções
        resposta = input(
        f'Quais são os conceitos das Demonstrações Contábeis abaixo que gostaria de saber?{os.linesep}[1] - O que é Balanço Patrimonial? {os.linesep}[2] - O que é a Demonstração de Resultado do Exercício (DRE)?{os.linesep}[3] - O que é a Demonstração do Fluxo de Caixa (DFC)?{os.linesep}[4] - O que é a Demonstração das Mutações do Patrimônio Líquido (DMPL)?{os.linesep}[5] - O que é a Demonstração do Valor Adicionado (DVA)?{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()

    
