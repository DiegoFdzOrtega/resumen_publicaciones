# 🌐 Infraestructura de Servidores Jocarsa (Nodo 026)

Este repositorio contiene la documentación y configuración de un **entorno de producción híbrido** diseñado para el despliegue de microservicios Python bajo un servidor perimetral robusto.

---

## 📋 ¿Qué es este proyecto?
Es una arquitectura de **Proxy Inverso**. Implementa un servidor web **Apache** como puerta de enlace (Gateway) y una aplicación **Flask** como motor de lógica de backend. En lugar de exponer Python directamente a internet, usamos Apache como escudo.

## ⚙️ ¿Qué hace el sistema?
1.  **Gestión de Tráfico:** Apache recibe todas las peticiones en los puertos estándar (`80`, `443`).
2.  **Filtrado y Seguridad:** Apache gestiona el cifrado **SSL/HTTPS** y protege la aplicación de accesos no autorizados.
3.  **Puente de Datos:** Mediante `mod_proxy`, Apache reenvía las peticiones dinámicas a un proceso **Gunicorn** que ejecuta la app Flask internamente en el puerto `5000`.
4.  **Respuesta:** Flask procesa la lógica y Apache entrega el resultado final al usuario.

## 🎯 ¿Para qué funciona?
*   **Seguridad:** Aísla la aplicación Flask del contacto directo con ataques externos.
*   **Rendimiento:** Apache es mucho más eficiente sirviendo archivos estáticos (HTML, CSS, imágenes).
*   **Alta Disponibilidad:** Gracias a **Systemd**, la aplicación se reinicia automáticamente si detecta un fallo.
*   **Organización:** Permite gestionar múltiples subdominios (`colores.jocarsa.com`, `flask.jocarsa.com`) de forma centralizada.

---

## 🛠️ Stack Tecnológico
*   **Gateway:** Apache 2.4 (`mod_proxy`, `mod_ssl`)
*   **Backend:** Flask 3.x (Python)
*   **WSGI Server:** Gunicorn
*   **Daemon:** Systemd (Gestión de procesos)

---

## 📂 Archivos Críticos

| Archivo | Función |
| :--- | :--- |
| `miniservidor.py` | Aplicación Flask con middleware `ProxyFix`. |
| `flask_app.service` | Configuración del demonio para ejecución en segundo plano. |
| `*.conf` | Archivos de VirtualHost para la configuración del Proxy. |

---

## 🚀 Mantenimiento y Logs
Para monitorizar el estado del nodo en tiempo real:

```bash
# Ver estado de los servicios
systemctl status apache2
systemctl status flask_app

# Auditoría de logs de Flask
journalctl -u flask_app -f