def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    new_dict=dict()
    try:
        with open(filename, 'r') as file:
            file_content = file.read()
            for i in file_content.split(';'):
                if i.strip() == '':
                    continue
                param=i.find(':')
                key = i[:param]
                val = i[param+1:]
                if key.strip() != '':
                    if key not in new_dict:
                        new_dict[key] = []
                    new_dict[key].append(float(val))
    except FileNotFoundError as e:
        print(e)
        raise FileNotFoundError('Error archivo no encontrado')
    return new_dict

def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    for k,v in data.items():
        total = sum(v)
        promedium = 0  # Default value
        try:
            promedium = total / len(v)
            print(f"{k}: ventas totales ${total:.2f}, promedio ${promedium:.2f}")
        except ZeroDivisionError:
            print('No es posible dividir por 0')

process_dict(read_file_to_dict('./datos.csv'))
