# Sprint_7
Project developed to accreditate the Sprint 7 of Data Scientist in TripleTen
# 🚗💨 **US Vehicles Market Intelligence Dashboard** 📊✨

> *"Transformando datos complejos del mercado automotriz en decisiones inteligentes y visualizaciones de alto impacto."*

---

## 🌟 **Descripción del Proyecto**

¡Bienvenido a este repositorio! Este proyecto es un **panel de control interactivo de última generación** desarrollado con **Python**, diseñado para explorar, filtrar y analizar a fondo el mercado de vehículos usados en los Estados Unidos.

Como parte de un portafolio de datos profesional, esta aplicación permite a los usuarios interactuar dinámicamente con miles de registros de vehículos, aplicando filtros avanzados en tiempo real (condición, tipo de combustible, tracción 4WD) y visualizando métricas clave a través de gráficos altamente responsivos construidos con Plotly Express.

> **💡 Propósito:** Demostrar habilidades sólidas en ingeniería de datos frontend, diseño de interfaces de usuario analíticas y narración visual de datos (*data storytelling*).

---

## 🛠️ **Tecnologías y Librerías Utilizadas**

El stack tecnológico de este proyecto ha sido seleccionado cuidadosamente para garantizar un rendimiento óptimo, interactividad fluida y una estética profesional:

* 🐍 **[Python](https://www.python.org/):** Lenguaje de programación principal para la lógica y manipulación de datos.
* 🎈 **[Streamlit](https://streamlit.io/):** Framework de código abierto para la creación rápida y elegante de aplicaciones web de datos.
* 🐼 **[Pandas](https://pandas.pydata.org/):** Librería líder para la limpieza, transformación y gestión eficiente de DataFrames.
* 📈 **[Plotly Express](https://plotly.com/python/plotly-express/):** Motor de visualización de gráficos interactivos, estéticos y de alto rendimiento.

---

## 🚀 **Instalación y Configuración Local**

Sigue estos sencillos pasos para clonar este repositorio y ejecutar la aplicación directamente en tu máquina local.

### **Prerrequisitos**

Asegúrate de tener instalado en tu sistema:

* Python (versión 3.8 o superior recomendada)
* `pip` (gestor de paquetes de Python)

### **Paso 1: Clonar el repositorio**

Abre tu terminal y ejecuta el siguiente comando para clonar el proyecto:

```bash
git clone https://github.com/tu-usuario/nombre-del-repositorio.git
cd nombre-del-repositorio

```

### **Paso 2: Instalar las dependencias**

Instala todas las librerías necesarias especificadas en el archivo `requirements.txt`:

```bash
pip install -r requirements.txt

```

*(Nota: Si aún no tienes un archivo `requirements.txt`, puedes crearlo ejecutando `pip install streamlit pandas plotly` y luego `pip freeze > requirements.txt`).*

### **Paso 3: Verificar la estructura de datos**

Asegúrate de que el archivo del conjunto de datos se encuentre en la ruta correcta dentro del proyecto:

```text
tu-repositorio/
│
├── data/
│   └── vehicles_us.csv
├── app.py
└── requirements.txt

```

### **Paso 4: Ejecutar la aplicación**

¡Lanza el servidor de desarrollo local de Streamlit con un solo comando!

```bash
streamlit run app.py

```

Una vez ejecutado, tu navegador predeterminado se abrirá automáticamente mostrando el panel interactivo (generalmente en `http://localhost:8501`).

---

## 🤝 **Contribuciones y Contacto**

¡Las contribuciones, ideas y sugerencias son siempre bienvenidas! Si deseas mejorar este proyecto o adaptarlo a tus necesidades, siéntete libre de hacer un *Fork* y abrir un *Pull Request*.

<sub>Desarrollado con pasión y código limpio 💻✨</sub>