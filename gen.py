import os, transliterate, random, time

words_file = "" # Dictionary file

words = []
special = ["@","%","!","#","$","?","(",")","~","&"]

with open(words_file,'r') as f:
    for line in f:
        line = line.strip()
        words.append(line)

f.close()

word1 = random.choice(words)
word2 = random.choice(words)
word3 = random.choice(words)

i1 = str(random.randint(1,9))
i2 = str(random.randint(1,9))
i3 = str(random.randint(10,99))

spec = random.choice(special)

password = (transliterate.translit(word1.title(), reversed=True)[:4] + i1 + transliterate.translit(word2.title(), reversed=True)[:4] + i2 + transliterate.translit(word3.title(), reversed=True)[:4] + i3 + spec)
rem = word1 + " " +i1 + " " + word2 + " " + i2 + " " + word3 + " " + i3+spec

print(password)
print(rem)