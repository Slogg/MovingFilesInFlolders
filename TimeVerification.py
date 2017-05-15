import threading
import ReceivingAllFiles
import os
import time

def ProcessFolder(directory):
    while(True):
        ReceivingAllFiles.GetFiles(directory)
