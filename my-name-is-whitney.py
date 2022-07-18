frequency = []
years_list = []
name = 'Whitney'
gender = 'F'

for year in range(1970, 2010):
    filename = f'./data/yob{year}.txt'
    with open(filename) as file:
        lines = file.readlines()
    for line in lines:
        columns = line.strip().split(',')
        if columns[0] == name and columns[1] == gender:
            frequency.append(int(columns[2]))
            years_list.append(year)
