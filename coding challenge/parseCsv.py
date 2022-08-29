def parseCSV(csv, separator = ',', quote = '"'):
    data, row, value = [], [], []
    inString = False

    def pushValue():
        row.append(''.join(value))

    def pushRow():
        pushValue()
        data.append(row)

    for i in range(len(csv)):
        ch = csv[i]
        if inString:
            if ch == quote:
                if csv[i+1] == quote:
                    value.append(quote)
                    i += 1
                else:
                    inString = False
            else:
                value.append(ch)
        else:
            if ch == '\n':
                pushRow()
                row, value = [], []
            elif ch == separator:
                pushValue()
                value = []
            elif ch == quote:
                inString = True
            else:
                value.append(ch)
    pushRow()
    row, value = [], []
    return data