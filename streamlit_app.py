import streamlit as st

st.title("AutoInfraGPT")
prompt = st.text_input("Enter Infra Command:")
if prompt:
    result = agent.run(prompt)
    st.code(result)
}
