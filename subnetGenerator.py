
# print "Class C Default Subnet Mask = 255.255.255.0"
# print "      128       64       32       16        8        4        2        1"
# print "N       2        4        8       16       32       64      128      256"
# print "H-2   256      128       64       32       16        8        4        2"
# print "C/24  /25      /26      /27      /28       /29     /30      /31      /32"
# print " "
# print "Available Networks:"
# print "Network ID:                     Range:                    Broadcast"
from array import array
##mainNetworkIPAddress=raw_input("Enter main network IP address")
#ainIPAddress=input("What is the main network IP address?")
numOfNetworkReq=input("How many networks would you like to create?")
#mainNetwork=input("Would you like to include main .0 network in your results? (Enter Y:N) ")

#from array import array
#itValueArray = array("i", [256,128,64,32,16,8,4,2,1])
networkValueArray = array("i",[2,4,8,16,32,64,128,256])
#for bitValue in bitValueArray:
for networkValue in networkValueArray:
    if int(numOfNetworkReq) < networkValue:
        print("Network Value=",networkValue)
        print("")
        break
    else:
        #print(networkValue)
        continue
    #print(vitValue)


##print(mainIPAddress)
##mainNetworkIPAddress=input('Enter main network IP address')
##print "Main Network IP Address=",mainNetworkIPAddress
