#!
# from mechanize import Browser
# import csv
#
# with open('namecsv.csv') as csvfile:
#     reader= csv.DictReader(csvfile)
#     for rows in csvfile:
#         browser = Browser()
#         browser.open("https://www.tse.go.cr/consulta_persona/consulta_cedula.aspx")
#         form= browser.select_form("form1")
#         browser["txtcedula"]=rows
#         response=browser.submit()
#         name=str(rows)
#         file=open(name+".html","w")
#         file.write(response.read().decode("UTF-8"))
#         file.close()

#Ejercicio #2

from mechanize import Browser
nombre=str(input("Digite el nombre de la persona que desea buscar \n >"))
apellido1=str(input("Digite el primer apellido de la persona \n >"))
apellido2=str(input("Digite el segundo apellido de la persona \n >"))
browser= Browser()
browser.open("https://www.consulta.tse.go.cr/consulta_persona/consulta_nombres.aspx")
form= browser.select_form("form1")
browser["txtnombre"]=nombre
browser["txtapellido1"]=apellido1
browser["txtapellido2"]=apellido2
response=browser.submit()
name=nombre
file=open(name+".html","w")
file.write(response.read().decode("UTF-8"))
file.close()