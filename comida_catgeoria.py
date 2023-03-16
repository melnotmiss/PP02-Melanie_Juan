
"""
    Leer el archivo adjunto "wendys-menu.csv", y devolver el promedio de las calorías de los alimentos agrupados por categorías.
    
"""
import csv
import pandas as pd

def comida_categoria():
    datos=pd.read_csv('wendys-menu.csv', header=0)
#si imprimimos datos veremos todos los datos en una tabla organizada llamado dataframe de pandas 
#print(datos)


#del modulo pandas utilizamos el metodo .loc para seleccionar la columna categoria  que contenga el valor Chicken, burger y breakfast en sus filas 
    Chicken=datos.loc[datos["Category"]=="Chicken"]
    Burgers=datos.loc[datos["Category"]=="Burgers"]
    Breakfast=datos.loc[datos["Category"]=="Breakfast"]


#ahora buscamos los valores de las calorias de chicken,burger y breakfast
    caloriasChicken=Chicken.iloc[:,2]
    caloriasBurgers=Burgers.iloc[:,2]
    caloriasBreakfast=Breakfast.iloc[:,2]


#con el metodo .sum() sumamos todos los valores de las calorias de chicken
    chickenTotal=caloriasChicken.sum()
    burgerTotal=caloriasBurgers.sum()
    breakfastTotal=caloriasBreakfast.sum()

#calculamos el promedio de calorias 
    promedioChicken=round((chickenTotal/17),2)
    promedioBurger=round((burgerTotal/9),2)
    promedioBreakfast=round((breakfastTotal/17),2)


    promedioTotalCal=[]
#convertimos cada promedio en un diccionario y lo añadimos a una lista
    promedioTotalCal.append({"Burgers":promedioBurger})
    promedioTotalCal.append({"Chicken":promedioChicken})
    promedioTotalCal.append({"Breakfast":promedioBreakfast})

    print("Promedio de calorías por categoría: ")
    print(promedioTotalCal)
