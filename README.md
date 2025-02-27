# Design e Arquitetura de Software II

Davi Pinheiro de Souza

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
