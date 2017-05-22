__all__ = (
    'title',
    'play_game',
)

title = 'Game Module'
def play_game():
    print('Play game!')

def only_using_inside_game_module():
    print('I don\'t want import')

if __name__ == '__main__':
    play_game()

