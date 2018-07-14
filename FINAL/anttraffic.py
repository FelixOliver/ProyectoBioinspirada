import random 
import math
from random import randint

#Valores Iniciales
p = 0.99
alfa = 1
beta = 1
Q = 1.0
feromona_Ini = 10 #es el tiempo verde
#cada hormiga calcula el tiempo verde = #carros + tiempo de espera
n_hormigas = 4
iteraciones = 100
abecedario = ['A','B','C','D']#E','F','G','H','I','J']
#['A','B','C','D','E']
#partida = 'A
#la partida depende del tiempo verde

mapa = {('A','A'):0,('A','B'):4,('A','C'):4,('A','D'):4,
            ('B','A'):8,('B','B'):0,('B','C'):8,('B','D'):8,
            ('C','A'):6,('C','B'):6,('C','C'):0,('C','D'):6,
            ('D','A'):5,('D','B'):5,('D','C'):5,('D','D'):0}

#tiempo de espera
visibilidad = {}
for hit in mapa:
    if(mapa[hit]==10000):
        visibilidad[hit] = 0.0
    else:
        visibilidad[hit] = 0.0

feromonas = {}
for hit in mapa:
    if(mapa[hit]==10000):
        feromonas[hit] = 0.0
    else:
        feromonas[hit] = feromona_Ini

def get_siguiente_ruta(ciudad_actual,camino):
    dict_tn = {}
    dict_prob = {}
    suma = 0
    for hit in abecedario:
        if hit not in camino:
            tn = feromonas[(ciudad_actual, hit)]*visibilidad[(ciudad_actual,hit)]
            dict_tn[hit] = tn
            suma = suma + tn
            print (ciudad_actual,"-",hit,": t =",feromonas[(ciudad_actual,hit)],"n =",visibilidad[(ciudad_actual,hit)],"t*n =",tn)
    print ("Suma:",suma)
    for hit in dict_tn:
        print (ciudad_actual,"-",hit,": prob =",dict_tn[hit]/suma)
    aleatorio = random.uniform(0,1)
    print ("Numero aleatorio para la probabilidad:",aleatorio)
    n = 0
    for hit in dict_tn:
        n = n + dict_tn[hit]/suma
        if (n>=aleatorio):
            return hit

#toma la mayor feromona (tiempo verde)
def get_siguiente():
    act = 0
    tup = ('A','A')
    for hit in feromonas:
        if feromonas[hit]>act:
            act=feromonas[hit]
            tup = hit
    return tup[0]

#actualiza el tiempo verde(feromonas) -> por cada iteracion(loop)
def actualizar_feromonas(nodo_verde):
    new_feromonas = {}
    for hit in feromonas:
        if(feromonas[hit]==0.0):
            new_feromonas[hit] = 0.0
        else:
            n_feromona = 0
            cadena_print = ""
            if nodo_verde not in hit:

                n_feromona = p*feromonas[hit]
                cadena_print = ": Feromona ="+str(n_feromona)
            #
            #for camino in vect_caminos:
            #    if(hit[0]+hit[1] in camino[0] or hit[1]+hit[0] in camino[0]):
            #        n_feromona = n_feromona + Q/camino[1]
            #        cadena_print = cadena_print + " + " + str(Q/camino[1])
            #    else:
            #        cadena_print = cadena_print + " + 0.0"
            #print (hit[0],"-",hit[1],cadena_print,"=",n_feromona)
            #PARA EL Q ESTUBO EN VERDE REINICIARA SU FEROMONA A 10
            else:
                n_feromona = n_feromona + (mapa[hit]/2) + (visibilidad[hit]/4)
            print "feromona: ",n_feromona
            new_feromonas[hit] = n_feromona
    return new_feromonas
actual_nodo = 'A'
for t in range (0,iteraciones):
    #vector_caminos = []
    for k in range (0,n_hormigas):
        print ("Hormiga:",k+1)
        print ("actual nodo: ",actual_nodo)
        
        print "vacio todos los autos en actual nodo y doy nuevo numero de autos"
        print ""
        #nuevos carros en actual nodo
        for h in abecedario:
            temp = randint(4,8)
            if mapa[(actual_nodo,h)] != 0.0 :
                mapa[(actual_nodo,h)] = temp
                
        for hit in visibilidad:
           tup = hit
           if tup[0] != actual_nodo:
               visibilidad[hit] = visibilidad[hit] + feromonas[hit]

        #actualiza feromona(tiempo verde)
        feromonas = actualizar_feromonas(actual_nodo)
        print("****************************")
        print "(SOLUCION)feromonas(tiempo verde) para cada nodo:\n",feromonas
        #seleciona nuevo nodo
        print ("******************************")
        actual_nodo = get_siguiente()
        
        #print ("Ciudad Inicial:",partida)
        #camino = partida
        #for i in range (0,len(abecedario)-1):
        #    
        #    siguiente = get_ciudad(camino[-1:],camino)
        #    print ("Ciudad Siguiente:",siguiente)
        #    camino = camino + siguiente
        #print ("Hormiga",k+1,":",camino)
        #vector_caminos.append((camino,fitness(camino)))
    #for k in range (0,n_hormigas):
    #    print ("Hormiga",k+1,"(",vector_caminos[k][0],") - Costo:",vector_caminos[k][1])
    #minimo = min(vector_caminos,key = lambda t: t[1])
    #print ("Mejor Hormiga Global:",minimo[0]," - Costo:",minimo[1])
    #feromonas = actualizar_feromonas(vector_caminos)




        