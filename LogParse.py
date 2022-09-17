import re
import matplotlib.pyplot as plt
FileImport = open("5gLog.txt", "rt")

SINR = []
RSRP = []
FrameNum = []
PCI = []
THROUGHPUT = []

for line in FileImport:
    if "rsrp" in line:
        sinr1 = re.findall('sinr=' '\d+', line)
        sinr2 = re.findall('\d+', str(sinr1))
        #print(sinr2) 

        rsrp1=re.findall ('rsrp=' '-?\d+', line)
        rsrp2=re.findall('-?\d+', str(rsrp1))
        #print(rsrp2)


        sfn1=re.findall ('sfn=' '\d+', line)
        sfn2=re.findall('\d+', str(sfn1))

        thp1=re.findall( 'Throughput=' '-?\d+', line)
        thp2=re.findall('-?\d+' , str(thp1))
        pc1=re.findall( 'PCI=' '-?\d+', line)
        pc2=re.findall('-?\d+', str(pc1))


        SINR.append(int(sinr2[0]))
        RSRP.append(int(rsrp2[0]))
        FrameNum.append(int(sfn2[0]))
        THROUGHPUT.append(int(thp2[0]))
        PCI.append(int(pc2[0]))

#print(SINR)
#print(RSRP)
#print(FrameNum)

fig, graph = plt.subplots(2,2)

graph[0,0].plot(FrameNum, RSRP)
graph[0,0].set_title('RSRP vs SFN')
graph[0,1].plot(FrameNum, SINR)
graph[0,1].set_title('SINR vs SFN')
graph[1,1].plot(FrameNum, THROUGHPUT)
graph[1,1].set_title('Throughput vs SFN')
graph[1,0].plot(FrameNum, PCI)
graph[1,0].set_title('PCI vs SFN')
plt.show()

