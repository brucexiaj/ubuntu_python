previousDir='/home/brucexiajun/Software/IDE'
currentDir='/home/brucexiajun/Software/IDE'
targetFile='youAge.sh'
currentFilesNum=0
currentDirFiles=os.listdir(currentDir)
currentDir=currentDir+"/"+currentDirFiles[0]
while True:
    if(os.path.isdir(currentDir)):
        currentDirFiles = os.listdir(currentDir)
        currentFilesTotalNum=len(currentDirFiles)
        if (currentFilesNum>=currentFilesTotalNum):
            currentDir = nextDir(currentDir)
            continue
        previousDir=currentDir
        currentDir = currentDir + "/" + currentDirFiles[currentFilesNum]
    elif(currentDirFiles[currentFilesNum]==targetFile):
        print currentDir
    else:
        currentDir=previousDir
        currentFilesNum+=1