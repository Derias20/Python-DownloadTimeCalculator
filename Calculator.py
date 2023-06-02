#created by derias => https://github.com/Derias20
#This calculator is only accurate if your device downloads data with the speed of your network.
getnetworkspeed = int(input("Network speed(Mbps)"))
convertMbpstoMB = (getnetworkspeed/8)
getFilesize = int(input("File size (MB)"))
seconds = (getFilesize/convertMbpstoMB)
minutes = (seconds/60)
hours = (minutes/60)
if seconds < 60:
    print("Downloading should take about"+" "+str(round(seconds))+"seconds") 
elif minutes < 60:
    print("Downloading should take about"+" "+str(round(minutes))+"minutes")
elif minutes > 60:
        print("Downloading should take about"+" "+str(round(hours,1))+"hours")    
