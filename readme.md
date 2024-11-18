# Projeto de Bloco de Fundamento de Dados  
## TP5 - Web Crawling, Web Scraping e Manipulação de Dados em SQL  

### **Introdução**  
Cheguei a mais uma etapa de preparação! Este Teste de Performance (TP) é uma oportunidade para eu praticar os conhecimentos adquiridos em **web scraping**, **web crawling** e **manipulação de dados em SQL**, além de receber feedbacks valiosos para o meu aprendizado.  

Neste TP, vou explorar técnicas de extração de dados de páginas HTML, armazenar os dados extraídos em um banco de dados SQL e aplicar operações de junção para obter insights a partir dos dados coletados.  

---

### **Atividades**  

#### 1. **Web Crawling e Web Scraping**  
Vou baixar e analisar o conteúdo HTML de páginas web específicas, utilizando bibliotecas como `urllib` e `BeautifulSoup` no Python. Vou extrair informações relevantes, como **nome do evento**, **data**, **localização**, e **tipo de evento** (música, teatro, arte, etc.). Quando necessário, aplicarei expressões regulares e criarei uma lógica própria para atribuir informações ausentes, como o tipo do evento.  

#### 2. **Armazenamento em Tabelas SQL**  
Os dados extraídos serão armazenados em um banco de dados SQL. Vou estruturar as tabelas para garantir consistência, incluindo:  
- **Eventos**: contém o ID, nome e tipo do evento.  
- **Dados dos Eventos**: contém o ID, ID do evento, data e localização.  
- **Metadados**: contém o ID, ID do evento e os metadados associados às páginas usadas no scraping.  

#### 3. **Manipulação de Dados em SQL**  
Realizarei consultas SQL diretamente no Python para:  
1. Mostrar todos os eventos com suas datas, localização e tipo de evento.  
2. Mostrar os dados dos dois eventos mais próximos de iniciar.  
3. Listar os eventos que acontecem em Florianópolis.  
4. Listar todos os eventos ao ar livre.  
5. Mostrar todos os metadados por evento.  

#### 4. **Gestão de Exceções e Relatório Final**  
Enquanto desenvolvo o script de scraping, vou tratar exceções para lidar com erros como falhas de conexão, páginas inacessíveis ou inconsistências nos dados.  
Ao final, vou criar um relatório contendo:  
- Prints das páginas web analisadas.  
- Exemplos de código utilizado.  
- Resultados das consultas SQL realizadas.  
- Estruturas das tabelas criadas.  

---

### **Descrição do Problema**  
Escolhi um site público para extrair dados de **eventos culturais**. Meu script será responsável por:  
1. Navegar pelas páginas do site.  
2. Extrair informações específicas, como **nome do evento**, **data**, **localização**, e **tipo de evento**.  
3. Armazenar essas informações em um banco de dados SQL, garantindo a organização e integridade dos dados.  

Se o tipo do evento não estiver explícito no site, aplicarei uma lógica própria para preencher essa informação.  

---

### **Estrutura das Tabelas**  
Definirei três tabelas para organizar os dados extraídos:  
1. **Eventos**:  
   - `id`: identificador único do evento (chave primária).  
   - `nome`: nome do evento.  
   - `tipo`: categoria do evento (ex.: música, teatro, arte).  

2. **Dados dos Eventos**:  
   - `id`: identificador único dos dados do evento (chave primária).  
   - `id_evento`: referência ao evento (chave estrangeira).  
   - `data`: data do evento.  
   - `localizacao`: local onde o evento será realizado.  

3. **Metadados**:  
   - `id`: identificador único do metadado (chave primária).  
   - `id_evento`: referência ao evento (chave estrangeira).  
   - `metadado`: informações adicionais sobre as páginas web utilizadas no scraping.  

Posso ajustar a estrutura dessas tabelas conforme necessário para atender às necessidades do projeto.  

---

### **Consultas em SQL**  
As consultas que realizarei no banco de dados incluem:  
1. Mostrar todos os eventos com suas respectivas datas, localização e tipo de evento.  
2. Mostrar os dois eventos mais próximos de iniciar (baseado na data atual).  
3. Listar os eventos que acontecem no Rio de Janeiro.  
4. Listar os eventos que são realizados ao ar livre.  
5. Mostrar os metadados associados a cada evento.  

---