import csv
import os
import RowsInCsv
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from time import time as tt
import time


def GetFiles(directory):
    n = 10000;
    i=0;
    filesArray = []
    files = os.listdir(directory)
    filesA = list(filter(lambda x: x.endswith('.csv'), files))
    if(len(filesA)==0):
        print("Файлов пока нет")
        time.sleep(10)
    elif(len(filesA)<n):
        filesArray = filesA
        print("Добавлено " + str(len(filesArray)))
    else:
        while i < n:
            filesArray.append(filesA[i])
            i+=1
        print("Добавлено " + str(len(filesArray)))

    RowsInCsv.GetPath(directory)
    tic = tt()
    for i in filesArray:
        RowsInCsv.MoveToOtherFolder(i)
    # pool = ThreadPool(10)
    # try:
    #     pool.map(RowsInCsv.MoveToOtherFolder, filesArray)
    #     pool.close()
    #     pool.join()
    # except:
    #     print("Lol")
    toc = tt()
    print(toc - tic)


