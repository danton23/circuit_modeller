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
#### Formula to Calculate 98% of Sideband for FM signal #####
### BT=2(Δf+fm) #### meaning Average bandwith (for 98% of power) = Two times(frequency deviation +the modulation freq)
### i.e if deviation =+-75Khz and max modulation freq of 15Khz power approxs (2(75+15)) =180Khz (add on around 20 KHZ to be sure! so bandwidth = 200KHZ therefore USB = f+ 100 and LSB- 100
Freqdev= 75
Modfreq= 15
Combination=Freqdev+Modfreq
AvBand=2*Combination
print(str(AvBand) + " is Average Bandwidth" )

