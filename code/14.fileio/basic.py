skills = '''Illumination
Light Binding
Prismatic Barrier
Lucent Singularity
Final Spark'''

len(skills)

f = open('skills.txt', 'wt')
f.write(skills)
f.close()

try:
    f = open('skills.txt', 'xt')
except FileExistsError:
    print('File is already exist')
print('Program terminate')

f = open('skills.txt', 'rt')
skills = f.read()
f.close()
print(skills)

f = open('skills.txt', 'rt')
fl = f.readlines()
print(fl)