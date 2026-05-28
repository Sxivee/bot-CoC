import pyautogui
import time
import random
import sys
from matplotlib.path import Path
import numpy as np

mensajes = {
    'es': {
        'Farm_Copes': '¿Quieres conseguir materiales o conseguir copas? Materiales=[1] / Copas [2]: ',
        'SuperNormal': 'Quieres atacar con Duendes Normales o Súper? Normales=[1] / Súper[2]: ',
        'elige_idioma': 'Elige un idioma (es/en): ',
        'TipoDragones':'Quieres atacar con deagones o con dragones eléctricos? Normales=[1] / Eléctricos[2]',
        'opcion_invalida': 'Opción no válida.'
    },
    'en': {
        'Farm_Copes': 'Do you want to Farm or get Cups? Farm=[1] / Cups=[2]',
        'despedida': 'Goodbye, thank you for using the application.',
        'elige_idioma': 'Choose a language (es/en): ',
        'opcion_invalida': 'Invalid option. Defaulting to Spanish.'
    }
}

idioma=input(mensajes['en']['elige_idioma'].strip().lower())

if idioma not in mensajes:
    print (mensajes['en']['opcion_invalida'])
    idioma='en'


TipoAtac= int(input(mensajes[idioma]['Farm_Copes']))

i=1

if TipoAtac== 1:

    SuperNormal=int(input("Vols atacar amb duendes normals o súper? Normal=[1] Súper=[2]:"))
    
    if SuperNormal==1:
        import AtacarDuendesNormals
    elif SuperNormal==2:
        import AtacarDuendesSuper
    else:
        print("Opció no disponible")
elif TipoAtac==2:
    TipoDragones=int(input("Vols atacar amb dragones o Dragones eléctricos? Dragones=[1] / Dragones Eléctricos=[2]: "))
    if TipoDragones==1:
        import AtacarDragones
    elif TipoDragones==2:
        import AtacarDragonesÉlectricos
    else:
        print("Opció no disponible")
else:
    print("Opció no Disponilbe")
    sys.exit()