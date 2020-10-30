# Projeto eHR

Com a chegada da Pandemia, muitas empresas tem procurado obter uma modernização de suas relações internas. Muitas estão adotando o estilo de trabalho Home Office, necessitando de ferramentas para o gerenciamento dos funcionários, para benefício de ambos.

Para este projeto, simulei uma demanda de construção de um sistema de gerenciamento de RH, com recursos que são escalaveis para atendimento de múltiplas empresas.

## Funcionamento do sistema

O sistema atende a várias funções dentro da empresa. Um gerente de RH, pode ter controle sobre criação de funcionario, adição de horas extras, liberação de horas. 

Na modelagem por UML, também projetei uma subaplicação do sistema com padrão REST, que faz comunicação com outro programa que é instalado no computador do usuário, que registra as horas de entrada e saída e realiza o cálculo das horas trabalhadas.