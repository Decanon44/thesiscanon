f = open("input.txt", "r")
fout = open("output.txt", "a")
lines = f.readlines()
flag=0
contlines=0
fecha=""
for line in lines:
  if("FECHA DD/MM/AAAA: " in line):
    fecha=line.split(" ")[2]
  if("========================================================" in line):
    flag=flag+1
  if("*** A N U L A D A ***" in line):
    continue
  if("**** DEVOLUCION ****" in line):
    continue
  if(flag==2 and "                ================= " in line):
    flag=0
  if(flag==2 and "===" not in line):
    line=line.replace("$ ","")
    line=line.replace(" $","").replace(",","")
    dataVar=line[26:].split(" ")
    saveData=[]
    for d in dataVar:
      if(len(d)>0):
        saveData.append(d)
    print(saveData)
    print(line[8:24]+";"+saveData[0]+";"+saveData[1]+";"+fecha)
    fout.write(line[8:24]+";"+saveData[0]+";"+saveData[1]+";"+fecha)
fout.close()
fout2 = open("datacleaned.txt", "a")
finput = open("output.txt", "r")
lines = finput.readlines()
for line in lines:
   fout2.write(line)
fout2.close()