# importamos las siguientes librerias y el modulo procesar
import os 
import time
import shutil
import Procesar
from googlesearch import search
lista=[]

  
# una vez iniciado el script, nos pide que ingresemos la busqueda a investigar, está limitado a 8 páginas  
query = input("Búsqueda: ")
print("Buscando...")
time.sleep(2)
for enlace in search(query, tld="com", num=8, stop=8, pause=5):
  lista.append(enlace)
  print(enlace)

  #################################################

def descargarimgs(urls,num):

  try:
    print(num)
    n_carpeta="imagenes url "+str(num)
    os.mkdir(n_carpeta)
    num=num+1
  except:
    print("Ya existe la carpeta")
    shutil.rmtree(n_carpeta)
    descargarimgs(image,num)
    

  i=1
  for url in urls:
    imagen=Procesar.requests.get(url).content
    nombre_local_imagen=str(i)+'.jpg'
    with open(n_carpeta+'/'+nombre_local_imagen, 'wb') as handler:
      handler.write(imagen)
    i=i+1
for j in range(8):
  page = Procesar.requests.get(lista[j])
  soup = Procesar.bs(page.content,"html.parser")            

  with open("page.html", "w", encoding="utf-8") as fo1:
     fo1.write(str(soup.prettify()))
  fo1.close()
  po1 = soup.findAll("img")
  m=0
  data1=""
  for archivo in po1:
    data1=data1+str(po1[m])
    m=m+1
  print(data1)

  image=Procesar.re.findall(r'//[\w\-\./%]+', data1)
  print("")
  print(image)
  m=0
  while m<len(image):
    image[m]="https:"+image[m]
    m=m+1
  print(len(image))
  m=0
  while m+1<len(image):
    if image[m]==image[m+1]:
      del image[m]
    m=m+1
  num=j+1
  descargarimgs(image,num)
  print("\n" ,image,"la ultima tine: ",len(image))  
