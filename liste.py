tab = [1,9,4,3]

def echange(list) :
  sauvegarde = list[0]
  list[0] = list[-1]
  list[-1] = sauvegarde
  return list
