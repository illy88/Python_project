import os
from datetime import datetime
class Lista:
    file=''
    def __init__(self,name):
        self.name = name
        self.file=name+'.txt'
        f=os.path.dirname(self.file)
        if not os.path.exists(f): 
            f=open(self.file,"a")
        f.close()
    #lista operazioni    
    def h(self):
            print('a >>> inserisci azione \nls >>> mostra tutte le azioni \nd(param:id) >>> cancella \nt(param:id) >>> Fatto-Non Fatto \ne(param:id, titolo) >>> modifica azione \ns(param:Titolo) >>> Ricerca azione')
            
            
    #validazione input
    def validazione (self,tit):
        titolo = str(tit)
        if len(tit)>=5 :
            return True
        else:
            return False

    #calcolo id successivo
    def calcoloid (self):
        f=open(self.file,'r')
        lines = f.readlines()
        f.close()
        indice=0
        if len(lines)!=0:
           lines.reverse()
           for line in lines:
               riga=str(line).split()
               indice=riga[0]
               break
           indice=int(indice)+1
        return indice
    
    #stampa lista
    def stampa(self,lista):
        print ('{id: ',lista[0],' " ',lista[1],' "',' done: ',lista[2],' timestamp: ',lista[3],'}\n')
        
    #cancella linea
    def d (self,val):
        f= open(self.file,'r')
        lines = f.readlines()
        f.close()
        f=open(self.file, "w")
        for line in lines:
            riga=str(line).split()
            if riga[0]!=val:
                f.write(line)
        f.close()
     
    #inserisci nuovo valore
    def a(self,titolo):
        f=open(self.file,'a')
        while self.validazione(titolo) == False:
            print('titolo non valido inserire una stringa più lunga di 5 caratteri')
            titolo=input("inserisci il titolo")
        dt=datetime.now()
        ind=self.calcoloid()
        f.write(str(ind))
        f.write(' ')
        f.write(titolo)
        f.write(' False ')
        f.write(str(datetime.timestamp(dt)))
        f.write('\n')
        f.close()

     #Toggle di una valore  
    def t(self,val):
        f=open(self.file,'r')
        lines = f.readlines()
        f.close()
        f=open(self.file, "w")
        i=0
        for line in lines:
            riga=str(line).split()
            if riga[0]== val:
                f.write(riga[0])
                f.write(' ')
                f.write(riga[1])
                if riga[2]=='False':
                    f.write(' True ')
                else:
                    f.write(' False ')
                f.write(riga[3])
                f.write('\n')
            else:
                f.write(line)
        f.close()

    #modifica del titolo di un valore
    def e(self,val, val1):
        f=open(self.file,'r')
        lines = f.readlines()
        f.close
        f=open(self.file, "w")
        for line in lines:
            riga=str(line).split()
            if riga[0]==val:
                linea=str(line).replace(riga[1],val1)
            else:
                linea=line
            f.write(linea)
        f.close()

    #ricerca di un valore 
    def s(self,val):
        f=open(self.file,"r")
        contents=f.readlines()
        indice=0
        i=0
        for line in contents:
            try:
                indice=line.index(val)
            except:
                indice=0
                i+=1
            if indice != 0:
               lista= str(line).split()
               self.stampa(lista)
               
            indice=0
        if i==len(contents):
             print('nessun valore trovato')
        
    #visualizzazione di tutto il file
    def ls(self):
        f=open(self.file,'r')
        contents = f.readlines()
        if contents != '\n':
            print('[')
            for i in reversed(range(0,len(contents),1)):
                lista= str(contents[int(i)]).split()
                self.stampa(lista)
            print(']')
        else:
            print('File Vuoto')
        f.close()
