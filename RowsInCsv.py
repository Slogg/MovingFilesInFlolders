import csv
import os
import re
import codecs
import LayoutString as LayStr

directory = None

def GetPath(directoryOut):
    global directory
    directory = directoryOut

def DetermineRowsInFile(adresse):
    try:
        f = codecs.open(adresse, "r", "utf_8_sig")
        reader = csv.reader(f)
        data = list(reader)
        row_count = len(data)
        return row_count
    finally:
        f.close()

def MoveToOtherFolder(i):
    global directory
    # adresse = re.sub(re.compile('/?$'), re.compile('\'), directory) + i
    adresse = directory + LayStr.PathWin + i
    replaced = re.sub(LayStr.PathAndEndWin, LayStr.PathWin  + 'Result' + LayStr.PathWin + str(DetermineRowsInFile(adresse)), directory)
    # replaced_adresse = re.sub(re.compile('[\/]?$'), re.compile('/'), replaced) + i
    replaced_adresse = replaced + LayStr.PathWin + i;
    if (os.path.isfile(replaced_adresse)):
        os.remove(replaced_adresse)
    ensure_dir(replaced_adresse)
    os.rename(adresse, replaced_adresse)

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)