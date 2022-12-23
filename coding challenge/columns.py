def sort_csv_columns(csv_data: str) -> str:
  lines = csv_data.split('\n')

  column_names = lines[0].split(',')
  column_names.sort(key=lambda s: s.lower())
  data = []
  
  for line in lines[1:]:
    if line.strip() == '':
      continue
    data.append(line.split(','))

  sorted_data = []
  sorted_data.append(column_names)

  for row in data:
    sorted_row = []

    for column_name in column_names:
      index = lines[0].split(',').index(column_name)
      sorted_row.append(row[index])

    sorted_data.append(sorted_row)

  sorted_csv = '\n'.join([','.join(row) for row in sorted_data])

  return sorted_csv