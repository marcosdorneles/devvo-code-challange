# 💍 Desafio Fullstack: Os Anéis de Poder

_One Challenge to rule them all, One Challenge to find them, One Challenge to bring them all, and in the darkness bind them_

## 📜 Contexto do Desafio

O grande mago J.R.R. Tolkien nos deixou a famosa frase:

> **Three Rings for the Elven-kings under the sky,  
> Seven for the Dwarf-lords in their halls of stone,  
> Nine for Mortal Men doomed to die,  
> One for the Dark Lord on his dark throne  
> In the Land of Mordor where the Shadows lie.  
> One Ring to rule them all, One Ring to find them,  
> One Ring to bring them all, and in the darkness bind them  
> In the Land of Mordor where the Shadows lie.**

Sua missão será criar um **CRUD** para gerenciar os anéis e desenvolver um **frontend** para visualizar e manipular essas informações.

---

## 🎯 Objetivo

### **Backend (Django)**
Criar uma API em **Django** para realizar as seguintes operações:

- **Criar** (POST) um novo anel.
- **Listar** (GET) todos os anéis.
- **Atualizar** (PUT) as informações de um anel.
- **Deletar** (DELETE) um anel existente.

### **Frontend (HTML, CSS, JS, Bootstrap)**
Desenvolver uma interface simples com as seguintes telas:

- **Tela de Criação/Atualização**: Formulário para criar um novo anel ou atualizar um anel existente.
- **Tela de Visualização**: Exibição dos anéis criados em um **carrossel**, mostrando as informações de cada anel (nome, poder, portador, forjadoPor e imagem).

---

## ⚔️ Requisitos Funcionais

### **Backend (Django e PostgreSQL)**

1. **Criar um Anel**  
   O anel deverá ter as seguintes propriedades:
   - `nome`: Nome do anel (ex: "Narya, o anel do fogo").
   - `poder`: Uma breve descrição do poder do anel (ex: "Seu portador ganha resistência ao fogo").
   - `portador`: O nome do portador atual (Ex: Gandalf).
   - `forjadoPor`: Quem forjou o anel (ex: Elfos).
   - `imagem`: URL de uma imagem genérica do anel.

2. **Regras de Negócio para Criação de Anéis**  
   A API deverá garantir que a quantidade máxima de anéis criados respeite as seguintes regras:
   
   - **Elfos**: No máximo **3** anéis.
   - **Anões**: No máximo **7** anéis.
   - **Homens**: No máximo **9** anéis.
   - **Sauron**: Apenas **1** anel.

   Caso o limite seja excedido, a criação deve ser rejeitada com uma mensagem de erro adequada.

3. **Listar os Anéis**  
   A API deverá retornar uma lista com todos os anéis e suas propriedades.

4. **Atualizar um Anel**  
   Deve ser possível atualizar as informações de um anel específico (ex: alterar o portador ou a descrição do poder).

5. **Deletar um Anel**  
   Deve ser possível remover um anel do banco de dados.

---

### **Frontend (HTML, CSS, JS, Bootstrap)**

1. **Tela de Criação/Atualização de Anel**  
   - Um formulário com os seguintes campos:
     - `nome`: Campo de texto para o nome do anel.
     - `poder`: Campo de texto para a descrição do poder do anel.
     - `portador`: Campo de texto para o nome do portador.
     - `forjadoPor`: Campo de texto para indicar quem forjou o anel.
     - `imagem`: Como a imagem será genérica, pode-se permitir que o usuário escolha entre imagens pré-definidas ou usar uma imagem padrão.
   - Botões para:
     - **Criar**: Submeter o formulário para criar um novo anel.
     - **Atualizar**: Alterar as informações de um anel existente.

2. **Tela de Visualização dos Anéis**
   - Exibir todos os anéis em um **carrossel** (ou grid), mostrando:
     - Nome, poder, portador, forjadoPor, e a imagem do anel.
   - O carrossel deve ser **responsivo** e permitir rolar entre os anéis cadastrados.
   - Adicionar a possibilidade de **excluir** ou **editar** um anel diretamente dessa tela.

---

## 🚀 Tecnologias Utilizadas

- **Backend**:
  - **Django** (Framework Web)
  - **Django REST Framework** (Para criar a API)
  - **PostgreSQL** (Banco de dados)
  - **Django ORM** (Para manipulação dos dados)

- **Frontend**:
  - **HTML, CSS, JavaScript**
  - **Bootstrap** (Para estilização e responsividade)
  - **Fetch API** (Para consumir a API)

---

## 🛠️ Instruções para Rodar o Projeto

### **Backend (Django)**
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/desafio-aneis-poder.git

