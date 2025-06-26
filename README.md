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

    + HPC (High Performance Computing): Recomendado agrupar máquinas na mesma AZ ou até no mesmo rack para reduzir latência.

    + Spread: Estratégia contrária ao HPC, distribuindo instâncias para maior disponibilidade.

    + Partition: Meio-termo — os dados são divididos entre servidores próximos. Usado com Apache Kafka, Cassandra ou Spark.

    + EC2 Free Tier: Gratuito por 12 meses.

## Modelos de EC2:

    + On-Demand: Flexível, mais caro.

    + Reserved: Compromisso de 1 ou 3 anos, mais barato.

    + Saving Plans: Flexível com cobrança por hora.

    + Spot: Usa capacidade ociosa da AWS (pode ser interrompido).

## Aula 10/04/2025

    O que pensar na hora de criar um banco de dados: escalabilidade, espaço necessário pra armazenar, tipo dos dados e quanto tempo eles precisam durar.
    
    + Amazon RDS: serviço da Amazon que gerencia bancos de dados relacionais pra você.
    
    + Amazon DynamoDB, Amazon Neptune e Amazon ElastiCache: são serviços da Amazon que cuidam de bancos de dados não relacionais.
    
    + Amazon Aurora: banco relacional que funciona igual MySQL (só que 5x mais rápido) ou Postgres (3x mais rápido).
    
    + Amazon Aurora Serverless: banco que liga e desliga sozinho conforme a necessidade.

## Aula 17/04/2025

    Connection pooling: melhora a escalabilidade usando um proxy entre a aplicação e o banco, evitando sobrecarregar o servidor com muitas conexões ao mesmo tempo.
    
    + Backups no RDS: tem o backup automático (roda a cada 5 dias, guarda de 7 a 35 dias) e o snapshot manual (que fica guardado pra sempre).
    
    + KMS (Key Management System): sistema que funciona como um cofre para guardar chaves.
    
    + Chave simétrica: mesma chave que criptografa também descriptografa.
    
    + Chave assimétrica: a chave que criptografa é diferente da que descriptografa.
    
    + DynamoDB: banco NoSQL, serverless, que tem uma performance super rápida (milissegundos). Ideal pra arquitetura baseada em eventos, funciona em modo ativo/ativo, tem criptografia automática e usa IAM roles pra controle de acesso.
    
    + Redshift: banco para data warehouse, focado em análises pesadas e dados históricos.
    
    + Outros bancos na AWS: DocumentDB, Keyspaces, MemoryDB, Neptune, Timestream, Quantum Ledger.

## Aula 05/05/2025

    + VPC (Virtual Private Cloud): rede virtual que existe só em uma região, totalmente isolada lá. Dá pra limitar a velocidade do tráfego dentro dela.
    
    + CIDR: tipo a máscara de rede, define o tamanho da rede.
    
    + Subnet pública: recursos nela podem ser acessados pela internet, tanto de dentro pra fora quanto de fora pra dentro.

## Aula 08/05/2025

    Máquinas dentro da VPC que não têm acesso direto à internet não conseguem baixar nada. Pra isso, precisa de uma máquina intermediária (NAT device instance ou NAT gateway).
    
    + Banco de dados geralmente fica em VPC privada.
    
    + Instâncias que processam batch ficam em VPC privada também.
    
    + Instâncias de aplicações web ficam na VPC pública.
    
    + NAT gateway também fica em VPC pública.
    
    + Security group: regra que define quem pode acessar o que.
    
    + Network ACL: valida se a permissão de entrada e saída tá ok.
    
    + AWS Network Firewall: firewall que fica numa subnet especial e controla o tráfego de entrada e saída pra internet.
    
    + VPC flow logs: registros das tentativas de conexão na rede.

## Aula 19/05/2025

    Topologia full mesh: todas as VPCs se comunicam diretamente entre si.

    + Topologia hub and spoke (Shared VPC): tem um hub central com serviços compartilhados que se conecta com todas as outras VPCs.
    
    + Transit Gateway: ajuda a montar essas topologias, é um serviço regional e pago, e pode suportar até 5000 conexões.
    
    + VPC Peering: conecta VPCs entre si; é grátis se as VPCs estiverem na mesma região, mas se forem de regiões diferentes, tem custo.
    
    + Direct Connect: conexão exclusiva feita por um circuito direto entre o servidor da AWS na região e você.
    
## Aula – 26/05

    + IAM Groups: Permite agrupar usuários com permissões semelhantes, facilitando o gerenciamento de políticas de acesso.

    + RBAC (Role-Based Access Control): Controle de acesso baseado em papéis, onde um usuário pode assumir temporariamente uma função com permissões específicas.

    + ABAC (Attribute-Based Access Control): Controle de acesso baseado em atributos (como tags, cargo ou departamento), permitindo regras mais dinâmicas e granulares.

    + Amazon Cognito: Serviço gerenciado para autenticação, autorização e gerenciamento de usuários em aplicações web e mobile.

## Aula – 29/05

    + As empresas podem se organizar na AWS de duas formas:

        - Com uma única conta AWS, utilizando diferentes VPCs para segmentar as equipes.

        - Com múltiplas contas AWS, uma para cada equipe, aumentando a separação e controle.

    + AWS Organizations: Ferramenta para gerenciar múltiplas contas AWS de forma centralizada, ideal para estruturas corporativas mais complexas.

    + A conta root (principal) pode convidar outras contas para compor uma hierarquia organizacional, habilitando recursos como faturamento consolidado (consolidated billing).

    + AWS Control Tower: Solução que automatiza a criação e configuração de ambientes multi-conta com base em boas práticas de segurança, compliance e governança.

    + Em segurança da informação, há um equilíbrio entre três pilares: confiabilidade, integridade e disponibilidade – geralmente, um desses precisa ser flexibilizado para priorizar os outros dois.

    + AWS Key Management Service (KMS): Serviço responsável por criar, armazenar e gerenciar chaves de criptografia para proteger dados.

    + Amazon Macie: Serviço que escaneia automaticamente dados armazenados (como no S3) para identificar informações sensíveis (por exemplo, CPF, cartão de crédito).

    + Amazon Inspector: Ferramenta que realiza análises automatizadas para detectar vulnerabilidades conhecidas em instâncias EC2 e containers no ECR (Elastic Container Registry).

## Aula 02/06/2025

    Funções do monitoramento da aplicação: Saúde operacional, otimização de recursos, performance e segurança.

    + CloudWatch: Ferramenta para coletar, armazenar e analisar métricas da aplicação. Gera métricas padrão e customizáveis, gráficos e alertas.

    + EventBridge: Barramento de eventos, monitoramento em tempo real da AWS.

## Aula 16/06/2025

    + Escalabilidade dos Bancos de Dados na AWS:

        + Aurora: Escala por cluster, tanto vertical quanto horizontal.

        + RDS: Escala por banco, principalmente vertical, com suporte a réplicas de leitura.

        + DynamoDB: Escala horizontal com uso de RCUs e WCUs.

    + ELB (Elastic Load Balancer): Distribui tráfego para múltiplos alvos em uma ou mais AZs, verificando a saúde das máquinas antes de enviar requisições.

        + Tipos de Load Balancer: Application, network, gateway, classic.

    + Route 53: Web service para administrar registros de domínios.

## Aula 23/06/2025

    Infraestrutura em forma de código
        + Benefícios: Produtividade aumentada, escalabilidade, menor taxa de erros;

    + CloudFormation: Ferramenta de criação e automação de recursos de maneira atualizada
    + Drift Detection: Ferramenta de controle de recursos que notifica e até corrige erros de forma automatizada
    + Amazon Q: Uma IA Generativa desenvolvida pela AWS que é responsável por otimização de tarefas e produtividade

## Aula 26/06/2025

    + Load Balancer: É possível utilizar balanceadores de carga para diminuir o acoplamento entre as camadas da aplicação.

    + Modularização: Em vez de adotar uma arquitetura monolítica, dividir a aplicação em módulos ajuda a reduzir o acoplamento entre os componentes.

    + Simple Queue Service (SQS): Serviço de fila de mensagens da AWS que permite múltiplos produtores e consumidores. Cada mensagem é entregue apenas uma vez para um dos consumidores, promovendo escalabilidade e desacoplamento.
    
