import os,sys
import glob
import subprocess

    

#Once you Are back to Home: It looks like ../../../scratch2/sd/abregman/g09/
def ExtractMOs(Path_To_MOs):
    count = 0
    home_dir = os.getcwd()
    subprocess.call("mkdir MOs", shell = True) #create a new directory to store MO files
    curr_dir = home_dir
    print "Rot or Trans? Which Axis?:"
    action = raw_input()
    print "Which Molecule?:"
    system = raw_input()
    print "How Many Verisons?:"
    versions = raw_input()

    

    ## HOW TO NAVIGATE TO THE SCRATCH 2 Directory?
    while count <= int(versions):
        filename = action + system +'iso' + str(count)
        currfile = system + str(count)

        # Move into to correct folder
        subprocess.call("cp %s/fort.7 MOs/%s" %(Path_To_MOs,currfile), shell =True)
        count += 1
    
ExtractMOs(of Path)
