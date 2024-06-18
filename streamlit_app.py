import streamlit as st

def montar_perfil():
    st.title("RELIA")
    st.header("Monte seu perfil")

    nome = st.text_input("Nome")
    idade = st.text_input("Idade")
    local = st.text_input("Local")
    gostos = st.text_area("Gostos")

    aceitar = st.checkbox("Aceito compartilhar meus dados")

    if st.button("Próximo"):
        if aceitar:
            st.session_state["perfil"] = {
                "nome": nome,
                "idade": idade,
                "local": local,
                "gostos": gostos
            }
            st.success("Perfil salvo com sucesso!")
            st.experimental_rerun()

def escolher_obra():
    st.header("Escolha da Obra e Autor")
    
    obra = st.text_input("Obra")
    autor = st.text_input("Autor")
    
    if st.button("Próximo"):
        st.session_state["obra"] = {
            "obra": obra,
            "autor": autor
        }
        st.success("Obra e autor salvos com sucesso!")
        st.experimental_rerun()

def resumo_e_acoes():
    st.header("Resumo e Ações de Interesse")
    
    st.write(f"**Obra:** {st.session_state['obra']['obra']}")
    st.write(f"**Autor:** {st.session_state['obra']['autor']}")
    st.write("**Resumo:** Lorem ipsum dolor sit amet...")  # Exemplo de resumo
    
    st.subheader("Escolha as Ações de Interesse")
    acoes = [
        "Questões intrigantes",
        "Contexto histórico",
        "Impacto cultural",
        "Relações e experiências humanas",
        "Estilo de escrita",
        "Mensagens e morais",
        "Realidade contextual da época"
    ]
    
    acoes_escolhidas = st.multiselect("Selecione as ações:", acoes)
    
    if st.button("Enviar"):
        st.session_state["acoes"] = acoes_escolhidas
        st.success("Ações salvas com sucesso!")
        st.experimental_rerun()

def interacao_llm():
    st.header("Interação com LLM")
    
    pergunta = st.text_area("Pergunta o que quiser sobre a obra")
    
    if st.button("Consultar LLM"):
        resposta = f"Resposta simulada para a pergunta: {pergunta}"  # Aqui seria a chamada real ao LLM
        st.write(resposta)

if "perfil" not in st.session_state:
    montar_perfil()
elif "obra" not in st.session_state:
    escolher_obra()
elif "acoes" not in st.session_state:
    resumo_e_acoes()
else:
    interacao_llm()
