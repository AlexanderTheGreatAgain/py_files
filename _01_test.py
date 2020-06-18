'''Aufgabe von Ivan:
  Marius und Jakob testen Docker und GitHub mit 2 verschiedenen
  Containern. Jakob testet code mit Python 3.7 in seinem container.
  Marius 2.7. Jakob hat dafür mit Anaconda neues env erstellt, das
  er dann in den container kopiert
'''
import sys

version = sys.version
print("hello docker world,
print("this is Python")
print("of version", version)
