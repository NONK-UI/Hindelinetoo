#MIS OLI PARANDATUD?
#SYNTAX VEAD SELLISED NAGU ":" KOLONI PUUDUSED,VALESTI KIRJUTATUD elif millegi pärast oli else if 
#Print oli lisatud valele reale
#ja line kus on yletus=kiirus - lubatud oli viga sest kiiruse variable oli ilma Int ehk oli tavaline input
print("Vali programm: ")
print("1 - Aastaaeg ")
print("2 - Kiiruse kontroll ")
print("3 - Taksosõit ")
valik = input("Sisesta valik (1-3) => ")


if valik == "1": 

  print("Aastaaeg")
  kuu=int(input("Sisesta kuu number (1-12) => "))
  if kuu<1 and kuu>12:
    print("Vigane kuu")
  elif kuu==12 or kuu<=2:
    print("Talv")
  elif 3<=kuu<=5:
    print("Kevad")
  elif 6<=kuu<=8:

   print("Suvi")

  else:
   print("Sügis")
elif valik == "2" :

  print("Kiiruse kontroll")
  lubatud=int(input("Sisesta lubatud kiirus (km/h) => "))
  kiirus=int(input("Sisesta tegelik kiirus (km/h) => "))
  if kiirus > 0 and lubatud > 0:
    yletus=kiirus - lubatud
 
    if yletus<=0:

       print("Kiirust ei ületatud")
    elif yletus>0:
      print("Hoiatus")
    elif yletus>20:
      print("Trahv")
    elif yletus>40:
      print("Juhiluba võetakse ära")
  elif kiirus < 0 or lubatud < 0:
      print("mingi neis on negatiivne vist")

elif valik == "3" :
  print("Taksosõit")
  allahindlus = False 
  km=float(input("Sisesta sõidu pikkus (km) => "))
  kM = int(km)
  #olen lisanud int kM mis teeb km numbriks
  #olen lisanud allahindlus Bool kui pikkus on rohkem kui 50 siis allahindluse bool on true 
  #lisasin ka variable txt mis juhib teksti kui allahindlus on false siis tekst on tavaline kui allahindlus on siis teekst muutub lisaks "Koos allahindlusega 10%"

  oo=input("Kas sõit on öösel (jah/ei)? => ")
  hind=3+km+0.8
  txt = "Sõidu hind:", round(hind,2), "€" 
  if kM > 50:
    allahindlus = True
   
  else: 
     allahindlus = False
    
  if oo=="jah" and oo=="JAH":
      hind=hind*1.2
  if allahindlus:
      txt = "Sõidu hind koos allahindlusega 10%:", round(hind,2), "€" 
      hind=hind-hind* 100 / 10
 
  print(txt)
  
else:

 print("valesti sisestasid")
