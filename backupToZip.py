#! python3
#encoding: utf-8
# backupToZip.py: Copies an entire folder and its contents into
#a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    os.chdir(folder)
    folder = os.path.abspath(folder) # make sure folder is absolute

    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder)+ '_' + str(number) + '.zip'
        if not os.path.exists(os.path.join(folder,zipFilename)):
            break
        number += 1

    # Create the ZIP file.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(os.path.join(folder,zipFilename), 'a')

    # Walk the entire folder tree and compress the files in eacg folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        
        # Relative pathes don't create the roots folders in the ZIP.
        foldername = os.path.relpath(foldername)    # Work with relative dir.
                
        # Add the current folder to the ZIP file.
        if foldername != '.':   # Avoid the creation of teh folder '.'
            backupZip.write(foldername)
                

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder)+'_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue #don't backup the backups files.
            backupZip.write(os.path.join(foldername, filename))
##    print(backupZip.namelist())
    backupZip.close()
    print('Done.')

