word = input("Choose word to be replaced: ")
new_word = input("Choose word to be replaced with: ")

def Count(search):
  f = open("datei.txt", "r")

  # data = f.read()
  # cont = data.count(search)

  cont = 0

  for line in f:
    line = line.strip()
    words = line.split(" ")
    for x in words:
      if x == search:
        cont += 1

  f.close()
  return cont

print(Count(word))

with open('datei.txt', 'r') as file:        # read in the file
  filedata = file.read()

filedata = filedata.replace(word, new_word)  # replace the target string

with open('datei.txt', 'w') as file:         # write file out
  file.write(filedata)

file.close()
