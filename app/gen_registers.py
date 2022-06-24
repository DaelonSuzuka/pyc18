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
    tables = camelot.read_pdf('datasheet.pdf', pages='873-887')
    tables.export('data/registers.json', f='json')


def generate_json():
    files = [f.as_posix() for f in Path('data').rglob('registers-page*.json')]
    data = []

    for name in files:
        with open(name) as f:
            d = json.loads(f.read())
            for row in d:
                # if '\n' in row['0']:
                #     continue
                # if '.' in row['0']:
                #     continue
                # if ' ' in row['0']:
                #     continue

                data.append(row)

    with open('data/registers-raw.json', 'w') as f:
        f.write(json.dumps(data, indent=4))


def reprocess_opcode_data():
    with open('data/registers-raw.json') as f:
        data = json.loads(f.read())

    registers = []

    # register = {
    #     'address': '',
    #     'name': '',
    #     'operands': '',
    #     'description': '',
    #     'cycles': '',
    #     'status': '',
    # }

    for i, d in enumerate(data):
        if '\n' in d['0']:
            continue
        if '.' in d['0']:
            continue
        if ' ' in d['0']:
            continue
        if not d['1']:
            continue
        if d['1'] == 'Reserved':
            continue

        register = {
            'address': d['0'],
            'name': d['1'],
            'bits': []
        }

        for i in range(3, 10):
            try:
                if d[str(i)]:
                    register['bits'].append(d[str(i)])
            except:
                break

        
        try:
            if data[i + 1]['0'] == '':
                for i in range(3, 10):
                    try:
                        if d[str(i)]:
                            register['bits'].append(data[i + 1][str(i)])
                    except:
                        break
                if data[i + 2]['0'] == '':
                    for i in range(3, 10):
                        try:
                            if d[str(i)]:
                                register['bits'].append(d[str(i)])
                        except:
                            break
        except:
            pass


        # register['bits'].append()


        registers.append(register)

    with open('data/registers.json', 'w') as f:
        f.write(json.dumps(registers, indent=4))

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
    reprocess_opcode_data()
    # generate_classes()

    pass