import os

liste=os.listdir("../")
liste2=[]
liste3=[]
for j in liste:
    if len(j)>30:
        m=len(j)-30
        
        liste2.append(j[0:(-7-m)]+"...")
    else:
        liste2.append(j[0:-4])
for m in liste:
    liste3.append("'"+"Music/"+m+"'")

    

for i,k in zip(liste3,liste2):
    print("<div class="+'"box"'+">\n    <button onclick="+'"test('+i+') "'+"></button>\n    <p>"+k+"</p>\n</div>\n")
    

print(len("congratulations! let_s see what..."))
