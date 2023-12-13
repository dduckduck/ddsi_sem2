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

Para activar el entorno virtual

```
source .venv/bin/activate 
```

Se requiere entrar como usuario y contraseña existentes en la base de datos
```
export DB_USERNAME="XXXXXXXXX"
export DB_PASSWORD="XXXXXXXXX"
```

# Gestion interna
Para crear la base de datos 
```
python3 db.py
```

Para lanzar la pagina 
```
flask run 
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



# Cosas
en el pdf utiliza '-' para los nombres de algunos atributos y tablas. El caso es que esto causa problemas. De modo que esto resulta en error
```sql CREATE TABLE Detalle-Pedido(Cpedido INT,Cproducto INT,Cantidad INT, CONSTRAINT dp_primaria PRIMARY KEY (Cpedido,Cproducto));```
