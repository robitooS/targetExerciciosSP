import pandas as pd
import numpy as np

faturamento = pd.read_json('dados.json') # Faturamento da empresa guardado num dataframe
# print(faturamento.head()) Primeiros 5 faturamentos (Noção sobre os dados)


# Menor faturamento, desconsiderando o 0
faturamento_maior_que_0 = faturamento[faturamento['valor'] > 0]
menor_faturamento = faturamento_maior_que_0['valor'].min()

print(f'\nMenor faturamento em um dia do mês R$ {menor_faturamento}')

# Foi criado uma série booleana contendo valores maiores que 0, e selecionando o menor valor 
# da coluna 'valor'

maior_faturamento = faturamento['valor'].max()
print(f'\nMaior faturamento em um dia do mês: R$ {maior_faturamento}\n')

# Calculando a média, desconsiderando dias que o faturamento foi zero
media = np.mean(faturamento_maior_que_0['valor'])
num_dias = len(faturamento_maior_que_0[faturamento_maior_que_0['valor'] > media])

print(f'Número de dias no mês em que o valor de faturamento diário foi superior à média mensal ({media}): {num_dias} dias\n')



