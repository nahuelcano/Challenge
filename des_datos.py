import logging
import locale
import fun_gen


def des_datos():

    try:
        locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")
    except:
        locale.setlocale(locale.LC_ALL, "es_AR.UTF-8")

    museo_url = "https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d"
    cine_url = "https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae"
    biblo_url = "https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7"

    bases = ["useo_url", "cine_url", "biblo_url"]

    for site in bases:
        print(f"Descargando{site} ...")

        categ = site.replace_("url", "")
