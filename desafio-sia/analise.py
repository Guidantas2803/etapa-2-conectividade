import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

1
data = pd.read_csv('caminho_do_arquivo.csv')  


print("Estatísticas Descritivas:")
print(data.describe())

#  Piauí vs. Nacional
# Calcular a média 
ibc_medio_nacional = data['ibc'].mean()

#  dados do Piauí 
piauí_data = data[data['sigla_uf'] == 'PI']
ibc_medio_estadual = piauí_data['ibc'].mean()

# Comparar
if ibc_medio_estadual < ibc_medio_nacional:
    print(f"O IBC médio do Piauí ({ibc_medio_estadual:.2f}) está abaixo da média nacional ({ibc_medio_nacional:.2f}).")
else:
    print(f"O IBC médio do Piauí ({ibc_medio_estadual:.2f}) está acima da média nacional ({ibc_medio_nacional:.2f}).")

# Identificar os "desertos digitais" no Piauí (sem a coluna 'nome')
desertos_digitais = piauí_data[['id_municipio', 'ibc']].sort_values(by='ibc').head(5)
print("Desertos Digitais no Piauí:")
print(desertos_digitais)


# Selecionar as colunas numéricas
numerical_cols = ['ibc', 'cobertura_pop_4g5g', 'fibra', 'densidade_smp', 'densidade_scm']
corr_matrix = data[numerical_cols].corr()

#  matriz de correlação
print("Matriz de Correlação:")
print(corr_matrix)


plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
plt.title('Matriz de Correlação')
plt.show()
