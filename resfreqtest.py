import math
Ind=100 #milliHenrys
Cap = 200   #microFarad
UseInd=Ind/1000
UseCap=Cap*10**-6
print(str(UseInd) + " " + str(UseCap))
resfreqprep=2*math.pi*math.sqrt(UseInd*UseCap)
resfreq=1/resfreqprep    #produces result in Hzs
resfreqkhzs=resfreq/1000
resfreqmhzs=resfreq/1000000
resfreqghzs=resfreq/1000000000
print(str(resfreq) + "Hzs")
print(str(resfreqkhzs) + " Khz")
print(str(resfreqmhzs)+ " Mhz")
print(str(resfreqghzs)+ " Ghz")

