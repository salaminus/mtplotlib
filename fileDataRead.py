def readDataFile():
    f = open('20046.dat', 'r')
    data = []
    counter = 1
    for s in f.readlines()[:10]:
        temp = s.split()
                    # станция, год, месяц, день, час, напр ветра, осадки, темпер-ра, влажность
        data.append([temp[0], temp[5], temp[6], temp[7], temp[10], float(temp[39]), float(temp[47]), float(temp[-31]), float(temp[-15])])
        print([temp[0], temp[5], temp[6], temp[7], temp[10], float(temp[39]), float(temp[47]), float(temp[-31]), float(temp[-15])])
    return data