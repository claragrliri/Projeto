qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0

TOTAL_ENTREVISTADOS = 10

print('---- PESQUISA DE SATISFAÇÃO DO ATENDIMENTO ----\n')

for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f'--- Entrevistado {i} de {TOTAL_ENTREVISTADOS}')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))

    print('Qual sua opinião sobre o atendimento?')
    print('1 - EXCELENTE')
    print('2 - BOM')
    print('3 - RUIM')

    opiniao = int(input('Sua opção (1, 2 ou 3): '))

    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 2:
        qtd_bom += 1
    elif opiniao == 3:
        qtd_ruim += 1

print('=' * 30)
print('RESULTADO DA PESQUISA')
print('=' * 30)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'BOM': {qtd_bom}")
print(f"c) Quantidade de respostas 'RUIM': {qtd_ruim}")
