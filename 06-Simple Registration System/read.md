#  Explicação Técnica: Sistema de Cadastro de Pessoas

Este script realiza o cadastro de múltiplos usuários em uma lista de dicionários, aplicando estruturas de validação de dados em loops e utilizando expressões lambda para análise estatística das informações coletadas.

##  Fluxo de Funcionamento

1. **Estrutura de Armazenamento:**
   O programa utiliza uma lista principal chamada `people` para agrupar os dados de todas as pessoas cadastradas.

2. **Loop de Cadastro Coletivo:**
   Através de uma estrutura de repetição `for`, o sistema executa exatamente 5 iterações para coletar os dados de cada indivíduo (Nome, Idade e Cidade).

3. **Validação Robusta de Entrada:**
   A captura da idade é protegida por um loop incremental `while True` combinado com um bloco `try/except`:
   * **`ValueError`**: Caso o usuário insira um caractere textual ou flutuante, o sistema intercepta o erro e solicita a entrada novamente.
   * **Validação Lógica**: Uma condicional `if` verifica se a idade fornecida é menor que zero, impedindo o registro de valores negativos.

4. **Modelagem de Dados:**
   Os dados de cada pessoa são estruturados dentro de um dicionário (`dict`) usando chaves textuais (`"name"`, `"age"`, `"city"`). Esse dicionário é adicionado à lista principal por meio do método `.append()`.

5. **Análise de Dados com Expressões Lambda:**
   Após a coleta, o script utiliza funções nativas do Python integradas a funções anônimas (`lambda`) para varrer a lista com máxima eficiência:
   * **`max()`**: Retorna o dicionário que contém o maior valor numérico associado à chave `"age"`.
   * **`min()`**: Retorna o dicionário que contém o menor valor numérico associado à chave `"age"`.

6. **Mapeamento e Média:**
   O script realiza uma compreensão de lista (*List Comprehension*) para extrair todas as idades, soma os valores com `sum()` e divide pelo total de elementos medidos através da função `len()`.

7. **Saída Formatada:**
   Utilizando a função `enumerate()`, o terminal exibe a lista indexada a partir do número 1 e exibe o bloco informativo contendo a pessoa mais velha, a mais jovem e a média final exata calculada com duas casas decimais.

# English Version

   ##  Technical Explanation: People Registration System

   This script performs the registration of multiple users into a list of dictionaries, applying data validation structures within loops and utilizing lambda expressions for statistical analysis of the collected information.

   ###  Operational Flow

   1. **Storage Structure:**
   The program uses a main list called `people` to group the data of all registered individuals.

   2. **Collective Registration Loop:**
      Through a `for` repetition structure, the system executes exactly 5 iterations to collect the data of each individual (Name, Age, and City).

   3. **Robust Input Validation:**
      The age capture is protected by an incremental `while True` loop combined with a `try/except` block:
      * **`ValueError`**: If the user enters a textual or floating-point character, the system intercepts the error and requests the input again.
      * **Logical Validation**: An `if` conditional checks if the provided age is less than zero, preventing the registration of negative values.

   4. **Data Modeling:**
      The data of each person is structured inside a dictionary (`dict`) using textual keys (`"name"`, `"age"`, `"city"`). This dictionary is added to the main list through the `.append()` method.

   5. **Data Analysis with Lambda Expressions:**
      After collection, the script uses Python's native functions integrated with anonymous functions (`lambda`) to scan the list with maximum efficiency:
      * **`max()`**: Returns the dictionary containing the highest numerical value associated with the `"age"` key.
      * **`min()`**: Returns the dictionary containing the lowest numerical value associated with the `"age"` key.

   6. **Mapping and Average:**
      The script performs a List Comprehension to extract all ages, sums the values using `sum()`, and divides by the total number of measured elements using the `len()` function.

   7. **Formatted Output:**
      Utilizing the `enumerate()` function, the terminal displays the indexed list starting from number 1 and shows the informative block containing the oldest person, the youngest person, and the exact final average calculated to two decimal places.