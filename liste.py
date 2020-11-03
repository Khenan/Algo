tab = [1,9,4,3]

# Fonction qui permet d'echanger le premier et le dernier element d'une liste
def echange(list) :
  sauvegarde = list[0]
  list[0] = list[-1]
  list[-1] = sauvegarde
  return list
