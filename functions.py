import streamlit as st
import pandas as pd
from PIL import Image

def home(data):
    #Cargamos una imagen.
    st.image('./img/puntos-recarga-madrid.jpg')
    #Creamos una descripcion.
    with st.expander('Leer mas'):
        st.write('Aqui vemos unos coches muy bonitos, que estan pues en reposo, mientras cargan, porque claro cada dia hay mas y mas coches electricos, y se necesitan mas puntos de carga, y esta muy bien tener informacion de donde estan situados.')
    #Mostramos el codigo que hay que ejcutar para ver los datos, ademas de que lo ejecuta.
    with st.echo():
        st.dataframe(data)

def datos(data):
    #Vamos a representar un mapa.
    st.map(data,latitude='latidtud', longitude='longitud')
    #Vamos a mostrar un bar chart
    d_distrito = data.groupby(['DISTRITO'], as_index = False).sum()
    d_operador = data.groupby(['OPERADOR'], as_index = False).sum()
    st.bar_chart(d_distrito, x = 'DISTRITO', y = 'Nº CARGADORES')
    st.bar_chart(d_operador, x = 'OPERADOR', y = 'Nº CARGADORES')

def distrito(data):
    with st.sidebar:
        dist = data.groupby('DISTRITO', as_index = False).count()
        selected_dist = st.selectbox('Elige un distrito', dist['DISTRITO'])
        
    distrito = data[data['DISTRITO'] == selected_dist]
    st.map(distrito,latitude='latidtud', longitude='longitud')
    st.bar_chart(distrito, x = 'DISTRITO', y = 'Nº CARGADORES')

def operador(data):
    with st.sidebar:
        cargadores = data.groupby(['Nº CARGADORES'], as_index = False).count()
        numero_cargadores = st.select_slider('Filtra por numero de cargadores',cargadores['Nº CARGADORES'])
    estaciones = data[data['Nº CARGADORES'] == numero_cargadores]
    st.map(estaciones,latitude='latidtud', longitude='longitud')
