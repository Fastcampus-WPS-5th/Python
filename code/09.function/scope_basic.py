champion = 'Lux'

def show_global_champion():
    print('show_global_champion : {}'.format(champion))
    print('show_global_champion id: {}'.format(id(champion)))

def change_global_champion():
    #print('before_change_global_champion : {}'.format(champion))
    champion = 'Ahri'
    print('local scope champion id: {}'.format(id(champion)))
    print('after_change_global_champion : {}'.format(champion))
    print('change_global_champion locals(): {}'.format(locals()))
    print('change_global_champion globals(): {}'.format(globals()))

show_global_champion()
change_global_champion()
print('print_champion : {}'.format(champion))
print('print_champion id: {}'.format(id(champion)))
print('print_locals(): {}'.format(locals()))
