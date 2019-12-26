import numpy

nBins=10000
binsize=1
binLo =numpy.zeros(nBins)
binHi =numpy.zeros(nBins)
binCent = numpy.zeros(nBins)

for i in range(nBins):
    binLo[i]=2+binsize*i
    binHi[i]=2+binsize*(i+1)-1
    binCent[i]=(binLo[i]+binHi[i])/2.

g = open('binningFile_%d_%d.dat'%(nBins,binsize),mode="w")
for i in range(nBins):
    g.write("%0.2f %0.2f %0.2f\n"%(binLo[i],binHi[i],binCent[i]))
g.close()