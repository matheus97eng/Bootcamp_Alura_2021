import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def preenche_tabela(dados):
  # preenche dados faltantes com dados das janelas posteriores e anteriores (respectivamente)
  features_continuas_colunas = dados.iloc[:, 13:-2].columns
  features_continuas = dados.groupby("PATIENT_VISIT_IDENTIFIER", as_index=False)[features_continuas_colunas].fillna(method='bfill').fillna(method='ffill')
  features_categoricas = dados.iloc[:, :13]
  saida = dados.iloc[:, -2:]
  dados_finais = pd.concat([features_categoricas, features_continuas, saida], ignore_index=True,axis=1)
  dados_finais.columns = dados.columns
  return dados_finais

def remove_janela(dados, janela):
  # remove as linhas onde ICU = 1 na janela especificada como parâmetro `janela` da função
  remover = dados.query('WINDOW == @janela and ICU == 1')['PATIENT_VISIT_IDENTIFIER'].values
  dados = dados.query('PATIENT_VISIT_IDENTIFIER not in @remover')
  return dados

def prepare_window(rows):
  # verifica, para cada paciente, todas as linhas aonde ICU = 1. Caso isso seja verificado para qualquer uma delas,
  # o valor de ICU para a primeira janela, '0-2', é colocado como = 1. Por fim a função retorna a linha dessa primeira
  # janela.
  if(np.any(rows["ICU"])):
    rows.loc[rows["WINDOW"]=="0-2", "ICU"] = 1
  return rows.loc[rows["WINDOW"] == "0-2"]

def limpeza_aula_1(dados):
  # faz a limpeza do dataframe retirado do repositório de acordo com o que foi feito na aula 1 do módulo 5
  
  dados_limpos = preenche_tabela(dados)
  
  dados_limpos = remove_janela(dados_limpos, '0-2')
  
  # removendo o restante de dados faltantes
  dados_limpos = dados_limpos.dropna()
  
  # pegando somente as informações das 2 primeiras horas, se esse paciente foi para a UTI ou não
  dados_limpos = dados_limpos.groupby("PATIENT_VISIT_IDENTIFIER").apply(prepare_window)
  
  # separando AGE_PERCENTIL em categorias para não ter dados do tipo string
  dados_limpos.AGE_PERCENTIL = dados_limpos.AGE_PERCENTIL.astype("category").cat.codes
  
  return dados_limpos
  
def prepara_treino_teste(dados_limpos, seed=73246):
  # separa o dataframe já tratado em variável dependente e independente, além de variável de treino e de teste
  # para ser reprodutível, é usada uma determinada semente que define como a função train_test_split fará a 
  # aleatpriedade. É possível mudar a semente com o parâmetro seed, mas por padrão o valor de seed é o mesmo
  # utilizado nas aulas do curso

  x_columns = dados_limpos.columns
  y = dados_limpos["ICU"]
  x = dados_limpos[x_columns].drop(["ICU","WINDOW"], axis=1)
  np.random.seed(seed)
  return train_test_split(x, y, stratify=y) #retorna x_train, x_test, y_train e y_test, nessa ordem
