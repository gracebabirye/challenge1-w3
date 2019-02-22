def missingnumbers(listb):
    try:
        if type(listb) is list:
            maxVal = max(listb)
            minVal = min(listb)
            missing_list = []

            for x in range(minVal, maxVal):
                if x not in listb:
                    missing_list.append(x)
            return (missing_list)
        else:
            return('Invalid Input')
    except ValueError:
        return('Invalid Input')