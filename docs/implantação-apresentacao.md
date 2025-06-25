# Implantação da solução

Nossa aplicação web tem como finalidade prever os preços de imóveis no **Condado de King** (Washington, EUA), combinando um backend em **Flask** com uma interface moderna e dinâmica construída com **HTMX**, **Alpine.js** e **Tailwind CSS**. O projeto foi publicado como um serviço público na **Azure App Service**, com **integração contínua e deploy automatizado via GitHub Actions**.

## Interface do Usuário e Formulário Interativo

A interface principal da aplicação é composta por um formulário interativo criado com **Alpine.js**, que gerencia o estado da aplicação de forma reativa. Os campos permitem ao usuário inserir atributos de um imóvel, como:

- Tamanho da casa e do lote (em pés²);
- Número de quartos, banheiros e andares;
- Condição, nota de avaliação do imóvel (*grade*) e idade da construção;
- Presença de vista privilegiada ou acesso à orla (*view*, *waterfront*).

Além dos campos estáticos, o formulário também integra um componente de **mapa interativo baseado na API do Google Maps**. O usuário pode clicar em qualquer ponto do mapa, e a aplicação captura automaticamente:

- **Latitude e longitude** do ponto selecionado;
- **CEP (zipcode)** e o **condado (county)** correspondente via geocodificação reversa.

Esses dados geográficos são validados em tempo real: **apenas localizações dentro do Condado de King são aceitas para simulação**, garantindo a integridade e o escopo do modelo de previsão.

## Integração com HTMX e Envio dos Dados

A submissão do formulário ocorre sem recarregamento da página, por meio de uma requisição assíncrona feita com **HTMX**, utilizando:

- `hx-trigger="submit"` para capturar o envio;
- `hx-target="#result"` para renderizar a resposta dinamicamente no frontend.

Antes do envio, Alpine coleta os dados, transforma-os em um objeto JSON e realiza a chamada para o endpoint `/simulate`.

## Backend em Flask com Modelos Serializados

O backend é um servidor **Flask** com uma API REST criada com **Flask-RESTful**. O endpoint `/simulate` aceita requisições POST contendo os dados do imóvel. Esses dados são repassados a uma função de predição que utiliza modelos de aprendizado de máquina previamente treinados e **serializados com `pickle`**.

Os modelos são carregados dinamicamente a partir de arquivos `.pkl` armazenados no servidor, permitindo:

- Rapidez na inferência;
- Facilidade de atualização dos modelos sem alterar a lógica da API.

A resposta do backend consiste em um **HTML parcial** renderizado com os resultados da simulação (ex: valor estimado do imóvel), que é retornado ao frontend para exibição dinâmica.

## Deploy Automatizado no Azure com GitHub Actions

O ciclo de desenvolvimento está integrado ao GitHub, com **deploy automatizado para o Azure App Service** via **GitHub Actions**. O fluxo de CI/CD executa as seguintes etapas:

1. Instala dependências e configura o ambiente Python;
2. Realiza o build e empacotamento da aplicação Flask;
3. Realiza o deploy no **Azure App Service** usando credenciais seguras armazenadas como *secrets* no repositório.

Este processo garante que qualquer alteração na branch principal da aplicação seja automaticamente publicada em produção, promovendo **agilidade, consistência e confiabilidade** na entrega contínua.








