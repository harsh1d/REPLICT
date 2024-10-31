def process_file(filename):
  with open(filename, 'r') as f:
    content = f.read()

    def count_words(s):
      return len(s.split())

    print(count_words(content))
