import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")

columnas_c1c2 = tbl0.iloc[:,[1,2]]
tuplas = [tuple(x) for x in columnas_c1c2.to_records(index=False)]
sorted_tupla = sorted(tuplas, key=lambda x: x[0])

diccionario={}
for key, value in sorted_tupla:
     if key not in diccionario.keys():
         diccionario[key]=[]
     diccionario[key].append(value)
                
new_sequence=[]
for key, value in diccionario.items():
    tupla=(key, value)
    new_sequence.append(tupla)

sorted_data = [(key, sorted(values)) for key, values in new_sequence]
formatted_data = [(key, ':'.join(map(str, values))) for key, values in sorted_data]

valores = pd.DataFrame(formatted_data)
valores.columns = ['_c0','_c1']

print(valores)