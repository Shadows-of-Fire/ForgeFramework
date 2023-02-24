import os
import subprocess

def mkdir(name):
    if not os.path.exists(name):
        os.mkdir(name)

def rename(old, new):
    if os.path.exists(old):
        os.rename(old, new)

properties = {}
with open("gradle.properties") as propFile:
    for line in propFile:
        name, var = line.partition("=")[::2]
        properties[name.strip()] = var.strip()

modid = properties['modid']
fileName = properties['fileName'] + '.java'

print('Running initial setup for project ' + modid)

os.chdir('src/main/java/shadows')
rename('modid', modid)
os.chdir(modid)

rename('ModClassRename.java', fileName)

with open(fileName, 'r') as mainModClass:
    data = mainModClass.read()

data = data.replace('modid', modid)
data = data.replace('ModClassRename', properties['fileName'])

with open(fileName, 'w') as mainModClass:
    mainModClass.write(data)

os.chdir('../../../resources')
rename('modid.mixins.json', modid + '.mixins.json')

mkdir('data')
os.chdir('data')
mkdir(modid)
os.chdir(modid)
mkdir('recipes')
mkdir('advancements')
mkdir('loot_tables')
mkdir('structures')
mkdir('tags')
os.chdir('../..')

mkdir('assets')
os.chdir('assets')
mkdir(modid)
os.chdir(modid)
mkdir('blockstates')
mkdir('lang')
with open('lang/en_us.json', 'w') as langFile:
    langFile.write('{\n}')

mkdir('models')
mkdir('textures')
os.chdir('../..')

os.chdir('../../..')
process = subprocess.Popen('setup.bat')
output, error = process.communicate()
process = subprocess.Popen(["git", "checkout", "-b", properties['mcVersion']], stdout=subprocess.PIPE)
output, error = process.communicate()