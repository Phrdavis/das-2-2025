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

## Aula 10/03/2025

### AWS Pops

    Pontos de presença (Data Centers) especializados em busca de conteudo de forma mais rapida

    + Edge Location: Servidores desenhaos para entregar dados com a menor latencia possvel
    + Regional Cache: Data center que se encontram entre as edge locations e os destinos

### Securing Access - *Topicos de Prova*

    Segurança básica de usuário, permissões de acesso e restrição de conteudo

### Modelo de Responsabilidade Compartilhada

    + IaaS - Infraestrutura como Serviço
        A responsabilidade é compartilhada entre Cliente/Usuário e Provedor do Serviço

    + S3 - Serviço de Software ( Saas/PaaS )
        Responsabilidade ainda é compartilhada, porém as maiores responsabilidades ficam nas mãos o provedor do serviço

### Design Principals for Security

    Principios para o pilar de segurança em aplicações

    + Implementar uma forma e armazenar identificações de forma mais segura
    + Proteção de dados em transito
    + Aplicação de segurança em todas as camadas de uma aplicação
    + Manter os usuários longe dos dados
    + Possuir rastreabilidade, saber as ações de usuários dentro de aplicações 
    + Se preparar para eventos de segurança (Ataques, vulnerabilidades...)
    + Automatizar práticas de segurança paa evitar cometer erros ao criar/editar manualmente

### User Permission to Accessa Resources

    Permissão que determinado grupo de usuários possuem, onde dita o que um usuario pode ou não fazer/acessar detro de um sistema

### Principle of least privilege

    + Garantir que usuario possua o nivel de privilegio necessario para acessar o sistema com os recursos necessarios

### Use cryptografia

    Não trafegar codigos/dados abertos na internet

### IAM - Identity and Access Manegement


## Aula 17/03/2025

### 
