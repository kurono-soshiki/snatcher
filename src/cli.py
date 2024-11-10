import argparse
from character import Character

def main():
    parser = argparse.ArgumentParser(description='Snatcher CLI')
    
    # Add arguments here
    parser.add_argument('--example', type=str, help='Example argument')

    args = parser.parse_args()

    # 対話コンソールを開始
    print('Welcome to Snatcher!')
    character_id = input('Please enter your character ID: ')
    chara = Character.get_character(character_id)
    if chara is None:
        print('Character not found')
        return
    
    print(f'Character: {chara.name}')
    print('You can type "exit" to quit the chat.')
    print('')

    input_text = input('You> ')
    while input_text != 'exit':
        response = chara.answer(input_text)
        print(f'{chara.name}> {response}')
        input_text = input('You> ')
        
    print('Goodbye!')

if __name__ == '__main__':
    main()