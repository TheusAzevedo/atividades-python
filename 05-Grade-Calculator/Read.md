# 📊 Explicação Técnica: Calculadora de Média

Este script realiza o processamento de notas acadêmicas de um aluno individual, validando as entradas de dados e aplicando estruturas condicionais para definir o status final.

## 📁 Fluxo de Funcionamento

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