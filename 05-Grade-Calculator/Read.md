#  Explicação Técnica: Calculadora de Média

Este script realiza o processamento de notas acadêmicas de um aluno individual, validando as entradas de dados e aplicando estruturas condicionais para definir o status final.

##  Fluxo de Funcionamento

1. **Captura de Identificação:** 
   O programa inicia coletando o nome do estudante através de uma entrada de texto convencional.

2. **Captura e Validação de Notas:** 
   São solicitadas três notas sequenciais. O código envolve essa etapa em uma estrutura `try/except` com a exceção `ValueError`. Caso o usuário digite letras ou caracteres inválidos no lugar dos números, o programa barra a execução imediatamente com uma mensagem de erro, impedindo falhas críticas no cálculo.

3. **Processamento Aritmético:** 
   As três notas coletadas são somadas e divididas por 3 para obter a média aritmética simples. O resultado numérico é formatado para exibir apenas duas casas decimais no relatório final.

4. **Análise Condicional (Regra de Status):** 
   O script avalia o valor da média calculada utilizando blocos `if/elif/else`:
   * **`average >= 7`**: Define o status como **Approved** (Aprovado).
   * **`average >= 5`** (e menor que 7): Define o status como **Remedial** (Recuperação).
   * **Qualquer valor abaixo de 5**: Define o status como **Failed** (Reprovado).

5. **Saída de Dados:** 
   Uma interface em bloco de texto é gerada no terminal, exibindo de forma organizada o nome do aluno, a média final com precisão decimal e a situação final calculada.

# English Version

   ## Technical Explanation: Grade Average Calculator

   This script processes the academic grades of an individual student, validating data inputs and applying conditional structures to define the final status.

   ###  Operational Flow

   1. **Identification Capture:** 
   The program begins by collecting the student's name through a conventional text input.

   2. **Grade Capture and Validation:** 
   Three sequential grades are requested. The code wraps this step in a `try/except` structure with the `ValueError` exception. If the user types letters or invalid characters instead of numbers, the program immediately halts execution with an error message, preventing critical failures in the calculation.

   3. **Arithmetic Processing:** 
   The three collected grades are summed and divided by 3 to obtain the simple arithmetic average. The numerical result is formatted to display only two decimal places in the final report.

   4. **Conditional Analysis (Status Rule):** 
      The script evaluates the calculated average value using `if/elif/else` blocks:
      * **`average >= 7`**: Sets the status to **Approved**.
      * **`average >= 5`** (and less than 7): Sets the status to **Remedial**.
      * **Any value below 5**: Sets the status to **Failed**.

   5. **Data Output:** 
   A text block interface is generated in the terminal, cleanly displaying the student's name, the final average with decimal precision, and the calculated final status.
