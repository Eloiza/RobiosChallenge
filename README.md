# RobiosChallenge :robot:

## Descrição
Este é um desafio proposto pela Human Robotics para implementar um programa para a triagem de Covid-19 na entrada de um estabelecimento. Ao final da triagem o resultado deve ser enviado por meio do protocolo `MQTT`.

Esta solução foi implementada inteiramente em Python. O arquivo `form.py` implementa funções para interagir com os clientes, processar a resposta obtida e envia-la através do protocolo `MQTT`. Para realizar a triagem, o programa utiliza como base os dados do arquivo `Data/sympstoms.csv`. Nele há três campos: 

- `symptom_name`: nome do sintoma; 
- `probability`: probabilidade de ocorrer em infectados com Covid-19 no Brasil;
- `question`: pergunta atrelada ao sintoma. 

O campo probabilidade foi baseado nos dados encontrados em dois artigos cientificos que relatam a situação da Covid-19 no Brasil. Esses artigos estão referenciados no final deste arquivo README.md.

O arquivo `subscriber.py` implementa um inscrito que irá receber a mensagem enviada pelo `form.py`. Este foi implementado para fim de teste do protocolo `MQTT` e utiliza o `localhost` como broker.

## Dependências
Para executar o código deste repositório é necessário ter instalado as bibliotecas `pandas` e `paho-mqtt`. A `pandas` é responsável pela manipulação do arquivo `.csv` e a biblioteca `paho-mqtt` é responsável por lidar com o procolo `mqtt`. Ambas podem ser instaladas usando os comandos abaixo.

##### Instalando a biblioteca Pandas
```
pip install pandas
```


##### Instalando a biblioteca Paho-Mqtt

```
pip install paho-mqtt
```

## Executando o código

Para executar o código deste repositório siga os passos:

1. Em um terminal inicie o `subcriber.py` para que ele possa ouvir ao formulário que o foi enviado.
```
python3 subscriber.py
```
2. Em outro terminal inicie o `form.py` para executar o código responsável por gerar o questionário da triagem.
```
python3 form.py
```
E está tudo pronto :smile:!

## Referências

- de Souza, W.M., Buss, L.F., Candido, D.d.S. et al. Epidemiological and clinical characteristics of the COVID-19 epidemic in Brazil. Nat Hum Behav 4, 856–865 (2020). https://doi.org/10.1038/s41562-020-0928-4

- Teich VD, Klajner S, Almeida FAS, Dantas ACB, Laselva CR, Torritesi MG, Canero TR, et al. Epidemiologic and clinical features of patients with COVID-19 in Brazil. einstein (São Paulo). 2020;18:eAO6022. https://doi.org/10.31744/einstein_journal/2020AO6022
