import boto3
import time

print ("#######WELCOME TO THE SECURITY GROUP CLEANER########")
print ("Checking your account for unused security groups...." + "\n")
time.sleep(3)

ec2client = boto3.client('ec2')

# Get the list of Security Groups

Sgs = []
results = ec2client.describe_security_groups(NextToken='')
Sgs += results['SecurityGroups']

try:
    Next_Token = results['NextToken']
except:
    Next_Token = ''

while Next_Token:
    results = ec2client.describe_security_groups(NextToken='')
    Sgs += results['SecurityGroups']
    try:
        Next_Token = results['NextToken']
    except:
        Next_Token = ''


Sgsname = []
for eachsg in Sgs:
   Sgsname.append(eachsg['GroupName'])
#print (Sgsname)


SgsId = []
for eachsg in Sgs:
    SgsId.append(eachsg['GroupId'])
#print (SgsId)

#print (len(SgsId))

#Check for unused ones in Network Interfaces
#Get the list of network interfaces

Next_Token = 'tempvalue'
NetworkInterfaces = []

results = ec2client.describe_network_interfaces()
NetworkInterfaces += results['NetworkInterfaces']
try:
    Next_Token = results['NextToken']
except:
    Next_Token = ''

while Next_Token:
    results = ec2client.describe_network_interfaces(NextToken=Next_Token)
    NetworkInterfaces += results['NetworkInterfaces']
    try:
        Next_Token = results['NextToken']
    except:
        Next_Token = ''

#print (NetworkInterfaces)
#print (len(NetworkInterfaces))

unusedsgs = SgsId[:]
for eachNetworkInterface in NetworkInterfaces:
    groups = eachNetworkInterface['Groups']

    #print (groups)
    for eachgroup in groups:
        if eachgroup['GroupId'] in unusedsgs:
            #print('removing ' + eachgroup['GroupId'])
            unusedsgs.remove(eachgroup['GroupId'])

#print (unusedsgs)
#print (len(unusedsgs))


#check Security groups for referencing
for eachsg in Sgs:
    for eachrule in eachsg['IpPermissions']:
        for idpairs in eachrule['UserIdGroupPairs']:
            if idpairs['GroupId'] in unusedsgs:
                unusedsgs.remove(idpairs['GroupId'])

#print (unusedsgs)
#print (len(unusedsgs))





if (unusedsgs):
    print("The unused security groups are: " + str(unusedsgs))
    while True:
        userinput = input("Are you sure you want to delete them?, Enter 'Y' for 'Yes', 'N' for 'No': ")

        if (userinput == 'y' or userinput == 'Y'):
            while True:
                userinput = input(
                    "Do you want to delete them one by one or all at a time?, Enter 'Y' for 'one by one', 'N' for 'All': ")
                if (userinput == 'y' or userinput == 'Y'):
                    for eachsg in unusedsgs:
                        while True:
                            userinput = input(
                                "Do you want to delete " + eachsg + " ? , Enter 'Y' for 'yes', 'N' for 'no', 'X' to 'exit': ")
                            if (userinput == 'Y' or userinput == 'y'):
                                try:
                                    response = ec2client.delete_security_group(GroupId=eachsg)
                                    print("Deleted " + eachsg)
                                except Exception as ex:
                                    print("Couldn't delete " + eachsg + str(ex))
                                break
                            elif (userinput == 'N' or userinput == 'n'):
                                print("Skipped " + eachsg)
                                break
                            elif (userinput == 'X' or userinput == 'x'):
                                exit(0)
                            else:
                                print("invalid input, try again")
                                continue
                    break
                elif (userinput == 'n' or userinput == 'N'):
                    for eachsg in unusedsgs:
                        try:
                            response = ec2client.delete_security_group(GroupId=eachsg)
                            print("Deleted " + eachsg)
                        except Exception as ex:
                            print("Couldn't delete " + eachsg + str(ex))
                    break
                else:
                    print("invalid input, try again")
                    continue
            break
        elif (userinput == 'n' or userinput == 'N'):
            break
        else:
            continue
else:
    print ("Hooray, you do not have any unused SGs!")