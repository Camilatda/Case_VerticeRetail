import streamlit as st
import plotly.express as px
import pandas as pd

# 1. Configuração da Página e Tema
st.set_page_config(page_title="Dashboard Executivo - Vértice Retail", layout="wide", initial_sidebar_state="expanded")

# 2. Sidebar: Resumo Executivo e Alertas (Visibilidade Constante)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2306/2306004.png", width=60) # Placeholder para logo
    st.title("Vértice Retail")
    st.markdown("---")
    st.markdown("### 🚨 Alertas Críticos")
    st.error("**SAC em Colapso:** 35.841 tickets para uma base de 24.000 pedidos.")
    st.warning("**Margem Corroída:** Custo de frete chegando a R$ 60,00 e margens negativas em categorias-chave.")
    st.warning("**Balde Furado:** 51% da base de clientes em risco ou churn.")
    st.markdown("---")
    st.caption("Atualizado: Setembro 2026")

# 3. Cabeçalho Principal
st.title("📊 Painel de Controle Estratégico")
st.markdown("Diagnóstico de gargalos operacionais e oportunidades de otimização de margem.")
st.markdown("---")

# 4. Abas de Navegação
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💰 Finanças", 
    "📈 Aquisição", 
    "👥 Retenção (RFM)", 
    "📦 Operação", 
    "🎧 Atendimento"
])

# ==========================================
# ABA 1: Margem e Finanças
# ==========================================
with tab1:
    st.subheader("Saúde Financeira e Margens")
    col1, col2, col3, col4 = st.columns(4)
    
    # Adicionando deltas para dar noção de impacto direcional
    col1.metric("Receita Líquida (Moda)", "R$ 6.24M", "Motor de Caixa", delta_color="normal")
    col2.metric("Margem de Contribuição (Moda)", "42,82%", "Top Categoria", delta_color="normal")
    col3.metric("Margem Mínima Registrada", "R$ -49,27", "Alerta Vermelho", delta_color="inverse")
    col4.metric("Custo de Frete (Teto)", "R$ 60,00", "Corrosão de Margem", delta_color="inverse")
    
    st.info("💡 **Insight:** A receita bruta mascara um vazamento de caixa severo causado por fretes desbalanceados e margens negativas em produtos de cauda longa.")

# ==========================================
# ABA 2: Aquisição e Canais de Marketing
# ==========================================
with tab2:
    st.subheader("Eficiência de Aquisição")
    col1, col2, col3 = st.columns(3)
    sub_col_a, sub_col_b = col1.columns(2)
    
    sub_col_a.metric("CAC Mínimo", "R$ 0,37", delta="Alta Volatilidade", delta_color="off")
    sub_col_b.metric("CAC Máximo", "R$ 82,33", delta="Alta Volatilidade", delta_color="off")
    col2.metric("ROAS Médio", "4.14", "Mínimo bate 0.53", delta_color="inverse")
    col3.metric("Campanhas Ativas", "523", "Redução de 3.500 iniciais", delta_color="normal")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    df_canais = pd.DataFrame({
        "Canal": ["Marketplace", "Google Ads", "Instagram Ads"],
        "Pedidos": [6040, 5505, 4965]
    })
    
    # Gráfico mais limpo e direto
    fig_canais = px.bar(
        df_canais, x="Pedidos", y="Canal", orientation='h',
        text="Pedidos", color="Canal", 
        color_discrete_sequence=["#3498db", "#9b59b6", "#e74c3c"],
        title="Volume de Transações por Canal (Top 3)"
    )
    fig_canais.update_traces(textposition='outside')
    fig_canais.update_layout(showlegend=False, xaxis_title="", yaxis_title="", template="plotly_white")
    st.plotly_chart(fig_canais, use_container_width=True)

# ==========================================
# ABA 3: Comportamento e Retenção (RFM)
# ==========================================
with tab3:
    st.subheader("Matriz RFM e Cenário de 'Balde Furado'")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.error("**O Problema:** Alta dependência de atração de novos clientes combinada com uma baixíssima taxa de recompra.")
        st.metric("Clientes Inativos/Em Risco", "6.993", "62% da base analisada", delta_color="inverse")
    
    with col2:
        df_clientes = pd.DataFrame({
            "Segmento": ["Promissor", "Em Risco", "Hibernando", "Churn"],
            "Quantidade": [4127, 3269, 1928, 1796]
        })
        fig_clientes = px.pie(
            df_clientes, names="Segmento", values="Quantidade", hole=0.5,
            color="Segmento",
            color_discrete_map={"Promissor":"#2ecc71", "Em Risco":"#f1c40f", "Hibernando":"#e67e22", "Churn":"#e74c3c"}
        )
        fig_clientes.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig_clientes, use_container_width=True)

# ==========================================
# ABA 4: Operação e Logística
# ==========================================
with tab4:
    st.subheader("Gargalos Logísticos e Rupturas")
    col1, col2, col3 = st.columns(3)
    col1.metric("Volume de Devoluções", "4.127", "14,8% do total de pedidos", delta_color="inverse")
    col2.metric("SKUs em Estoque Crítico", "701", "Risco Iminente", delta_color="inverse")
    col3.metric("Ruptura Absoluta", "99 SKUs", "Perda direta de venda", delta_color="inverse")
    
    df_devolucoes = pd.DataFrame({
        "Motivo": ["Defeito (Fornecedor)", "Tamanho Errado (Grade)"],
        "Volume": [1039, 1025]
    })
    
    fig_devolucoes = px.bar(
        df_devolucoes, x="Motivo", y="Volume", 
        text="Volume", color="Motivo",
        color_discrete_sequence=["#e74c3c", "#f39c12"],
        title="Principais Indutores de Devolução (Impacto direto no CAC e Logística)"
    )
    fig_devolucoes.update_layout(showlegend=False, xaxis_title="", yaxis_title="", template="plotly_white")
    st.plotly_chart(fig_devolucoes, use_container_width=True)

# ==========================================
# ABA 5: Atendimento (SAC)
# ==========================================
with tab5:
    st.subheader("Experiência do Cliente (CSAT: 3.24/5.0)")
    
    # Destaque visual forte para o maior ofensor
    st.error("⚠️ **Diagnóstico:** A ausência de comunicação proativa de rastreio transformou o SAC em um centro de custos altamente inflamado.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Tickets Abertos", "35.841", "Supera os 24k pedidos", delta_color="inverse")
    col2.metric("Custo por Ticket", "R$ 14,85", "Chegando a R$ 45,00", delta_color="inverse")
    col3.metric("Tempo de 1ª Resposta", "Até 24h", "Ideal < 2h", delta_color="inverse")
    
    st.markdown("### Maior Ofensor do SAC")
    st.info("📍 **'Onde está meu pedido?'** gerou **10.765 tickets** de forma isolada. A implementação de réguas de comunicação no WhatsApp resolveria este gargalo quase que integralmente.")