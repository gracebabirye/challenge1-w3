def list_sort(lista):
    dict = {'evens': [], 'odds': [], 'chars': []}
    if type(lista) is list:
        if len(lista) == 0:
            return dict
        else:
            for i in lista:
                if(type(i) == str):
                    dict['chars'].append(i)
                else:
                    if(i % 2 == 0):
                        dict['evens'].append(i)
                    else:
                        dict['odds'].append(i)
            dict['chars'].sort()
            dict['evens'].sort()
            dict['odds'].sort()
            return dict
    else:
        return('Invalid Input')