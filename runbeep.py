import subprocess

repeat = 'y'
while repeat == 'y':
  subprocess.call(["beep.py"])
  repeat = raw_input("Deseja Executar Novamente ? (y/n) :")