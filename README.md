# NomedoProjeto

**Número do Grupo**: II<br>
**Código da Disciplina**: FGA0208-T01<br>

## Alunos
|Matrícula | Aluno |

| 202402814028 |  Eduardo Parga |<br>
| 202402627287  |  Enzo Rafael |<br>
| 202309057981 | Lukas Souza  |<br>

## Sobre 
O projeto é um programa inovador de monitoramento de atividades físicas que visa transformar a forma como os usuários gerenciam e otimizam sua saúde e bem-estar. Este sistema vai além do simples rastreamento de exercícios, oferecendo uma experiência enriquecida com uma série de recursos adicionais.

Os usuários podem monitorar suas atividades físicas com precisão, acompanhando métricas detalhadas como distância percorrida, velocidade, calorias queimadas e frequência cardíaca. Além disso, o programa inclui uma rede social interna onde os usuários podem se conectar, compartilhar suas conquistas, trocar dicas e apoiar uns aos outros. Para proporcionar um suporte ainda mais personalizado, há treinadores virtuais que criam planos de treino adaptados às necessidades e metas individuais de cada usuário.

O sistema também incentiva a participação em desafios e competições, criando um ambiente motivador e engajador. Os usuários podem competir entre si e participar de desafios que promovem a prática regular de atividades físicas. Para complementar a experiência, o programa oferece uma vasta gama de conteúdos educativos, incluindo artigos, vídeos e tutoriais sobre saúde, nutrição e técnicas de treino, ajudando os usuários a aprimorar seu conhecimento e suas práticas.

A integração com dispositivos vestíveis e sensores permite uma sincronização eficiente dos dados, oferecendo uma visão mais completa do progresso do usuário. A interface do programa é projetada para ser intuitiva e altamente personalizável, garantindo que cada usuário possa adaptar a plataforma às suas preferências e necessidades.

Em resumo, o projeto não apenas monitora e analisa a atividade física, mas também cria uma comunidade envolvente e educativa, promovendo um estilo de vida saudável e sustentável de maneira eficaz e motivadora.

## Screenshots
Adicione 3 ou mais screenshots do projeto em termos de interface e funcionamento.

## Instalação 
**Linguagens**: Python  <br>
**Tecnologias**: Django<br>

# Configuração e Execução do Projeto

## Requisitos

Certifique-se de ter os seguintes itens:

1. **Python**: Versão 3.8 ou superior.
2. **Pip**: Gerenciador de pacotes do Python.
3. **Banco de Dados**: Pode ser SQLite (padrão do Django), PostgreSQL, MySQL, etc.
4. **Ambiente Virtual**: Recomendado usar `venv` ou `virtualenv`.

## Passos para Configuração e Execução

1. **Instalar Python e Pip**

   Certifique-se de que o Python e o Pip estão instalados no seu sistema. Você pode verificar as versões instaladas com os comandos:

   ```bash
   python --version
   pip --version

2. **Clonar o Repositório**
 
git clone https://github.com/Projetos-de-Extensao/PBE_24.2_8002_II_Pandora

3. **Criar e Ativar um Ambiente Virtual**
É recomendável usar um ambiente virtual para gerenciar dependências. Crie e ative o ambiente virtual com os seguintes comandos:

### python -m venv venv
# No Windows: venv\Scripts\activate
# No macOS e Linux: source venv/bin/activate

4. **Instalar Dependências**
Com o ambiente virtual ativado, instale as dependências do projeto listadas no arquivo requirements.txt:

pip install -r requirements.txt

5. **Cinfugurar o Banco de Dados**
Certifique-se de que o banco de dados escolhido está instalado e configurado. Se estiver usando SQLite (padrão do Django), isso não é necessário. Para outros bancos de dados (PostgreSQL, MySQL, etc.), configure as credenciais no arquivo settings.py do Django.

6. **Aplicar Migrações**
Aplique as migrações do banco de dados para criar as tabelas necessárias:

python manage.py migrate

7. **Executar o Servidor de Desenvolvimento**
Inicie o servidor de desenvolvimento do Django:

python manage.py runserver

## Uso 
Explique como usar seu projeto caso haja algum passo a passo após o comando de execução.

## Vídeo
Adicione 1 ou mais vídeos com a execução do projeto final.

## Outros 
Quaisquer outras informações sobre seu projeto podem ser descritas abaixo.
