import string
import re

source = 'Lux, the Lady of Luminosity'
'%Lady%'
m = re.match('Lux', source)
m = re.match('.*Lady', source)
m = re.search('o', source)
m = re.match(r'(.*)(Lady)(.*)', source)
l = re.findall('y.?.?', source)

printable = string.printable

'y{3, 10}'
'yyy ~ yyyyyyyyy')

# print(printable)
# print(re.findall('\w', printable))
# print(re.findall('\W', printable))
# print(re.findall('\d', printable))
# print(re.findall('\D', printable))
# print(re.findall(r'\s', printable))
# print(re.findall(r'\S', printable))
# print(re.findall(r'\b', printable))
# print(re.findall(r'\B', printable))

import re
story = '''Born to the prestigious Crownguards, the paragon family of Demacian service, Luxanna was destined for greatness. She grew up as the family's only daughter, and she immediately took to the advanced education and lavish parties required of families as high profile as the Crownguards. As Lux matured, it became clear that she was extraordinarily gifted. She could play tricks that made people believe they had seen things that did not actually exist. She could also hide in plain sight. Somehow, she was able to reverse engineer arcane magical spells after seeing them cast only once. She was hailed as a prodigy, drawing the affections of the Demacian government, military, and citizens alike.

As one of the youngest women to be tested by the College of Magic, she was discovered to possess a unique command over the powers of light. The young Lux viewed this as a great gift, something for her to embrace and use in the name of good. Realizing her unique skills, the Demacian military recruited and trained her in covert operations. She quickly became renowned for her daring achievements; the most dangerous of which found her deep in the chambers of the Noxian High Command. She extracted valuable inside information about the Noxus-Ionian conflict, earning her great favor with Demacians and Ionians alike. However, reconnaissance and surveillance was not for her. A light of her people, Lux's true calling was the League of Legends, where she could follow in her brother's footsteps and unleash her gifts as an inspiration for all of Demacia.'''

