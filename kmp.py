import os
import threading
import time
def getText(txtfile):
    txt = open(txtfile,'r').read()
    txt = txt.lower()    #Changer tous les mots du texte en lettres minuscules
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        txt = txt.replace(ch, ' ')  #Remplacer les caractères spéciaux dans le texte par des espaces
    return txt

def kmp(mom_string,son_string):
    # Passer une chaîne parente et une sous-chaîne
    # Renvoie la première position de la sous-chaîne correspondante, s'il n'y a pas de correspondance, renvoie -1
    test=''
    if type(mom_string)!=type(test) or type(son_string)!=type(test):
        return -1
    if len(son_string)==0:
        return 0
    if len(mom_string)==0:
        return -1
    #Trouvez le tableau 'next'
    next=[-1]*len(son_string)
    if len(son_string)>1:# # Le if ici est dans le cas où la liste est hors limites.
        next[1]=0
        i,j=1,0
        while i<len(son_string)-1:
            if j==-1 or son_string[i]==son_string[j]:
                i+=1
                j+=1
                next[i]=j
            else:
                j=next[j]
    # Partie Kmp
    m=s=0#Le pointeur parent et le sous-pointeur sont initialisés à 0
    while(s<len(son_string) and m<len(mom_string)):
        # La correspondance est réussie ou la correspondance de la chaîne parente ne parvient pas à se terminer après la traversée
        if s==-1 or mom_string[m]==son_string[s]:
            m+=1
            s+=1
        else:
            s=next[s]
    if s==len(son_string):#La correspondance est réussie
        return m-s
    #La correspondance est échouée
    return -1

def search_in_txt(txt,str_set):
    mom_string=getText(txt)
    for item in str_set:
        kw=' '.join(item)
        if kmp(mom_string,kw)>=0:
            print(txt+" contain: "+kw+'\n')
            #Rechercher à partir du plus long, puis revenir une fois trouvé, il n'est pas nécessaire de rechercher les plus courts
            return

filelist = os.listdir('./text/')
filelist1=[]
for dataname in filelist:
    if os.path.splitext(dataname)[1] == '.txt':
        filelist1.append(dataname)




# keyword1="soldiers"
while True:
    print("input keywords: (for example:soldiers, or Muggle)")
    keyword1=input().lower() 
    keyword1=keyword1.split(' ')
    #Rechercher des sous-chaînes consécutives
    str_set=[keyword1[i:i + x + 1] for x in range(len(keyword1)) for i in range(len(keyword1) - x)]
    #Recherche à partir de la plus longue sous-chaîne
    str_set=str_set[::-1]
    start_t=time.time()
    threads = []
    for txt in filelist1:
        t = threading.Thread(target=search_in_txt,args=('./text/'+txt,str_set))
        threads.append(t)
    for i in range(len(filelist1)):
        threads[i].start()
    for i in range(len(filelist1)):
        threads[i].join()
    end_t=time.time()
# print(end_t-start_t)




    
