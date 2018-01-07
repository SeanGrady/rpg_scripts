from random import randrange
from npc_generator import generator as npc_gen


def roll_on_generator(generator=npc_gen, table_number=None):
    while True:
        output = generator['name'] + '\n'
        results = {
            number: make_line(
                number,
                roll_on_table(table['table']),
                table['name'],
            )
            for (number, table) in generator['tables'].items()
        }
        text_block = make_text_block(results)
        print(text_block)
        resp = input('===>')

        while resp:
            table_id = int(resp)
            table = generator['tables'][table_id]
            table_name = table['name']
            table_list = table['table']
            new_roll = roll_on_table(table_list)
            results[table_id] = make_line(table_id, new_roll, table_name)
            text_block = make_text_block(results)
            print(text_block)
            resp = input('===>')


def make_line(number, roll, name):
    line = (
        str(number) + ') ' + name
        + ':\n'
        + roll
        + '\n\n'
    )
    return line


def make_text_block(results):
    strings = [string for id, string in results.items()]
    text_block = ''.join(strings)
    reroll_text = (
        'Enter table number to reroll one table '
        'or nothing to reroll generator.'
    )
    text_block += reroll_text
    return text_block


def roll_on_table(table):
    size = len(table)
    roll = randrange(size)
    line = []
    result = table[roll]
    parts = result.strip().split(';')
    prefix = parts[0]
    line.append(prefix)
    if len(parts) > 1:
        reroll_instructions = parts[1]
        if reroll_instructions.strip() == 'reroll on 1d4':
            roll = randrange(4)
            prefix = table[roll]
            line.append(prefix)
        elif reroll_instructions.strip() == 'reroll for it':
            roll_2 = roll
            while roll_2 == roll:
                roll_2 = randrange(size)
            result = table[roll_2]
            line.append(result)

    if len(line) > 1:
        rolled_result = ': '.join(line)
    else:
        rolled_result = line[0]
    return rolled_result
