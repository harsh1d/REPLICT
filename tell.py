with open('examples.txt', 'r') as file:
  file.seek(5)
  print(content)
  print(file.tell())
