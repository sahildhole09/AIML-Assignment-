import os
import hashlib

#########################################################################
# Function Name : CalculateChecksum
# Description   : Calculate MD5 checksum of file
#########################################################################

def CalculateChecksum(FileName):
    try:
        fobj = open(FileName, "rb")

        hobj = hashlib.md5()

        Buffer = fobj.read(1024)

        while len(Buffer) > 0:
            hobj.update(Buffer)
            Buffer = fobj.read(1024)

        return hobj.hexdigest()

    except Exception:
        return None


#########################################################################
# Function Name : FindDuplicate
# Description   : Find duplicate files
#########################################################################

def FindDuplicate(DirectoryName):

    Duplicate = {}
    TotalFiles = 0

    Ret = os.path.exists(DirectoryName)
    if(Ret == False):
        raise Exception("Directory does not exist.")

    Ret = os.path.isdir(DirectoryName)
    if(Ret == False):
        raise Exception("Invalid directory.")

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for File in FileNames:
            FilePath = os.path.join(FolderName, File)
            try:
                Checksum = CalculateChecksum(FilePath)
                if Checksum is None:
                    continue
                TotalFiles += 1

                if Checksum in Duplicate:
                    Duplicate[Checksum].append(FilePath)
                else:
                    Duplicate[Checksum] = [FilePath]

            except Exception:
                pass

    return Duplicate, TotalFiles


#########################################################################
# Function Name : DeleteDuplicate
# Description   : Delete duplicate files
#########################################################################

def DeleteDuplicate(DirectoryName):

    Duplicate, TotalFiles = FindDuplicate(DirectoryName)

    DeletedFiles = []
    DuplicateCount = 0

    for Checksum in Duplicate:
        Files = Duplicate[Checksum]

        if len(Files) > 1:
            DuplicateCount = DuplicateCount + len(Files) - 1

            # Keep first file
            for File in Files[1:]:
                try:
                    os.remove(File)

                    DeletedFiles.append({
                        "File": File,
                        "Checksum": Checksum
                    })

                except Exception:
                    pass

    return {
        "TotalFiles": TotalFiles,
        "DuplicateFiles": DuplicateCount,
        "DeletedFiles": DeletedFiles
    }