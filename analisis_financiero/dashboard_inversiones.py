import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine    

# 1. CONFIGURACIÓN DE CONEXIÓN CON TUS DATOS REALES
usuario = "root"
contraseña = "22307706GAS"
host = "localhost"
base_datos = "portafolio"

# Creamos el motor de conexión
engine = create_engine(f'mysql+pymysql://{usuario}:{contraseña}@{host}/{base_datos}')

# 2. CONSULTA ANALÍTICA AJUSTADA A TUS TABLAS EXACTAS
# Corregidos los typos (cantiidad -> cantidad), nombres de tabla (instrumenntos -> portafolio) y las claves del JOIN
query = """
SELECT
    i.ticker AS activo,
    i.tipo_activo AS categoria,
    SUM(m.cantidad * m.precio_compra) AS capital_invertido_USD
FROM movimientos m
JOIN portafolio i ON m.id_instrumento = i.id_instrumento
GROUP BY i.ticker, i.tipo_activo
ORDER BY capital_invertido_USD DESC;
"""

print("☕ Conectando a la base de datos 'portafolio'...")
df_cartera = pd.read_sql(query, engine)

print("\n📊 POSICION VALORIZADA ACTUAL ")
print(df_cartera)

# 3. VISUALIZACIÓN COMPLETA: GRÁFICO DE DONA (Diverisificación)
plt.figure(figsize=(8, 6))
sns.set_theme(style="whitegrid")

# Paleta de colores financieros limpia
colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Dibujamos la torta usando los nombres en minúscula tal cual los devuelve la query
plt.pie(
    df_cartera['capital_invertido_USD'], 
    labels=df_cartera['activo'], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colores, 
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

# Convertimos la torta en Dona agregando el círculo central blanco
centro_blanco = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centro_blanco)

plt.title("Distribución de Capital de Inversión (Diversificación)", fontsize=14, fontweight='bold')
plt.tight_layout()

print("\n Renderizando reporte visual de la cartera...")
plt.show()