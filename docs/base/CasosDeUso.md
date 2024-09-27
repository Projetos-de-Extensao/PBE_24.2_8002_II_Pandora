# Requisitos Funcionais

## Integração com Dispositivos
1. **Objetivo**: Garantir a coleta e processamento preciso dos dados das atividades físicas realizadas pelos usuários.
2. **Atores**: 
   - Usuário
   - Dispositivos de medição (ex: relógios inteligentes)
3. **Pré-condições**: 
   - O dispositivo de medição deve estar emparelhado com o aplicativo.
   - O usuário deve ter permitido o acesso aos dados do dispositivo.
4. **Trigger**: 
   - O início de uma atividade física (natação, corrida, ciclismo).
5. **Fluxo Principal**:
   1. O usuário inicia uma atividade física no aplicativo ou no dispositivo.
   2. O dispositivo coleta os dados de desempenho (ex: batimentos cardíacos, distância, tempo).
   3. O aplicativo processa e exibe os dados em tempo real para o usuário.
   4. Ao fim da atividade, o aplicativo armazena o histórico da sessão.
6. **Fluxos Alternativos**:
   - **Fluxo Opcionais**: O usuário pode visualizar uma comparação com atividades anteriores.
   - **Fluxo Variante**: Diferentes dispositivos podem enviar dados adicionais, como níveis de oxigênio ou sono.
   - **Fluxo de Exceção**: Se o dispositivo perder a conexão, o aplicativo tenta reconectar ou notifica o usuário para reiniciar a conexão.
7. **Pós-condições**: 
   - O histórico de desempenho da atividade é salvo no perfil do usuário.
8. **Regras**: 
   - O aplicativo deve verificar a compatibilidade do dispositivo e seu estado de bateria.

---

## Precisão no GPS
1. **Objetivo**: Melhorar a exatidão dos dados de localização e percurso.
2. **Atores**: 
   - Usuário
   - Sistema de GPS
3. **Pré-condições**: 
   - O GPS do dispositivo deve estar ativado e funcional.
4. **Trigger**: 
   - O início de uma atividade que requer rastreamento (ex: corrida, ciclismo).
5. **Fluxo Principal**:
   1. O usuário inicia o rastreamento da atividade.
   2. O GPS captura dados de localização e percurso com precisão.
   3. O aplicativo exibe o trajeto em um mapa em tempo real.
   4. Ao final da atividade, o percurso é salvo.
6. **Fluxos Alternativos**:
   - **Fluxo Variante**: O usuário pode revisar o percurso em diferentes níveis de zoom.
   - **Fluxo de Exceção**: Caso a precisão do GPS caia, o aplicativo tenta recalibrar ou notifica o usuário.
7. **Pós-condições**: 
   - O trajeto completo e preciso é salvo no histórico.
8. **Regras**: 
   - O aplicativo deve garantir o mínimo de desvio possível na precisão do GPS, considerando margens de erro aceitáveis.

---

# Requisitos Esperados

## Funcionalidades de Rede Social
1. **Objetivo**: Promover a interação social e a motivação entre os usuários.
2. **Atores**: 
   - Usuário
   - Outros membros de grupos ou assessorias esportivas
3. **Pré-condições**: 
   - O usuário deve estar inscrito em um grupo ou assessoria esportiva.
4. **Trigger**: 
   - Um membro do grupo conclui uma atividade ou compartilha uma atualização.
5. **Fluxo Principal**:
   1. O usuário visualiza as atividades dos outros membros do grupo.
   2. O usuário pode reagir ou comentar nas atividades.
   3. As reações/comentários são salvos e exibidos em tempo real.
6. **Fluxos Alternativos**:
   - **Fluxo Opcional**: O usuário pode ativar notificações para ser informado quando outros membros completarem atividades.
7. **Pós-condições**: 
   - As interações sociais (comentários/reações) são registradas no perfil do usuário.
8. **Regras**: 
   - O aplicativo deve garantir que apenas membros autorizados visualizem e interajam com atividades.

---

## Atualizações e Novidades por Email
1. **Objetivo**: Manter os usuários informados sobre melhorias e novas funcionalidades do app.
2. **Atores**: 
   - Usuário
   - Sistema de envio de email
3. **Pré-condições**: 
   - O usuário deve estar inscrito para receber emails.
4. **Trigger**: 
   - O aplicativo ou seus desenvolvedores lançam uma atualização ou notícia relevante.
5. **Fluxo Principal**:
   1. O usuário opta por receber atualizações por email.
   2. O sistema envia notificações periódicas de novidades.
   3. O usuário recebe o email e pode acessar informações adicionais.
6. **Pós-condições**: 
   - O usuário está informado sobre as últimas novidades do aplicativo.

---

# Requisitos Excitantes

## Estreitamento de Relações entre Membros
1. **Objetivo**: Fomentar uma comunidade engajada e conectada.
2. **Atores**: 
   - Usuário
   - Membros de grupos esportivos
3. **Pré-condições**: 
   - O usuário deve fazer parte de um grupo.
4. **Trigger**: 
   - Criação de fóruns, desafios ou competições amistosas.
5. **Fluxo Principal**:
   1. O grupo organiza desafios ou fóruns de discussão.
   2. O usuário participa, comentando ou competindo.
   3. O aplicativo registra o progresso do desafio ou fórum.
6. **Fluxos Alternativos**:
   - **Fluxo Opcionais**: O usuário pode criar seus próprios desafios dentro de grupos menores.
7. **Pós-condições**: 
   - O grupo se fortalece com as interações e desafios realizados.

---

## Personalização Avançada
1. **Objetivo**: Oferecer uma experiência rica e adaptada às preferências individuais.
2. **Atores**: 
   - Usuário
3. **Pré-condições**: 
   - O usuário deve configurar suas preferências no aplicativo.
4. **Trigger**: 
   - O usuário acessa a área de personalização.
5. **Fluxo Principal**:
   1. O usuário ajusta o perfil e as metas no aplicativo.
   2. O aplicativo oferece recomendações e feedback personalizados.
6. **Fluxos Alternativos**:
   - **Fluxo Variante**: As metas podem ser ajustadas dinamicamente com base no desempenho do usuário.
7. **Pós-condições**: 
   - As metas e feedbacks são atualizados e adaptados à evolução do usuário.

---

# Requisitos Não Funcionais

## Desempenho
1. **Objetivo**: Garantir eficiência e ausência de atrasos significativos.
2. **Atores**: 
   - Usuário
   - Servidor do aplicativo
3. **Pré-condições**: 
   - O aplicativo deve ser executado em dispositivos compatíveis.
4. **Trigger**: 
   - A utilização de grandes volumes de dados ou funcionalidades complexas.
5. **Fluxo Principal**:
   1. O usuário utiliza o aplicativo sem interrupções ou atrasos, mesmo com grandes volumes de dados.
6. **Pós-condições**: 
   - O aplicativo mantém um desempenho estável.

---

## Segurança e Privacidade
1. **Objetivo**: Proteger informações sensíveis e garantir a privacidade dos usuários.
2. **Atores**: 
   - Usuário
   - Sistema de segurança do aplicativo
3. **Pré-condições**: 
   - O usuário deve ter um login seguro.
4. **Trigger**: 
   - O usuário acessa ou envia dados sensíveis.
5. **Fluxo Principal**:
   1. O sistema valida as credenciais do usuário.
   2. O aplicativo criptografa e protege os dados armazenados.
6. **Pós-condições**: 
   - Os dados do usuário estão seguros e protegidos.
