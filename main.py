with open('files.txt', 'w') as f:
  h = input(str("Enter any string ="))
  f.write(h)
with open('files.txt', 'r') as f:
  content = f.read()

  def count_words(s):
    return len(s.split())

  print(count_words(content))
