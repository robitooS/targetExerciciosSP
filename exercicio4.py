faturamento_mensal = {
    'SP':67936.43,
    'RJ':36678.66,
    'MG':29229.88,
    'ES':27165.48,
    'Outros':19849.53 
}

faturamento_mensal_total = round(sum(faturamento_mensal.values()), 2)

# Escreva um programa na linguagem que desejar 
# onde calcule o percentual de representação
# que cada estado teve dentro do valor total mensal
# da distribuidora.  

print(f'\nFaturamento mensal total: {faturamento_mensal_total}\n')

for key, value in faturamento_mensal.items():
    percentual = (value / faturamento_mensal_total) * 100
    
    if key == 'Outros':
        print(f'Percentual de outros estados não listados em relação ao total: {round(percentual, 2)}%\n')
        
    else:
        print(f'Percentual do Estado de {key} em relação ao total: {round(percentual, 2)}%')