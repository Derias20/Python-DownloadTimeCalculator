#made by Derias -> https://github.com/Derias20
getnetworkspeed = int(input("Network speed(Mbps)"))
convertMbpstoMB = (getnetworkspeed/8)
getFilesize = int(input("File size (MB)"))
seconds = (getFilesize/convertMbpstoMB)
minutes = (seconds/60)
hours = (minutes/60)
if minutes > 60:
    print("Downloading should take about"+" "+ str(round(hours,1))+"hour/s") 
else:
    print("Downloading should take about"+" "+str(round(minutes))+"minutes")    
