import os, sys
import glob
import subprocess

def ExtractMO():

    count = 10
    home_dir = os.getcwd()
    print "Rot or Trans? Which Axis?:"
    action = raw_input()
    print "Which Molecule?:"
    system = raw_input()
    print "How Many Versions?:"
    versions = raw_input()


    subprocess.call("mkdir Overlap", shell = True) #create a new directory to store MO files
    
    while count <= int(versions):
        file = action+ system + str(count)
        currfile = system + str(count)
        with open("%s/%s.out" %(home_dir, file), "r") as f:
            text = f.read()
            overlapstart = text.find("*** Overlap ***")
            overlapend = text.find("*** Kinetic Energy ***")
            overlap = text[overlapstart+15:overlapend]
            with open("%s/Overlap/%s.txt" %(home_dir, currfile), "w") as f:
                f.write(overlap)
        count += 1
        
    
ExtractMO()
