# Gestão de Stock

## Português (Portugal)

### Descrição Geral
Este é um sistema simples de gestão de stock baseado em texto, desenvolvido para adicionar, consultar, atualizar e exibir materiais e suas quantidades em stock. Ele utiliza uma interface interativa no terminal.

---

### Funcionalidades Principais
1. **Adicionar Material**:
   - Permite inserir novos materiais ao stock, juntamente com suas quantidades.

2. **Consultar Stock**:
   - Permite verificar a quantidade disponível de um material específico.

3. **Atualizar Stock**:
   - Altera a quantidade de materiais existentes no stock.

4. **Exibir Stock Geral**:
   - Lista todos os materiais disponíveis no stock, com suas respectivas quantidades.

---

### Estrutura do Código
- **Funções Implementadas**:
  - `adicionar_material(stock)`: Adiciona um novo material ao stock ou atualiza a quantidade de um material existente.
  - `consultar_stock(stock)`: Permite consultar a quantidade de um material específico no stock.
  - `atualizar_stock(stock)`: Atualiza a quantidade de um material já registrado.
  - `exibir_stock(stock)`: Exibe todos os materiais e suas respectivas quantidades.
  - `stosk_file()`: Lê e imprime o conteúdo de um arquivo de texto chamado `s.txt` (função de exemplo para integração com arquivos).

- **Menu Interativo**:
  - O menu é implementado dentro da função `main()`, que apresenta opções para o usuário e executa as ações correspondentes com base na escolha.

- **Estrutura de Dados**:
  - Os materiais e suas quantidades são armazenados em um dicionário Python, onde a chave é o nome do material e o valor é a quantidade.

---

### Como Utilizar
1. Execute o programa.
2. Escolha uma das opções apresentadas no menu:
   - **1**: Adicionar um novo material ou atualizar a quantidade de um existente.
   - **2**: Consultar a quantidade de um material específico.
   - **3**: Atualizar manualmente o stock de um material.
   - **4**: Exibir todo o stock disponível.
   - **5**: Encerrar o programa.
3. Siga as instruções no terminal para interagir com o sistema.

---

### Pontos a Melhorar
1. **Persistência de Dados**:
   - Atualmente, os dados são armazenados apenas em memória (no dicionário). Uma melhoria seria integrar leitura e escrita em arquivos (como `s.txt`) para salvar o stock entre execuções.

2. **Validação de Entradas**:
   - Melhorar a validação de entradas para evitar valores inválidos ou entradas incorretas.

3. **Interface Gráfica**:
   - Uma possível expansão seria criar uma interface gráfica ou migrar o sistema para uma aplicação web.

4. **Relatórios**:
   - Adicionar funcionalidades para gerar relatórios de stock, como materiais em baixa quantidade.

---

## English

### Overview
This is a simple text-based stock management system designed to add, check, update, and display materials and their quantities in stock. It uses an interactive terminal interface.

---

### Main Features
1. **Add Material**:
   - Allows adding new materials to the stock along with their quantities.

2. **Check Stock**:
   - Lets you check the available quantity of a specific material.

3. **Update Stock**:
   - Changes the quantity of existing materials in stock.

4. **Display All Stock**:
   - Lists all available materials in stock with their respective quantities.

---

### Code Structure
- **Implemented Functions**:
  - `adicionar_material(stock)`: Adds a new material to the stock or updates an existing material's quantity.
  - `consultar_stock(stock)`: Checks the quantity of a specific material in stock.
  - `atualizar_stock(stock)`: Updates the quantity of an existing material.
  - `exibir_stock(stock)`: Displays all materials and their quantities.
  - `stosk_file()`: Reads and prints the contents of a text file called `s.txt` (example function for file integration).

- **Interactive Menu**:
  - The menu is implemented inside the `main()` function, which presents options to the user and executes corresponding actions based on their choice.

- **Data Structure**:
  - Materials and their quantities are stored in a Python dictionary, where the key is the material name and the value is the quantity.

---

### How to Use
1. Run the program.
2. Choose one of the options from the menu:
   - **1**: Add a new material or update the quantity of an existing one.
   - **2**: Check the quantity of a specific material.
   - **3**: Manually update the stock of a material.
   - **4**: Display all available stock.
   - **5**: Exit the program.
3. Follow the terminal instructions to interact with the system.

---

### Improvement Points
1. **Data Persistence**:
   - Currently, data is stored only in memory (in the dictionary). A potential improvement would be to integrate reading and writing to files (like `s.txt`) to save stock between sessions.

2. **Input Validation**:
   - Improve input validation to prevent invalid values or incorrect entries.

3. **Graphical Interface**:
   - A possible expansion would be to create a graphical interface or migrate the system to a web application.

4. **Reports**:
   - Add functionalities to generate stock reports, such as materials in low supply.
