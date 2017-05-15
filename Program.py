import ReceivingAllFiles
import TimeVerification
from time import time

print("Введите путь к папке с файлами *.csv")
directory = input()
TimeVerification.ProcessFolder(directory)
