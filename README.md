# Huella Ambiental

Este proyecto es una aplicación web desarrollada con Django para calcular y concientizar sobre la huella ambiental en el entorno universitario.

## Requisitos previos
- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- (Opcional) Entorno virtual recomendado

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Jhon98E/huella-ambiental.git
   cd huella-ambiental
   ```

2. **Crea y activa un entorno virtual (opcional pero recomendado):**
   - En Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - En Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realiza las migraciones de la base de datos:**
   ```bash
   python manage.py migrate
   ```

5. **Ejecuta el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

6. **Accede a la aplicación:**
   Abre tu navegador y ve a `http://127.0.0.1:8000/`

## Estructura del proyecto
- `consumo_universitario/`: Aplicación principal con modelos, vistas, plantillas y archivos estáticos.
- `huella_ambiental/`: Configuración principal del proyecto Django.
- `requirements.txt`: Lista de dependencias del proyecto.
- `manage.py`: Script de administración de Django.
