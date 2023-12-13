# Primeros pasos:

```
git clone git@github.com:dduckduck/ddsi_sem2.git
```

# No es necesario hacer fork. 
Podeis subir los cambios directamente a este repositorio. Para subir los archivos ejecutar en la raiz del proyecto:
```
git add .
git commit -m "mi actualización"
git push
```

primer comando añade todos los archivos que se han modificado<br>
segundo comando no es más que una etiqueta<br>
tercer comando envia los archivos al repositorio<br>

# Entorno virtual
Para ejecutar el fichero para comprobar el entorno virtual y en su caso de que no existe instalarlo

```
bash install.bash 
```

Dentro del bash podemos encontrar:<br>
Para instalar el entorno virtual
```
python3 -m venv .venv
```

Para activar el entorno virtual

```
source .venv/bin/activate 
```

Instalar las dependencias
```
pip3 install -r requirements.txt
```

Desacticar el entorno virtual
```
deactivate
```


# Gestion interna

Se requiere entrar como usuario y contraseña existentes en la base de datos
```
(.venv) export DB_USERNAME="XXXXXXXXX"
(.venv) export DB_PASSWORD="XXXXXXXXX"
```

Para crear la base de datos 
```
(.venv) python3 db.py
```

Para lanzar la pagina 
```
(.venv) flask run 
```
La pagina estará disponible en "http://localhost:5000/"


# Nada relevante
Lo óptimo sería que cada uno use su propia rama para evitar conflictos de actualizaciones y posteriormente hacer merge con la rama main. 
Supongo que para este seminario lo podemos ignorar

Por si alguien quiere investigar/probar con esto deberia ser suficiente:

1. Actualizar y mostrar todas las ramas disponibles
    ```
    git fetch --all
    git branch --all
    ```

2. Ir a mi rama
```
git checkout nombre_rama
```

3. Syncronizar mi rama con la rama main
```
git checkout main
git pull
git checkout tu_rama
git merge main
```

4. Syncronizar main con mi rama
```
git checkout main
git merge tu_rama
```
