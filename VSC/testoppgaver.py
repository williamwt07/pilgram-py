def beregn_gjennomsnitt(tall_liste):

if_not tall_liste:
return None 


gjennomsnitt = sum(tall_liste) / len(tall_liste)
return gjennomsnittet


tallene = [10, 15, 20, 25, 30]
gjennomsnittet = beregn_gjennomsnitt(tallene)

if gjennomsnittet