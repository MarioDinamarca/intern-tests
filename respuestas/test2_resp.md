# Explicación de la lógica de la función.
La función scrape_url lo que hace es que al recibir una url como parametro, procede a intentar realizar una solicitud mediante la función get de la librería requests, en el caso de que no resulte la request debido a que el código de la respuesta es distinto a 200, imprimirá un mensaje de error junto al status code correspondiente, en caso de que al realizar la solicitud, esta arroje un error también se informará por pantalla un error.

En caso de que la solicitúd sea exitosa (cod. 200), se procederá con el scraping mediante la utilización de la librería BeautifulSoup que realizará el parseo de la información obtenida en la solicitud realizada mediante request.

Posteriormente se procederá a buscar el primer elemento que cumpla con ser una etiqueta de tipo 'div' de la clase 'example-class', de esta etiqueta se extraerá el texto contenido en ella, asignandolo a la variable data.

Finalmente se retornará la variable data que contiene el texto.

# ¿En qué casos es útil hacer web scraping secuencial y concurrente?

El webscraping concurrente es útil cuando podemos realizar extracciones en paralelo aprovechando los hilos de nuestra CPU, así si tenemos 8 páginas distintas para realizar scraping donde cada una demoraría 10 minutos, mediante el uso de concurrencia, podríamos utilizar 8 hilos para scrapear las 8 en 10 minutos, en el caso de que fuese secuencial se demoraría 80 minútos, pues empezaría el siguientes solo después de haber terminado el anterior.

Respecto al webscraping secuencial, se me ocurre que pudiese llegar a ser útil cuando se desea realizar webscraping a algún sitio alojado en un servidor que tenga protección contra web scraping, por lo que en caso de recibir muchas solicitudes desde una misma IP este las banee, esto considerando que no se tiene acceso a un proxy que pueda ayudar a evitar ser descubierto por los métodos de seguridad del servidor donde se realizarán las solicitudes. Por tanto, realizar un trabajo secuencial que simule de mejor manera el comportamiento de un humano, es una buena idea.