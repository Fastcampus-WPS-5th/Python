import re

story = '''Born to the prestigious Crownguards, the paragon family of Demacian service, Luxanna was destined for greatness. She grew up as the family's only daughter, and she immediately took to the advanced education and lavish parties required of families as high profile as the Crownguards. As Lux matured, it became clear that she was extraordinarily gifted. She could play tricks that made people believe they had seen things that did not actually exist. She could also hide in plain sight. Somehow, she was able to reverse engineer arcane magical spells after seeing them cast only once. She was hailed as a prodigy, drawing the affections of the Demacian government, military, and citizens alike.

As one of the youngest women to be tested by the College of Magic, she was discovered to possess a unique command over the powers of light. The young Lux viewed this as a great gift, something for her to embrace and use in the name of good. Realizing her unique skills, the Demacian military recruited and trained her in covert operations. She quickly became renowned for her daring achievements; the most dangerous of which found her deep in the chambers of the Noxian High Command. She extracted valuable inside information about the Noxus-Ionian conflict, earning her great favor with Demacians and Ionians alike. However, reconnaissance and surveillance was not for her. A light of her people, Lux's true calling was the League of Legends, where she could follow in her brother's footsteps and unleash her gifts as an inspiration for all of Demacia.'''

# 1번
result = re.findall(r'\ba\w{3}\b', story)

# 2번
result = re.findall(r'\w*r\b', story)

# 3번
result = re.findall(r'\w*[abcde]{3}\w*', story)


# 4번
def re_change(m):
    return '{}{}[{}]'.format(m.group('before').upper(), m.group('center'), m.group('after'))


p = re.compile(r'(?P<before>\w+)(?P<center>\s*,\s*)(?P<after>\w+)')
result = re.sub(p, re_change, story)
# re_change부분을 lambda함수로 만들어보세요


print(result)
