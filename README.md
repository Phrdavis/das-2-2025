# Design e Arquitetura de Software II

Davi Pinheiro de Souza

    Configurado user e email do github

            git config --global user.name ""
            git config --global user.email ""


## Aula 27/02/2025

### Trade-offs 
   
    Resultado da escolha de ferramentas necessarias para um projeto;

Exemplo:

    + Durabilidade
        Dados duraveis, garantia de permanencia de informação;
        Caracteristicas de sistemas transacionais;

    + Cache
        Memoria temporaria, guardar informações em memória para mais rapidez  na busca dos dados

### Escalabilidade

    Assegurar que uma aplicação consiga se manter mesmo em altos niveis de demandas

Exemplo:

    + Servidor local
        Maior rentabilidade no sentido de gerenciamento fixo

    + Servidor Clound
        Maior segurança e flexibilidade na garantia de escalabilidade


### Automatização

    Automatizar processos e recursos de um sistema 

Exemplo:

    + Aplicação que monitora o estado de servidores para criar alertas;
    + Sistema responsável por recriar maquinas virtuais sozinha;
    + Aplicar recursos necessários para colocar a aplicação online novamente;

### IaC

    Infraestrutura em forma de codigo

    + Reduz falhas por configuração manual;
    + Propaga mudanças e atualizações de forma uniforme;
    + Agilidade na execução e manutenção de aplicações;

### Recursos Descartaveis

    Tratar recursos todos como descartaveis

    + Recursos que podem ser facilmente substituidos;
    + Substituição de recursos mais antigos automaticamente devido a descartabilidade
 
## Aula 06/02/2025

### Componentes Independentes

    Trabalhar com arquiteturas que possuam componentes independentes

    + Componentes com pouco acoplamento
    + Cópias de componentes para perder dependencia 

### Design de Serviços 

    Não limitar infraestruturas a somente servidores, mas também a serviços

    + Utilização de containers
    + Sistemas de mensageria para comunicação em aplicações

### Escolher melhores opções de Soluções de Banco de Dados

    Sempre escolher as opções que melhor se adequam ao seu projeto

    + Opções escalaveis que se adequam a soluções
    + Optar por soluções que tragam melhor performance a longo prazo

### Evitar Pontos Unicos

    Sempre evitar pontos chaves dentro de uma aplicação e optar por soluções que podem ser substituiveis

    + Cópias de banco de dados
    + Backups de Aplicações

### Otimização de Custo

    Avaliar os recursos necessarios para obter os resultados esperados com o menor custo possivel

    + Evitar aplicações robustas para aplicações simples
    + Buscar soluções que otimizem os processos

### Cache

    Minimizar a redundancia de dados em operações

    + Melhorar performance de aplicações usando cache
    + Dados são mais acessíveis e não exigem tanto de requisições

### Segurança

    Garantir a segurança em todas as camadas de uma aplicação

    + Usar serviços gerenciados para melhor segurança
    + Isolar partes da infraestrutura
    + Encryptar os dados de um banco de dados
    + Utilizar de varias formas de autenticação
    + Utilizar varias formas de segurança para os mesmos componentes de uma aplicação


### Selecionar Regiões

    Selectionar sempre a melhor região das zonas de disponibilidade conforme o ponto chave da aplicação

    + Zonas de Disponibilidade (AZ) são areas na qual possuem um numero X de Data Centers
    + Regiões são pontos de AZs 
    
### Local Zone 

    Serviços locais em regiões na qual ainda não possuem serviços AWS

    + Pequenas zonas de disponibilidades dentro de grandes Regiões

### Infraestrutura Global AWS

    + 36    Regiões
    + 114   Zonas de Disponibilidade
    + 700   Pontos de Presença