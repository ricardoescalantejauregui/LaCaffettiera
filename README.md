# Proyecto Webempresa

Este repositorio contiene un proyecto Django para la empresa Webempresa. A continuación encontrarás los pasos para clonarlo, crear el entorno virtual, instalar dependencias y preparar la base de datos.

---

## 1. Clonar el repositorio

```bash
git clone https://github.com/ricardoescalantejauregui/webempresa.git
cd webempresa
```

---

## 2. Crear y activar el entorno virtual

Usaremos un entorno virtual en la carpeta `.venv`:

```bash
python3 -m venv .venv
```

* **Linux/macOS**

  ```bash
  source .venv/bin/activate
  ```
* **Windows (PowerShell)**

  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
* **Windows (cmd.exe)**

  ```bat
  .\.venv\Scripts\activate.bat
  ```

---

## 3. Instalar dependencias

Si ya existe un `requirements.txt`, instala todo en una sola línea:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> **Nota**: Si tu `requirements.txt` no incluye `django-ckeditor` o `Pillow`, instálalos manualmente:
>
> ```bash
> pip install django-ckeditor Pillow
> ```

---

## 4. Crear y aplicar migraciones

1. **Generar nuevas migraciones** (si has modificado modelos):

   ```bash
   python manage.py makemigrations
   ```

2. **Ejecutar todas las migraciones pendientes**:

   ```bash
   python manage.py migrate
   ```

   Al terminar, Django creará todas las tablas necesarias (incluyendo `social_link`, `blog`, `services`, etc.).

---

## 5. Crear un superusuario (opcional)

Si necesitas acceder al admin de Django:

```bash
python manage.py createsuperuser
```

Sigue los pasos para definir usuario, correo y contraseña.

---

## 6. Levantar el servidor de desarrollo

Con el entorno activado y todo listo:

```bash
python manage.py runserver
```

Abre en tu navegador:

```
http://127.0.0.1:8000/
```

---

## Tips adicionales

* Para activar automáticamente el entorno al entrar en la carpeta, añade esto a tu `~/.bashrc` o `~/.zshrc`:

  ```bash
  ```

autoenv() {
if \[ -f .venv/bin/activate ] && \[ -z "\$VIRTUAL\_ENV" ]; then
source .venv/bin/activate
fi
}
cd() { builtin cd "\$@"; autoenv; }

````

- Mantén actualizado tu `requirements.txt`:
```bash
pip freeze > requirements.txt
````

¡Listo! Ya tienes tu proyecto Django corriendo en local.
