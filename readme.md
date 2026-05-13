# 🚀 Infraestructura de Servidores Jocarsa
### Despliegue Híbrido: Apache + Flask Proxy Inverso

Este repositorio contiene la configuración y arquitectura para el despliegue de microservicios en un entorno de producción Linux. La arquitectura utiliza **Apache** como servidor principal y **Flask** como motor de aplicaciones dinámicas detrás de un **Proxy Inverso**.

---

## 📂 Estructura del Proyecto

*   `miniservidor.py`: Aplicación principal de Flask con soporte para cabeceras de proxy.
*   `flask_app.service`: Archivo de unidad de Systemd para garantizar alta disponibilidad.
*   `apache_conf/`:
    *   `jocarsa.com.conf`: VirtualHost para el dominio principal.
    *   `colores.jocarsa.com.conf`: Configuración para el subdominio de recursos estáticos.
    *   `flask.jocarsa.com.conf`: Configuración del Proxy Inverso con soporte SSL/HTTPS.

---

## 🛠️ Arquitectura del Sistema

El flujo de tráfico se organiza de la siguiente manera:

1.  **Tráfico Estático (Puerto 80):** Apache sirve directamente los archivos desde `/var/www/html/`.
2.  **Tráfico Dinámico (Puerto 443):**
    *   El usuario conecta via **HTTPS** a `flask.jocarsa.com`.
    *   **Apache** recibe la petición, gestiona el certificado SSL y actúa como **Proxy Inverso**.
    *   La petición se redirige internamente a **Gunicorn** ejecutándose en `127.0.0.1:5000`.
    *   **Flask** procesa la lógica y devuelve la respuesta.

---

## 🚀 Guía de Instalación y Despliegue

### 1. Configuración de Flask (Entorno Aislado)
```bash
# Crear entorno virtual e instalar dependencias
python3 -m venv venv
source venv/bin/activate
pip install flask gunicorn werkzeug
2. Configuración de ApacheActiva los módulos necesarios para el proxy:Bashsudo a2enmod proxy proxy_http headers ssl
sudo systemctl restart apache2
Enlaza los VirtualHosts:Bashsudo ln -s /ruta/al/repo/flask.jocarsa.com.conf /etc/apache2/sites-available/
sudo a2ensite flask.jocarsa.com.conf
sudo apachectl configtest
sudo systemctl reload apache2
3. Persistencia con SystemdCopia el archivo de servicio para que la app arranque automáticamente:Bashsudo cp flask_app.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable flask_app
sudo systemctl start flask_app
📊 Monitorización y AuditoríaComandos esenciales para el mantenimiento del servidor:ComandoFunciónhtopMonitorización de recursos (CPU/RAM)journalctl -u flask_app -fLogs en tiempo real de la aplicación Flaskdf -hVerificación de espacio en discosystemctl status apache2Estado del servidor web principal📋 Requisitos de Producción[x] VPS: Servidor con acceso root (Debian/Ubuntu).[x] DNS: Registros tipo A configurados para jocarsa.com y subdominios.[x] SSL: Certificados instalados en /etc/apache2/ssl/.[x] ProxyFix: Implementado en miniservidor.py para corrección de IPs tras el proxy.Proyecto Intermodular DAM | Resumen de Publicación en Servidores
### Consejos para tu README:
*   **Personalización:** He usado los nombres de archivos que mencionaste (`miniservidor.py` y `flask_app.service`).
*   **Bloques de código:** He usado resaltado de sintaxis para que los comandos `bash` se vean claros.
*   **Tablas:** La tabla de monitorización ayuda a que el profesor vea que dominas