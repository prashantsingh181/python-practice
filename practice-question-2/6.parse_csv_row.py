def parse_csv_row(row):
    quotes = []
    result = []
    j = 0
    for i in range(len(row)):
        char = row[i]
        if char == '"' or char == "'":
            if len(quotes) > 0 and quotes[-1] == char:
                quotes.pop()
            else:
                quotes.append(char)
        elif char == "," and len(quotes) == 0 or i == len(row) - 1:
            word = row[j : i + 1] if i == len(row) - 1 else row[j:i]
            j = i + 1
            if word:
                result.append(word)
    return result


print(parse_csv_row("name,age,city"))
print(parse_csv_row('"Smith, John",30,London'))
