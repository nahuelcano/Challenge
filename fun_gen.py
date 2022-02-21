import logging
import locale
import re
import sys
import requests
import os
import datetime


def req_ok(web):

    fuente = web.status_code
    if fuente != 200:
        logging.warning(f"fail request:{fuente}")
        sys.exit(f"fail request:{fuente}")
    return


def links(url):

    pagina = requests.get(url)
    req_ok(pagina)

    part1 = 'href="'
    part2 = '"DESCARGANDO'

    Link_des = re.search(f"{part1}(.*?){part2}", pagina.text)

    return Link_des


def descargar_tabla(url_des):

    pagina = requests.get(url=url_des)
    req_ok(pagina)

    contenido = pagina.content

    archivo = url_des.split("/")[-1]
    logging.info(f"Se ha descargado la información de {archivo}")

    return contenido


def file_path(categoria):

    # Carpeta principal
    path = "challenge"

    # Carpeta secundaria: Categoría
    carpeta = categoria

    # Carpeta terciaria: Fecha
    año = datetime.today().strftime("%Y")
    mes = datetime.today().strftime("%B")
    folder_date = año + "-" + mes  # YYYY-mes

    # Path final para la categoría correspondiente
    path_final = os.path.join(path, carpeta, folder_date)

    # Creamos las carpetas de forma recursiva si NO existen.
    os.makedirs(path_final, exist_ok=True)

    # # Fecha de Descarga: DD-MM-YYYY
    download_date = datetime.today().strftime("%d-%m-%Y")
    # Nombre del archivo a guardar
    file = carpeta + "-" + download_date + ".csv"
    # Path con el nombre del archivo a guardar
    file_path = os.path.join(path_final, file)

    return file_path


def guardar(file_path, tabla):

    csv_file = open(file_path, "wb")
    csv_file.close()

    return
