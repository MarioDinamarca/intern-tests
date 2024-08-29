# Linea "df[col] = df[col].str.strip()"
## El problema
El problema acá es que en primer lugar se quiere aplicar el método str.strip() el cual se puede aplicar solo a columnas que contengan valores de tipo string, y al ver que la columna "Edad" está compuesta por datos de tipo "float64", el código produce error.

## La propuesta de solución
Las propuestas de solución pueden ser varias, pero considerando que solo que pueden hacer correcciones y no cambios mayores, la propuesta más cercana a la solución original va de la mano con agregar el casteo "astype(str)" ente "df[col]" y ".str.strip()", pero esto castearía incluso la columna númerica de "float64" en tipo string igualmente, por lo que  mi propuesta va de la mano de la utilización de una función lambda donde se utilice la función strip solo si es que el valor es un string (de otra forma no tendría sentido tampoco utilizar la función strip), por lo que así también evitamos realizar dobles casteos a valores de tipo string y castear valores numericos a string.

La nueva formula quedaría de la siguiente manera:
``` python
df[col] = df[col].apply(lambda x: x.strip() if isinstance(x,str) else x)
```
Donde a cada valor de las columnas recorridas, se le aplicará la función strip mientras cumpla con ser un string.


# Linea "df[col] = re.sub(r'\W+', '', df[col])"

## El problema
El problema acá es que se desea aplicar un remplazo utilizando una operación con expresión regular, esto trae problemas, pues la operación se debe aplicar sobre una cadena de caracteres y en este caso se está entregando una columna en el tercer parametro de la función "re.sub()" 

## La propuesta de solución
En este caso la propuesta también va de la mano de utilizar un función lambda al igual que la solución anterior. Puesto que de nuevo queremos comprobar que el valor sobre el cual realizaremos esta limpieza de valores no alfanumericos sea un valor de tipo string, puesto que si es float no tiene sentido realizar una limpieza de ese tipo en un valor que no sea string. Por lo que se aplicará a cada valor de la columna la función re sub, solo en caso de que sea una instancia de string.

``` python
df[col] = df[col].apply(lambda x: re.sub(r'\W+', '',x) if isinstance(x,str) else x)
```

# Linea "df[col].fillna('', inplace=True)"
Esta linea de código funciona bien.