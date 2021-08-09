# Apresentação

Olá! Tudo bem por aí?! Meu nome é Matheus Maia, estudante de ciência de dados, engenheiro físico. 

Estou completando o final do curso/bootcamp de DataScience aplicada da Alura e este é o espaço que desenvolvi para o projeto final do curso: desenvolver um modelo capaz de prever, 
através de dados do hospital Sírio Libanês, se um paciente com covid precisa ser internado e ir para a UTI.

# Motivação

A transmissão gerada pelo coronavírus virou pandemia e impactou o mundo todo. Muito se ouviu falar que uma das maiores preocupações é com o sistema de saúde não suportar a
grande quantidade de pessoas infectadas precisando de cuidados médicos. De fato, só agora depois de um tempo considerável do início da campanha de vacina no Brasil, é que o 
sistema público conseguiu se estabilizar mais. Mesmo assim, alguns estados ainda possuem uma alta porcentagem de leitos ocupados, gerando preocupação em todos sobre a capacidade
dos hospitais de tratar a doença de tantas pessoas.

Com essa preocupação que o **hospital Sírio Libanês**, de São Paulo, lançou um projeto no [kaggle](https://www.kaggle.com/S%C3%ADrio-Libanes/covid19), desafiando cientistas de
dados e pesquisadores em geral. O desafio é usar os dados fornecidos pelo hospital para conseguir prever o tratamento de futuros pacientes que chegassem. Eles deverão ser 
internados ou não? Com essa previsão, o Sírio Libanês pode se preparar melhor para receber pacientes na UTI.

# Sobre o projeto

O projeto desenvolvido conta com 2 notebooks: um de exploração dos dados, usando vários conhecimentos aprendidos no decorrer do curso, e outro para o desenvolvimento e validação do modelo de machine learning. No primeiro notebook, `analise_exploratoria.ipynb`, o intuito é entender a representatividade dos dados e como as informações se distribuem no dataframe disponibilizado pelo hospital. Entendido isso, é feito um tratamento e preparação desses dados, de acordo com regras estabelecidas pelo desafio no kaggle. Com os dados tratados e preparados, chega a parte do segundo notebook: `desenvolvimento_de_modelo.ipynb`. Ele tem como objetivo encontrar um bom modelo que consiga fazer a predição desejada. Para isso é utilizado conhecimentos de validação de modelos como matriz de confusão e acurácia.

A utilização dos dados para treino e teste dos modelos teve o seguinte objetivo:

- utilizar ao máximo os dados fornecidos pelo Sírio Libanês;
- não utilizar dados que foram retirados possivelmente depois do paciente ter sido internado;
- excluir dados que não contribuem para o modelo, como identificação do paciente.

# Resultados

O melhor modelo encontrado no projeto foi o **Random Forest**, com uma acurácia de 0.73 em média para 10 modelos rodados com validação cruzada. É um resultado bem razoável para o que se espera do projeto, mas que obedece a todas as especificações estipuladas. Verificou-se durante o tratamento de dados e testes que não foi uma boa escolha retirar muitas features com bastante correlação entre si. 

Além disso, retirar muitos dados para manter as especificações do projeto acabou deixando o dataset com poucas linhas (poucos pacientes com dados válidos), o que prejudica na obtenção de um modelo que consiga interpretar bem as variáveis independetes que determinam se um paciente precisará ser internado ou não. De 385 pacientes inicialmente que forneceram dados, o dataframe utilizado para preparação do modelo acabou ficando com apenas 294 pacientes válidos.

# Projeções

O projeto no entanto pode ser melhorado em vários pontos, se destacando:

- procurar outras formas de se utilizar os dados fornecidos pelo Sírio Libanês;
- estudar melhor a influência de cada variável na predição do resultado (os testes de sangue e os sinais vitais não foram analisados separadamente);
- procurar por outros modelos de machine learning que se adequem melhor, mas principalmente
- explorar mais os hiperparâmetros dos modelos já utilizados, buscando pela melhor configuração do modelo.
