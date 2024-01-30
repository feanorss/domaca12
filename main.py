class Queue:
  def __init__(self, maxfronta):
      self.list = []
      self.maxfronta = maxfronta

  def empty(self):
      return not bool(self.list)

  def full(self):
      return len(self.list) == self.maxfronta

  def engueue(self, hodnota):
      if not self.full():
          self.list.append(hodnota)
      else:
          print("Fronta je plna, nieje mozne pridat dalsie hodnoty ")

  def dequeue(self):
      if hodnota in self.list:
          self.list.remove(hodnota)
          print(f"Hodnota {hodnota} bola vymazana")
      else:
        print("Hodnota nie je v liste")

  def show(self):
      return (self.list)


class Character:
  def __init__(self, hodnota):
      self.hodnota = hodnota


def menu():
  print("")
  print("Menu: ")
  print("1. pridat ")
  print("2. ukazat ")
  print("3. je prazdna? ")
  print("4. Je plna? ")
  print("5. Vymazat hodnotu: ")
  print("6. Koniec ")


max_fronta = 2
my_queue = Queue(max_fronta)

while True:
  menu()
  volba = input("Zadaj volbu: ")
  if volba == '1':
      hodnota = input("Zadaj hodnotu :")
      my_queue.engueue(hodnota)

  elif volba == '2':
      print("Obsah fronty: ", my_queue.show())

  elif volba == '3':
      if my_queue.empty():
          print("Fronta je prazdna")
      else:
          print("Fronta nie je prazdna")

  elif volba == '4':
      if my_queue.full():
          print("Fronta je plna")
      else:
          print("Fronta nieje plna")

  elif volba == '5':
      if not my_queue.empty():
        hodnota = input("Zadaj hodnotu ktoru chces vymazat: ")
        my_queue.dequeue()
      else:
        print("Fronta je prazdna, nie je mozne odobrat hodnotu ")

  elif volba == '6':
      break

  else:
      print("neplatna volba")
