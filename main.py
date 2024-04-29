from functions import *
# from functions import home, datos, cargar_datos, menu_filtros
#st.beta_expander ahora es expander
# Este es mi script



#Este comando configura el layout de la pagina que vamos a desplegar.
st.set_page_config(page_title='Cargatron', layout='wide', page_icon=':battery:')
#Creamos un titulo para el body de la apliacaion.
st.title('Puntos de carga para coches electricos.')
#Cargamos una data concreta.
data = pd.read_csv('data/red_recarga_acceso_publico_2021.csv', sep = ';')
#Celebramos con globitos, pero para que no los saque constantemente, miramos si la funcion varia algo.
@st.cache_resource
def baloons():
    st.balloons()
baloons()
#Vamos a hacer un menu para que el usuario cambie.
with st.sidebar:
    opcion = st.selectbox('Seleccione una opción de menú', ['Home', 'Datos', 'Filtros'])
    #Le damos al usuario a cargar una data que el quiera.
    uploaded_file = st.file_uploader("Sube un archivo .csv", type= ['.csv'])
#Le pasamos los parametros para que se apliquen nuestros filtros.   
if opcion == 'Home':
    home(data=data)
elif opcion == 'Datos':
    datos(data = data)    
else:
    with st.sidebar:
        filtro = st.selectbox('Seleccione un opcion de filtro', ['Distrito', 'Operador'])
    if filtro == 'Distrito':
        distrito(data=data)
    elif filtro == 'Operador':
        operador(data = data)





