# Redes de Computadores 2 - Trabalho Prático

## 📌 **Descrição Geral**
Trabalho prático da disciplina de Redes de Computadores 2, com foco em programação de redes utilizando os protocolos **TCP** e **UDP**. Foram desenvolvidos quatro exercícios que cobrem conceitos de comunicação cliente-servidor, manipulação de threads e criação de um sistema de chat em rede.

---

## 📝 **Exercícios Desenvolvidos**

### **1️⃣ Exercício 1: Cliente-Servidor (TCP)**
- Servidor TCP que aceita múltiplos clientes e responde mensagens recebidas.
- Cliente que envia mensagens e recebe confirmação do servidor.

### **2️⃣ Exercício 2: Servidor Echo (UDP)**
- Servidor UDP que recebe mensagens e devolve o mesmo conteúdo (eco).
- Cliente que envia mensagens e exibe o retorno do servidor.

### **3️⃣ Exercício 3: Chat em Rede (TCP)**
- Sistema de chat em tempo real entre dois clientes, com comunicação bidirecional.

### **4️⃣ Exercício 4: Servidor de Hora com Threads (TCP)**
- Servidor que fornece a hora atual para múltiplos clientes simultaneamente.

---

## ⚙️ **Requisitos para Execução**
- Python 3.10 ou superior
- Sistema Operacional Linux

Para instalar as dependências necessárias:
```bash
sudo apt-get update
sudo apt-get install python3.10
```

## 🐍 **Utilizando Ambiente Virtual (venv)**

Para garantir que todas as dependências do projeto sejam instaladas corretamente e evitar conflitos com outras bibliotecas Python do sistema, recomenda-se o uso de um ambiente virtual.

### 🔧 **Passos para criar e ativar o ambiente virtual**

1. **Crie o ambiente virtual na raiz do projeto:**

   ```bash
   python3 -m venv venv
   ```

2. **Ative o ambiente virtual:**

   * No **Linux/macOS**:

     ```bash
     source venv/bin/activate
     ```

3. **Instale as dependências do projeto:**

   ```bash
   pip3 install -r requirements.txt
   ```

4. **(Opcional) Desative o ambiente virtual após o uso:**

   ```bash
   deactivate
   ```

## 👥 **Integrantes do Grupo**
- Arthur Abreu
- Enzo Veloso
- Josiney Junior

---

## ✔️ **Critérios de Avaliação Atendidos**
- [x] Funcionalidade e correção do programa
- [x] Uso adequado de threads e manipulação de sockets
- [x] Tratamento de erros e validação de entradas
- [x] Clareza e organização do código

---