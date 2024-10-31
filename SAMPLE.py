def countUniqueWords(filename):
  file = open(fileName,"r")
  read_file=file.read()
  words_in_file=read_file.split()
  count_map={}
  
  for i in words_in_file:
    if i in count_map:
      count_map[i]+=1
    else:
      count_map[i]=1
  count=0

  for i in count_map:
    if count_map[i]==1:
      count+=1
  file.close()
  return count
  
with open("SAMPLE.txt","w") as file:
  file.write("hello deep how")

print("Number of unique words in file are:",countUniqueWords("SAMPLE.txt")