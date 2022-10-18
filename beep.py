# from tkinter import *
# window = Tk()
# window.title("Powos Timer App")
# window.mainloop()

import winsound
import time

def my_function():

  trinta = 1050  # Set Frequency To 2500 Hertz
  tresmin = 1600
  cincomin = 600
  duration = 600  # Set Duration To 1000 ms == 1 second

  time.sleep(30)
  winsound.Beep(trinta, duration)
  print("30 segundos!")
  time.sleep(150)
  winsound.Beep(tresmin, duration)
  print("3 minutos!")
  time.sleep(120)
  winsound.Beep(cincomin, duration)
  print("5 minutos, seu tempo acabou.")

while True:
  var = input("Tecle (ENTER) para executar o programa Beep: ")
  if var == '':
    my_function()
  else:
    break