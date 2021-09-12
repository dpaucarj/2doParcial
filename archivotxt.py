archivo, f ='datos.txt',""
docentes= [{'nombre':'Darwin', 'edad':30, 'fac': 'ingenieria'}, 
{'nombre':'Juan', 'edad':30, 'fac': 'salud'},
{'nombre':'Yadi ', 'edad':40, 'fac': 'administrativa'}]

with open (archivo, 'w') as writer:
    for i in range (len (docentes)):
        linea =''
        for clave , valor in docentes[i].items():
            if clave =='fac':
                linea = linea+(str (valor) if type(valor)== int else valor )+'\n'
            else:
                linea = linea+(str (valor) if type(valor)== int else valor )+';'
        writer.writelines(linea)

try :
    f= open (archivo, 'r')
    for linea in f :
        print(linea[:-1])
except Exception as e:
    print("Error de archivo: " + str (e)) 
finally:
    f.close()            


