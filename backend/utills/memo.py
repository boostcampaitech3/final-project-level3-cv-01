import csv

def update_memo(responese):
    f = open('database.csv', 'r', encoding="utf-8")
    rd = csv.reader(f)
    for line in rd:
        if line[0] == responese[0]['date'] and line[3] == responese[0]['kind']:  # db에 해당 날씨 정보가 있을 때 일지 추가
            responese[0]['dbmemo'] = line[-1]
        if line[0] == responese[1]['date'] and line[3] == responese[1]['kind']:
            responese[1]['dbmemo'] = line[-1]
    f.close()
    return
    

def save_memo(memo):
    fr = open('database.csv', 'r', encoding="utf-8")  # read
    rd = csv.reader(fr)
    temp = []
    flag = True
    for line in rd:
        if memo.bug == line[3] and memo.date == line[0]:
            line[-1] = memo.memo
            flag = False
        temp.append(line)
    fr.close()
    if flag:
        temp.append([memo.date, memo.datetime, memo.crop, memo.bug, memo.weather, memo.memo])
    fw = open('database.csv', 'w', newline='', encoding="utf-8")  # write   
    wr = csv.writer(fw)
    for t in temp:
        wr.writerow(t)
    fw.close()
    return