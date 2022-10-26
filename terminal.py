import inquirer
import os
    
#složka ve solici /diaglist    
folder = './i'

od = ""

while od == "":
    od = input("1. písmeno? ")

sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
sub_folders = sorted(sub_folders)
#print(sub_folders)

filtered = []

for firma in sub_folders:
    if firma.startswith(od):
        filtered.append(firma)

#print(filtered)

questions = [inquirer.List("size",message="Firma?",choices=filtered, ),]

answers = inquirer.prompt(questions)

#print(answers["size"])
firma = answers["size"]
akz = ""
while akz == "":
    akz = input("AKZ? ")
dbz = ""
while dbz == "":
    dbz = input("DBZ? ")
web = ""
while web == "":
    web = input("WB? ")

print(firma,akz,dbz,web)

