import camelot

# class CPU:
#     pass


# class Register:
#     pass

tables = camelot.read_pdf('datasheet.pdf', pages='791-800')
print(tables)
print(tables[0].to_json('data.json'))