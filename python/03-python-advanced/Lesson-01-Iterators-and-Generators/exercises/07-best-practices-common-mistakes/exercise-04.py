with open("products.txt","r") as file:
        data = file.readlines()

#will strore all the lines in once.

for line in data:
    print(line.strip())

print("=============================")

with open("products.txt","r") as file:
        for line in file:
            print(line.strip())

#Python reads one line at a time, making this very memory-efficient for large files.
