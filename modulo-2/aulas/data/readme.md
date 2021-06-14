Aqui você encontra arquivos que foram gerados pelos notebooks das aulas para uso em notebooks posteriores. Por isso a nomenclatura deles começar com "out", indicando que 
foram saídas geradas pelos códigos. Pelo menos em sua maioria, são arquivos em .csv para gerar dataframes.
Uma breve descrição deles:

+ `out_populacao` = dados da população de cada UF do país extraídos [desta página da wikipédia](https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_popula%C3%A7%C3%A3o).
Quando foram extraídos, a estimativa era de 2020.

+ `out_ordenado_por_total` = dados de gastos em internações pelo SUS para cada UF. São semelhantes aos dados de gastos [deste repositório](https://github.com/matheus97eng/Bootcamp_Alura_2021/tree/main/modulo-1/projeto_final/dados), 
mas aqui eles estão mais desatualizados, sendo o último mês de registro em Julho de 2020.

+ `out_gastos_2020-Jul` = os mesmos valores de gastos da tabela acima, porém somente com os valores do mês de Julho de 2020.

+ `out_gastos_e_populacao_2020-Jul` = as informações da tabela de cima mais as informações da tabela `out_populacao`

+ `out_mensal_aberto` = informação dos gastos, onde os dados são separados pelas colunas data, UF, Região, gastos e gastos em milhões.
