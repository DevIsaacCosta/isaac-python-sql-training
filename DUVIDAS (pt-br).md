# duvida 01
No main review foi colocado
    "Single quotes are preferred over double quotes, besides for single characters"
Mas no seu pull request foi alterado o single quotes que eu tinha adicionado pra double quotes, eu nao sei se foi algum lint que fez isso automaticamente?

# duvida 02
No caso de
    "Multiline comments should be defined by triple quotes"
Seria tambem single quotes?

# duvida 03
Eu deveria ter criado um documento para adicionar o meu pensamento 'passo a passo' ao inves de ter jogado dentro do codigo, mas fiquei em duvida sobre se seria uma alternativa a esse ponto.
    "We can define at the top of the file a docstring with a short description" e
    "Prefer docstrings over comments on the file root level"

# duvida 04
    "Avoid saving rounded values that will be used as sources"
Eu não entendi exatamente o motivo de ter surgido esses valores que eu senti a necessidade de arredondar, pois eu dei um view na tabela sales que eu gerei e não notei numeros quebrados com mais de 2 casas depois da virgula, dai eu fiquei com a impressao de que fosse aqueles problemas de variaveis que sendo convertidas ou mesmo armazenadas, eu já li sobre umas problemas similares, por isso acabei utilizando o arredondamento.

Minha duvida é se voce sabe me dizer o motivo de ter acontecido isso?

# duvida 05
    Notei depois de analizar o projeto que deu inicio a esse que em todas as solucoes voce utiliza no nome fact_xxx e dim_xxx para salvar os nomes das tabelas que voce gera.
    Isso foi só para exemplo por conta do projeto ser um estudo do star schema ou é realmente um padrao que voce (ou todo mundo) gosta de manter?

# duvida 06
    No ponto que voce adicionou suas notas no Olap Cube onde o state nao faria diferença, num SELECT DISTINCT porque na tabela big o resultado da consulta se manteria.
    É correto falar que isso acontece apenas porque as lojas nesse caso estão cadastradas por um ID individual? E em um exemplo onde por algum motivo as lojas estivessem salvas pelo nome da loja e existisse o caso de lojas em estados diferentes possuirem o mesmo nome dai faria diferença e por conta disso seria necessario considerar uma granularidade maior para esse caso para garantir a integridade do resultado?
