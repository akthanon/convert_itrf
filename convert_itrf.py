import matplotlib.pyplot as plt
import numpy as np
import math
#Comentario2
f = open("stations.txt", "r")
archivo=f.readlines()

f = open("docs/Transfo-ITRF2014_ITRFs.txt", "r")
architrf=f.readlines()

itrf="2005"
time=1000


for i in range(8,33,2):
    linea=architrf[i]
    datos=linea.split()
    name=datos[0]

    if itrf in name:
        stx=float(datos[1])*0.001
        sty=float(datos[2])*0.001
        stz=float(datos[3])*0.001
        sd=float(datos[4])*10**-9
        srx=float(datos[5])*(0.001*np.pi)/(3600*180)
        sry=float(datos[6])*(0.001*np.pi)/(3600*180)
        srz=float(datos[7])*(0.001*np.pi)/(3600*180)

        linea=architrf[i+1]
        datos=linea.split()    
        rtx=float(datos[1])*0.001
        rty=float(datos[2])*0.001
        rtz=float(datos[3])*0.001
        rd=float(datos[4])*10**-9
        rrx=float(datos[5])*(0.001*np.pi)/(3600*180)
        rry=float(datos[6])*(0.001*np.pi)/(3600*180)
        rrz=float(datos[7])*(0.001*np.pi)/(3600*180)


for linea in archivo:
    datos=linea.split()
    name=datos[0]
    xx=datos[1]
    yy=datos[2]
    zz=datos[3]
    vx=datos[4]
    vy=datos[5]
    vz=datos[6]

    P1=np.array([xx,yy,zz],float)
    P2=np.array([stx,sty,stz],float)
    P3=np.array([[sd,-srz,sry],[srz,sd,-srx],[-sry,srx,sd]],float)

    res1=P1+P2+np.dot(P3,P1)
    print(name)
    print("pos1ORIG",P1)
    print("pos1ITRF",res1)

    V1=np.array([vx,vy,vz],float)
    V2=np.array([rtx,rty,rtz],float)
    V3=np.array([[rd,-rrz,rry],[rrz,rd,-rrx],[-rry,rrx,rd]],float)


    P21=P1+V1*time
    P2=np.array([stx,sty,stz],float)
    P3=np.array([[sd,-srz,sry],[srz,sd,-srx],[-sry,srx,sd]],float)

    res2=P21+P2+np.dot(P3,P21)

    print("pos2VELO",P21)
    print("pos2ITRF",res2)

    resvel1=V1+V2+np.dot(V3,P1)
    print("oldvel",resvel1)

    resvel2=(res2-res1)/time

    dif=V1-resvel2
    ndif=[]
    for i in dif:
        ndif.append("{:.6f}".format(i))
    print("newvel",resvel2)
    print("oldvel",ndif)
    print("*")







