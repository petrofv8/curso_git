import pandas as pd 
import numpy as np 
import streamlit as st

def rd1_question_9(df):
    df_grouped = df[['id', 'seller_type']].groupby('seller_type')

    df_grouped = df_grouped.count().reset_index(df1)

    df_grouped = df_grouped.rename(columns={'id': 'count'})

    df_grouped

    fig= px.bar(
        df_grouped,
        x="seller_type"
        y="count",
        labels{"seller_type":"seller type","count":"Quantity"}

    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig,use_container_width=True)

    return None

def rd1_question_13(df):
    df_grouped = df.groupby('owner').agg(
    qty = pd.NamedAgg('id', 'count')
    ).sort_values('qty').reset_index()

    ax = sns.barplot(
    data=df_grouped,
    x = 'owner',
    y = 'qty'
    )

    ax.bar_label(ax.containers[0])

    ax.set(
    title = 'Quantidade de Motos por tipo de dono',
    xlabel = 'Tipo de Dono',
    ylabel = 'Quantidade de donos'
    )

    return None

def rd1_question_14(df):
    ax = sns.barplot(
    data = df_grouped,
    x = 'km_class',
    y = 'selling_price'
    )

    ax.set(
    title = 'Média de Preço das Motocicletas agrupadas por classe',
    xlabel = 'Classe de Quilemtros percorridos (5 mil Km percorrido por classe)',
    ylabel = 'Preço Médio de venda'
    )
    return None
