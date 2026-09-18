# Projeto Vértice: Consultoria Estratégica e IA Aplicada ao Varejo D2C

## 📋 Sobre o Projeto
Este repositório contém a solução completa desenvolvida para o **Case Projeto Vértice** do Bootcamp EloGroup. O objetivo central foi atuar como uma consultoria para diagnosticar as causas da deterioração da rentabilidade na "Vértice Retail" (um e-commerce focado no público jovem) e propor soluções de alto impacto financeiro e operacional para os próximos 90 dias, utilizando análise de dados e Inteligência Artificial.

## 📁 Estrutura do Repositório
* **`CaseBootcamp_AnaliseDados.ipynb`**: Notebook de perfilamento de dados e análise exploratória (EDA) cruzando bases de vendas, clientes, estoque, marketing e atendimento.
* **`ClassificadorInteligenteAtendimento.ipynb`**: Protótipo funcional offline simulando a integração com um LLM para triagem e roteamento estratégico de tickets do SAC.
* **`dashboard_vertice.py`**: Painel executivo interativo construído em Streamlit, focado no monitoramento de KPIs de finanças, retenção (Matriz RFM), operações e aquisição.
* **`artefato_triagem_ia.md`**: Evidência estruturada da validação do classificador de IA no tratamento de solicitações como o ofensor logístico WISMO ("Onde está meu pedido?").
* **Documentos Estratégicos**: Relatórios contemplando a pesquisa de mercado, diagnóstico operacional, Business Case com cálculo de ROI/Payback e o Roadmap de implementação em fases de 30-60-90 dias.

## 💡 Principais Descobertas (Diagnóstico)
1. **A Ilusão do ROAS vs. A Realidade da CM3**: O alto volume de tráfego de canais de marketing mascara uma Margem de Contribuição 3 (CM3) negativa devido aos altos custos de frete e descontos agressivos no portfólio.
2. **O Ralo Operacional Pós-Venda**: Um volume crítico de 4.127 devoluções corrói a margem do negócio, impulsionado predominantemente por falhas como "Tamanho errado" e "Produto com defeito".
3. **O Falso Atraso e o Colapso do SAC**: O SAC concentra cerca de 30% da sua fila (10.765 tickets) apenas em dúvidas transacionais de logística, mascarando clientes de alto valor com risco real e imediato de *churn*.

## 🤖 Solução Proposta
A principal intervenção recomendada é a implantação de um **Classificador Inteligente de Atendimento N1**. Através da orquestração de um LLM com prompts rigidamente formatados em JSON, a IA identifica a intenção do cliente, calibra o risco de *churn* e analisa o sentimento da interação.
* **Impacto Estimado:** O *Business Case* elaborado aponta um ROI de 622% e *payback* em menos de 2 meses, protegendo mais de R$ 1 milhão em receita vitalícia (LTV) ao desviar tickets transacionais e priorizar os clientes mais valiosos para o Nível 2 humano.

## 🛠️ Tecnologias Utilizadas
* **Análise e Tratamento de Dados:** Python, Pandas.
* **Visualização de Dados e Dashboards:** Plotly, Streamlit.
* **Inteligência Artificial:** Engenharia de Prompt e Saídas Estruturadas (Google Gemini).

## 👨‍💻 Sobre a Autoria
Este repositório materializa a união entre a sólida base analítica desenvolvida no curso de Ciência da Computação da Universidade Federal de Ouro Preto (UFOP) e a visão prática na construção de aplicações inteligentes alavancada pela vivência como Embaixador Estudantil Google Gemini. Desenvolvido como resolução do estudo de caso Projeto Vértice durante o bootcamp da EloGroup, o foco do projeto vai além da escrita de código, entregando uma solução consultiva de ponta a ponta: do diagnóstico minucioso de gargalos operacionais até a proposição de um plano de ação escalável que gera impacto financeiro real.
