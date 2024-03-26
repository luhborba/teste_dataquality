"""Arquivo de Interface Visual."""
import pandas as pd
import streamlit as st

from schema import ContratoFuncionarios


def validar(file):
    """
    Função responsável pela validação do arquivo em formato csv de acordo com o contrado de dados.

    Args:
        file: Arquivo csv enviado no streamlit no file uploader.
    """
    try:
        df = pd.read_csv(file)
        erros = []

        for idx, row in df.iterrows():
            try:
                ContratoFuncionarios(**row.to_dict())
            except Exception as e:
                erros.append(f"Linha {idx+2}: {e}")

        if erros:
            st.error("Erros encontrados no seu arquivo CSV:")
            for erro in erros:
                st.error(erro)
        else:
            st.success("Arquivo Validado com Sucesso!!!")
    except Exception as e:
        st.error(f"Erro ao ler o arquivo CSV: {e}")


def main():
    """Função principal que chama a interface visual para validação do arquivo csv de acordo com o contrato de dados."""
    st.set_page_config(
        page_title="Validação de CSV", page_icon=":bar_chart:", layout="wide"
    )

    st.title("Validação de CSV - DataQuality")

    csv = st.file_uploader("Selecione o arquivo CSV", type=["csv"])

    botao = st.button("Validar")

    if botao:
        validar(csv)


if __name__ == "__main__":
    main()
