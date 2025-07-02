# lista_tarea_pendientes
pagina web lista de tareas pendientes.


# 📝 Página de Tareas Pendientes (Django WebApp)

Aplicación web construida con Django que permite a los usuarios **registrarse, iniciar sesión y gestionar sus tareas diarias**. Incluye funcionalidades completas CRUD (crear, leer, actualizar y eliminar tareas) y sistema de autenticación de usuarios.

---

## 🚀 Funcionalidades

- ✅ Registro y autenticación de usuarios
- ✅ Página de inicio con lista personalizada de tareas
- ✅ Crear nuevas tareas con título, descripción y estado de completado
- ✅ Editar tareas existentes
- ✅ Eliminar tareas confirmando acción
- ✅ Interfaz limpia con estructura de plantillas HTML
- ✅ Sistema de administración de Django activado

---

## 🛠️ Tecnologías Usadas

- **Lenguaje principal:** Python 3.10+
- **Framework:** Django 4.x
- **Frontend:** HTML5 + CSS3 (plantillas base de Django)
- **Base de datos:** SQLite (por defecto)
- **Entorno local:** CMD + VSCode + Git + GitHub

---

## 📦 Estructura del Proyecto

```bash
mi_web/
├── src/
│   └── proyecto/
│       ├── base/
│       │   ├── templates/
│       │   │   └── base/
│       │   │       ├── login.html
│       │   │       ├── registro.html
│       │   │       ├── tarea_list.html
│       │   │       ├── tarea_form.html
│       │   │       ├── tarea.html
│       │   │       └── tarea_confirm_delete.html
│       │   ├── views.py
│       │   ├── models.py
│       │   ├── urls.py
│       │   └── admin.py
│       ├── proyecto/
│       │   ├── urls.py
│       │   ├── settings.py
│       │   └── wsgi.py
│       └── manage.py
