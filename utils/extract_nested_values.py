# Este metodo extrae el valor de forma mas clara de un diccionario
# Pre: recibe como parametro un diccionario y un arreglo de claves

def extract_nested_values(data,keys):
    
    
    
    
    for key in keys:
        
        if isinstance(data, list):
            data=data[0]
        data=data.get(key,None)
       
        if data is None:
            return None
    return data