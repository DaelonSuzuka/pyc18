import camelot
from pathlib import Path
import json
from dotmap import DotMap


class Writer:
    def __init__(self, out):
        self.out = out
        self.indent = 4
        self.level = 0

    def __iadd__(self, other):
        self.line(other)
        return self

    def raw(self, string):
        self.out(string)

    def line(self, string=''):
        if string:
            self.out(' ' * self.indent * self.level + string + '\n')
        else:
            self.out('\n')

    def __call__(self, string=''):
        self.out(' ' * self.indent * self.level + string)
    
    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, *_):
        self.level -= 1


def read_pdf():
    tables = camelot.read_pdf('datasheet.pdf', pages='791-795')
    tables.export('data/opcodes.json', f='json')


def generate_json():
    files = [f.as_posix() for f in Path('data').rglob('opcodes-page*.json')]
    data = []

    for name in files:
        with open(name) as f:
            d = json.loads(f.read())
            for row in d:
                if '\n' in row['0']:
                    continue
                if '.' in row['0']:
                    continue
                if ' ' in row['0']:
                    continue

                data.append(row)

    with open('data/opcodes-raw.json', 'w') as f:
        f.write(json.dumps(data, indent=4))


def reprocess_opcode_data():
    with open('data/opcodes-raw.json') as f:
        data = json.loads(f.read())

    opcodes = []

    # opcode = {
    #     'name': '',
    #     'operands': '',
    #     'description': '',
    #     'cycles': '',
    #     'status': '',
    # }

    for i, d in enumerate(data):
        if not d['0']:
            continue

        opcode = {
            'name': d['0'],
            'operands': d['1'],
            'description': d['2'],
            'cycles': d['3'],
            'word' : {
                '0': d['4'],
                '1': d['5'],
                '2': d['6'],
                '3': d['7'],
            },
            'status': d['8'],
        }

        try:
            if data[i + 1]['0'] == '':
                opcode['word']['4'] = data[i + 1]['4']
                opcode['word']['5'] = data[i + 1]['5']
                opcode['word']['6'] = data[i + 1]['6']
                opcode['word']['7'] = data[i + 1]['7']
                if data[i + 2]['0'] == '':
                    opcode['word']['8'] = data[i + 2]['4']
                    opcode['word']['9'] = data[i + 2]['5']
                    opcode['word']['10'] = data[i + 2]['6']
                    opcode['word']['11'] = data[i + 2]['7']
                    if data[i + 3]['0'] == '':
                        opcode['word']['12'] = data[i + 3]['4']
                        opcode['word']['13'] = data[i + 3]['5']
                        opcode['word']['14'] = data[i + 3]['6']
                        opcode['word']['15'] = data[i + 3]['7']
        except:
            pass

        opcodes.append(opcode)

    with open('data/opcodes.json', 'w') as f:
        f.write(json.dumps(opcodes, indent=4))

def generate_classes():
    with open('data/opcodes.json') as f:
        opcodes = json.loads(f.read())

    with open('opcodes.py', 'w') as f:
        w = Writer(f.write)

        w += '# test line'

        for op in opcodes:
            op = DotMap(op)

            w += ''
            w += f"class {op.name}:"
            with w:

                w += f"# {op.description}"
                w += f"# operands: {op.operands}"
                w += f"# cycles: {op.cycles}"
                w += f"# affected status bits: {op.status}"
                w += ''
                w += f"cycles = {op.cycles}"
                w += ''
                w += "def __init__(self):"
                with w:
                    w += 'pass'

        w += ''

if __name__ == '__main__':
    # read_pdf()
    # generate_json()
    # reprocess_opcode_data()
    generate_classes()

    pass