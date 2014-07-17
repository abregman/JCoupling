import os, sys
import glob
import subprocess
from string import*



#################MATHEMEATICA TO G09 CONVERSION FUNCTIONS################################
def NegWithExp(nums,i,temp):
    temp += nums[i:i+7]
                    
    exp = nums[i+9:i+11]#Find out the Exponent
    exp = int(exp[1])- 1# Exponent minus 1, since we add a zero in the next line
    
    num = temp[0]+ '0' + '.' + (exp*'0')
    num += temp[1] + temp[3:]
    return num

def NegNoExp(nums,i,temp):
    num = nums[i:i+8]
    return num

def PosWithExp(nums,i,temp):
    temp += nums[i:i+7]

    exp = nums[i+8:i+10]#get exponent
    exp = int(exp[1]) - 1

    num = '0' + '.' + (exp*'0')
    num += temp[0] + temp[2:]
    return num

def PosNoExp(nums,i,temp):
    num = nums[i:i+7]
    return num
    

def NumConstruct(nums):
    i = 0
    num = ''
    temp = ''
    numarray = []
    while i != len(nums)+1:
        temp = ''
        num = ''
        if i + 11 > len(nums):
            if len(nums)-i == 7:
                num = PosNoExp(nums,i,temp)
                numarray.append(num)
            elif len(nums)-i == 8:
                num = NegNoExp(nums,i,temp)
                numarray.append(num)
            elif len(nums-i) == 10:
                num = PosWithExp(nums,i,temp)
                numarray.append(num)
            else:
                num = NegWithExp(nums,i,temp)
                numarray.append(num)
            
            return numarray
        
        
        elif (nums[i] == '-') and (nums[i+8] == 'E'): # negative numbers w/ Exponents
            num = NegWithExp(nums,i,temp)
            numarray.append(num)
            count = 11
            
        elif (nums[i] == '-') and (nums[i+8] != 'E'):# neg number no exponent
            num = NegNoExp(nums,i,temp)
            numarray.append(num)
            count = 8
              
        elif (nums[i+7] == 'E'):# pos number with exponent
            num = PosWithExp(nums,i,temp)
            numarray.append(num)
            count = 10
            
        else:# pos number no exponent
            num = PosNoExp(nums,i,temp)
            numarray.append(num)
            count = 7
            
            
        i += count
        





def MMTCAtoG09(home_dir,currfile):
    with open ("%s.xyz" %(currfile),'r') as f:
        coords = f.read()
    coords = coords[89:]
    newcoords = ''
    atoms = ''
    nums = ''
    i = 0
    atomlist = ascii_letters.replace('E','')
    numlist = octdigits + 'E' +'-' + '.'+ '8' +'9'
    
    while i < len(coords):
        if coords[i] in atomlist :
            atoms += coords[i]
        elif coords[i] in numlist:
            nums += coords[i]
        else:
            i = i
        i += 1
    numarray = NumConstruct(nums)

    i = 0
    j = 0
    while j < len(atoms):
        row = numarray[i] + ' '+ '\t' + numarray[i+1]+ ' ' + '\t' + numarray[i+2] +'\n'
        newcoords += atoms[j] + ' ' + '\t'+ row
        i += 3
        j += 1
    
    with open ("%s.xyz" %(currfile), "w") as f:
        f.write(newcoords)




######################################################################################33

def Zindosetup():
    home_dir = os.getcwd()
    DirList = ""
    count = 1
    print "Rot or Trans? Which Axis?:" #i.e RotX or TransY
    action = raw_input()
    print "What is the Multiplcity?:"
    Multiplicity = raw_input()
    print "What is the Charge?:"
    Charge = raw_input()
    print "Which coord file?:"
    coordfile = raw_input() #just the name, no extension
    print "How Many Versions?:"
    versions = raw_input()

    while count <= int(versions):
        currfile = coordfile + str(count)
        filename = action + coordfile + str(count)
    

        subprocess.call("dos2unix %s.xyz" %(currfile), shell=True)
        
        MMTCAtoG09(home_dir,currfile)
        
        subprocess.call("cp %s.xyz %s.com" %(currfile,filename), shell=True)


        with open("%s/%s.com" %(home_dir, filename),"r") as f:
            coords = f.read()
        setup =("%%mem=16gb \n%%chk=%s/%s \n%%nprocshared=8 \n#p ZINDO Punch=MO  IOp(3/33=1) \n \nZindo.%s \n \n0 %s" %(home_dir ,file, currfile, Multiplicity))
        space = ("\n"*20)
        com_text = setup + "\n" + coords + space
        with open("%s/%s.com" %(home_dir, filename),"w") as f:
            f.write(com_text)

        subprocess.call("perl new.pl" , shell = True)
        subprocess.call("qsub %s/%s.sub" %(home_dir, filename), shell=True)

        count += 1
        

Zindosetup()
    

    
    

    

    
    
    
