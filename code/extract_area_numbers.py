import pandas as pd

tables = pd.read_html('https://www.ssa.gov/employer/stateweb.htm', thousands='$')

final = pd.DataFrame(columns=['area_number', 'location'])

def funct(x):
    global final
    for y in x['SSN Area Number'].split(','):
        print(y)
        for z in range(int(y.split('-')[0]), (int(y.split('-')[1]) if '-' in y else int(y.split('-')[0]))  +1):
            final = final.append({'area_number':f'{z:03}', 'location': x['Location']}, ignore_index=True)

tables[0].apply(lambda x: funct(x), axis=1)

final['location'] = final['location'].replace('Railroad Board**', 'Railroad Board')

final.to_csv('area_numbers.csv', index=False)