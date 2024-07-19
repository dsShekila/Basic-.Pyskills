def checkIfNotNumeric(L):
  for x in L:
    if not(isinstance(x, (int,float))):
      return False
  return True

def addAllNumerics(*args):
  s = 0
  for x in args:
    s += x
  return s

MyName = "Phython course"
