import json
import numpy as np

# Carrega os dados do JSON
with open('faturamento.json', 'r') as file:
    dados = json.load(file)

# Extrai os valores de faturamento, ignorando dias sem faturamento (valor 0.0)
faturamentos = [dia["valor"] for dia in dados["faturamento_diario"] if dia["valor"] > 0]

# Calcula o menor e o maior valor de faturamento
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

# Calcula a média mensal, ignorando dias sem faturamento
media_mensal = np.mean(faturamentos)

# Conta o número de dias em que o faturamento foi superior à média mensal
dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

# Exibe os resultados
print(f"Menor faturamento ocorrido em um dia do mês: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento ocorrido em um dia do mês: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")