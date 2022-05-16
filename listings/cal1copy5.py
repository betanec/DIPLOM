for table in soup.find_all('table'):
        try:    
            if 'table-striped' in table['class']:
                parsed = [[i] for i in [i.text for i in table.find_all('p')]]
        except KeyError:
            pass