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

## Aula 13/03/2025

### Autenticação

    Confirmar minha identidade. O que eu sei (usuário e senha), o que eu sou (biometria) e o que eu possuo (chave de segurança).

    + Usuário é uma forma de autenticação.

    + Sempre ativar a autenticação multifatorial (MFA).

    + Rotacionar regularmente as credenciais e chaves de acesso de longo prazo.

    + Armazenar as credenciais de forma segura.

    + Evitar o uso do usuário root para tarefas que podem ser realizadas por outros usuários.

    + A primeira ação ao usar o usuário root deve ser habilitar a autenticação multifatorial (MFA).

### Acesso Programático

    Uma Role fornece uma chave de acesso temporária, permitindo que o usuário execute ações específicas enquanto a chave permanecer válida.


## Aula 17/03/2025

### RBAC Role Base Access Control
    
    Permissões definidas de acordo com o seu papél na empresa/sistema

### IAM Policies and Permissions

    Policies e Permissões fornecidas, quais usuários podem acessar determinados recursos ou até mesmo quais recursos podem ser acessados

### Determining Permissions at the Time of Request

    Determina todas as policies de determinado usuário a um recuros para analisar 
    as permissões determinadas fornecidas pelo administrador

    + Condition: Condição para permitir/recusar determinadas ações mesmo possuindo/não possuindo permissão

### Types Of Storage (EBS - EFS, FXs - S3)

    Tipos de Armazenamento de dados na AWS

    + Block Storage: Armazenamento por blocos, ou seja, os dados são armazenados em partes fixas de blocos.
    + File Storage (File Share): Armazenamento em arquivo, armazenamento por uma estrutura de hierarquia.
    + Object Storage: Armazenamento em Objeto, dados atribuidos por atributos e metadados (Tags)

### Amazon S3

    Um dos serviços mais famosos da AWS

    + Virtualmente Limitado: Atualmente não possuem limite de estrutura, porém é limitado por 5TB por objeto/arquivo
    + Objetos possuem globalmente URLs unicas (Namespace Universais)
    + Objetos possuem Key, Version ID, Value, Metadata e Subresources
    + Prefixos: Formas de aplicar estrutura de arquivos dentro do Bucket, mesmo que essa estrutura de fato não exista dentro do S3


## Aula 24/03/2025

### Ciclo de Vida S3 (Lifecycle Polices)

    Regras que definem ações para determinado  grupo de objetos

    + Transição de classes:Mudança entre classes de armazenamento
    + Ações de Expiração: Expirar arquivos que não são mais necessários

### S3 Versionamento

    Proteção de objetos contra sobreescritas de objetos 

    + Após habilitar o versionamento, não é possível desabilitar, pois ao habilitar essa função, já é criado uma nova versão de um objeto

### Cross Origin Suport

    Proteção para arquivos e sites de compartilhamento e comunicação na rede

    
### Data Consistency Model

    S3 sempre irá trabalhar de forma consistência em tempo excepcional

### Cryptografia de Objetos 

    O S3 trabalha sempre com cryptografia
   
    + Server side: O backend é criptografado e é responsabilidade do S3
    + Client side: frontend é responsabilidade do cliente/Usuário


## Aula 27/03/2025

### Amazon Costs

    + Pay for what you use: Somente paga pelos recursos q estão sendo consumidos
    + No change for data transfer
    + Testes com Python e Conexão com Bucket S3


## Aula 03/04/2025

### EC2 
    
    Elastic compute Cloud, permite criar e hospedar sistemas de software com capacidade computacional redimencionável;

    + Serve para qualquer coisa que necessite de um servidor;

    + AMI, uma "foto" do servidor, permitindo criar cópias idênticas do servidor original. Serve para recuperação e repetição;

### EBS 
    
    Armazenamento persistente na EC2, diferente da instance store no host, que só armazena arquivos temporariamente;

    + Quanto menos gerenciado, mais controle:

    + (menos gerenciado) Vms, Containers, VPS, PaaS, Serverless (mais gerenciado);

### Compute optimizer 

    IA que recomenda recursos de computação da AWS mais eficientes para workloads, tem versão gratuita e paga;

### File share

    Usar FSx para Windows, EFS para Linux;


## Aula 07/04/2025

Instance Metadata: Funciona como uma API REST acessível apenas dentro da AWS, usada para obter informações que o servidor precisa.

HPC (High Performance Computing): Recomendado agrupar máquinas na mesma AZ ou até no mesmo rack para reduzir latência.

Spread: Estratégia contrária ao HPC, distribuindo instâncias para maior disponibilidade.

Partition: Meio-termo — os dados são divididos entre servidores próximos. Usado com Apache Kafka, Cassandra ou Spark.

EC2 Free Tier: Gratuito por 12 meses.

Modelos de EC2:

On-Demand: Flexível, mais caro.

Reserved: Compromisso de 1 ou 3 anos, mais barato.

Saving Plans: Flexível com cobrança por hora.

Spot: Usa capacidade ociosa da AWS (pode ser interrompido).


