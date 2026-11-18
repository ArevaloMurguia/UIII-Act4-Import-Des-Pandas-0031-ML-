
import pandas as pd
import matplotlib.pyplot as plt

# Arevalo Rafael NC:0031

# 1. Crear diccionario con datos de personal medico
personal_medico = {
    'id_empleado': [201, 202, 203, 204, 205, 206],
    'nombre': ['Dr. Ruiz', 'Dra. Lopez', 'Enf. Garcia', 'Dr. Martinez', 'Enf. Torres', 'Dra. Sanchez'],
    'especialidad': ['Cardiologia', 'Pediatria', 'General', 'Neurologia', 'Urgencias', 'Dermatologia'],
    'tipo_contrato': ['Tiempo completo', 'Tiempo completo', 'Medio tiempo', 'Tiempo completo', 'Turnos', 'Por consulta'],
    'anos_experiencia': [15, 8, 3, 20, 5, 12],
    'consultorio': [101, 102, 105, 103, 100, 104],
    'salario_mensual': [45000, 42000, 18000, 55000, 22000, 38000],
    'pacientes_atendidos_mes': [120, 95, 200, 80, 150, 110],
    'calificacion_pacientes': [4.8, 4.9, 4.5, 4.7, 4.6, 4.9],
    'vacaciones_pendientes': [5, 10, 2, 0, 4, 8]
}

print("Análisis Exploratorio de Datos EDA")
print("Exploratory Data Analysis Por Arevalo Rafael NC:0031")
print("5. Crear el diccionario con 10 listas y 6 elementos")

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(personal_medico)

print("\n--- TABLA ORIGINAL DE PERSONAL MEDICO ---")
print(df)

# 3. Exportar los datos a CSV
print("+-+-+ Convertir el DataFrame en archivo CSV -+-+-+-")
df.to_csv(
    'personal_medico_0031.csv',
    index=False,
    encoding='utf-8-sig'
)

print("\n✅ Archivo CSV creado correctamente")

print("+-+- 8. Leer los datos desde el archivo CSV +-+-+")
print("personal_medico_0031.csv")

# 4. Leer el archivo CSV
df = pd.read_csv('personal_medico_0031.csv')

print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)

print("+-+-+- 9. Análisis Exploratorio de Datos (EDA) +-+-+-")

# 5. Primeros y últimos registros
print("+-+-+- \n1. PRIMEROS REGISTROS (Head): +-+-+-")
print(df.head(3)) # Muestra los primeros 3

print("+-+-+- \n2. ÚLTIMOS REGISTROS (Tail): +-+-+-")
print(df.tail(2)) # Muestra los últimos 2

# 6. Dimensiones y estructura
print("+-+-+-+ 6. Dimensiones y estructura -+-+-+-")
print(df) # Mostrar tabla o matriz

print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)

print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)

print("\n5. TIPOS DE DATOS:\n", df.dtypes)

print("\n6. INFORMACIÓN GENERAL:")
df.info()

# 7. Estadísticas y limpieza
print("\n+-+-+-+ 7. ESTADÍSTICAS DESCRIPTIVAS: +-+-+-+-")
print(df.describe())

print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())

print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())

print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())

print("Especialidades únicas:", df['especialidad'].unique())

# 8. Análisis específico
print(df)

print("-----------------------------------------------------------------------")

print("\n11. PERSONAL MEDICO POR ESPECIALIDAD:")
print(df['especialidad'].value_counts())

print("\n12. PROMEDIO DE SALARIO: $", df['salario_mensual'].mean())

print("13. SALARIO MÁXIMO: $", df['salario_mensual'].max())

print("14. SALARIO MÍNIMO: $", df['salario_mensual'].min())

# 9. Ordenamiento, filtrado y agrupación
print(" 9. Ordenamiento, filtrado y agrupación")

print("+-+-+- \n15. PERSONAL ORDENADO POR SALARIO (Mayor a menor): +-+-+-+")
print(df.sort_values(by='salario_mensual', ascending=False))

print("\n16. PERSONAL CON SALARIO MAYOR A $30,000:")
filtro = df[df['salario_mensual'] > 30000]
print(filtro)

print("\n17. RESUMEN POR ESPECIALIDAD:")
resumen = df.groupby('especialidad').agg(
    empleados=('id_empleado', 'count'),
    salario_promedio=('salario_mensual', 'mean'),
    salario_maximo=('salario_mensual', 'max')
)

print(resumen)

# 18. Gráfica de barras: Personal por especialidad
print("18. Gráfica de barras: Personal por especialidad")

conteo = df['especialidad'].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Personal por especialidad Arevalo Rafael 0031')
plt.xlabel('Especialidad')
plt.ylabel('Cantidad de empleados')
plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Salarios por empleado
plt.figure(figsize=(8, 5))
plt.bar(df['nombre'], df['salario_mensual'], color='lightgreen')
plt.title('Salario mensual del personal medico EDA por Rafael 0031')
plt.xlabel('Personal medico')
plt.ylabel('Salario en pesos')
plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de años de experiencia
plt.figure(figsize=(8, 5))
plt.hist(df['anos_experiencia'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de experiencia del personal medico EDA Rafael 0031')
plt.xlabel('Años de experiencia')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Experiencia vs Salario
plt.figure(figsize=(8, 5))
plt.scatter(df['anos_experiencia'], df['salario_mensual'], color='red', s=100)
plt.title('Relación entre experiencia y salario EDA por Rafael 0031')
plt.xlabel('Años de experiencia')
plt.ylabel('Salario mensual')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de salarios
plt.figure(figsize=(7, 5))
plt.boxplot(df['salario_mensual'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de salarios (Boxplot) EDA Rafael 0031')
plt.ylabel('Salario mensual')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)

print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas EDA Rafael 0031')
plt.tight_layout()
plt.show()
