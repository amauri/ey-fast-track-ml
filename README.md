# ey-fast-track-ml
Projeto final do bootcamp EY Dio


![projeto_ey_dio_diagrama](https://user-images.githubusercontent.com/301956/197619006-60f5aed8-c8d6-49a7-913e-874b3a5f9790.png)


## Motivação

Na casa dos meus pais em Cabo Frio, RJ, pombos invadem a casa para comer a ração do cachorro e em alguns casos vão até a cozinha.
Como essa ave transmite diversas doenças, precisamos de uma sistema de monitamento que avisa aos meus pais quando o pombo chegar.

## Detalhes do projeto:

1- Raspberry PI model B com com a PiCamera.
1.1 - Instalção do aplicativo motion(https://motion-project.github.io/)
O aplicativo fica rodando em segundo plano monitorando o ambiente, quando ocorre movimento, uma fotografia é tirada e enviada para a nuvem.

2- VM na OCI(Oracle Cloud Infraestructure) com o ubuntu 22.04 server e Anaconda.

3 - O projeto consite um 2 microserviços:

3.1 - API feita utilizando o framework Flask, onde é realizada a integração com o telegram e foi criado um chatbot que recebe as incrições dos clientes que querem ser notificados quando o pombo invadir o ambiente e um endpoint disponível para enviar as mensagens.

3.2 - um microserviço que vai rodar o tensor flow com um modelo treinado externamente, pois o computador na nuvem é uma maquina com um processador de apenas 1 core com 1 GB de RAM, onde foi inviável realizar o treinamento do modelo.
O modelo consiste em um dataset de imagens de cachorros(imagens aproveitadas do exemplo passando em aula) e imagens de pombos baixadas da internet.

o modelo foi treinado no meu computador pessoal rodando o anaconda onde salvei o modelo para o uso na maquina na nuvem.

OBS.: Falantando configurar o envio da imagem para o algoritimo avaliar se é um pombo ou cachorro, sendo o pombo, será realizada uma requisição a api do telegram para avisa aos clientes.

Acurácia do treinamento:

![results](https://user-images.githubusercontent.com/301956/197621048-587d26e4-5f1b-437c-a848-faff4c78a025.png)



Chatbot do Telegram, onde qualquer um pode realizar a inscrição para o recebimento das notificações:

@EY_Fast_Track_ML_bot


![ey-fast-track-ml_bot_image](https://user-images.githubusercontent.com/301956/197621909-7dd7ea9e-5a0e-4cff-8edb-9cf05a5568e0.jpg)






