import csv
data_list = []
temp = []
alpha = 0.1
total = 0
e = 0
temp_w = []
del_e = 0
pre_exp = 0
column_name = ['Dataset', 'No of Iteration', 'Learning Rate', 'Squared Error']
result = []
data_key = {}
value = 1
change_value = []


if __name__ == '__main__':
    output = open('result.csv', 'w', newline='')
    write = csv.writer(output)
    write.writerow(column_name)
    with open('fish.csv', 'r') as file:
        data = csv.reader(file)
        for i in data:
            data_list.append(i)
    w = [0.5] * len(data_list[0])
    pre = w[0]
    data_list_name = file.name.split('.').pop(0)

    for i in range(len(data_list[0])):
        if not data_list[1][i].replace('.', '').isdigit():
            change_value.append(data_list[0][i])

    for i in range(len(data_list[0])):
        if data_list[0][i] in change_value:
            for j in range(len(data_list)):
                if data_list[j][i] not in list(data_key.keys()) and data_list[j][i] not in change_value:
                    data_key[data_list[j][i]] = value
                    value += 1
        value = 1
    data_list.pop(0)
    for i in range(len(data_list[0])):
        for j in range(len(data_list)):
            if data_list[j][i] in list(data_key.keys()):
                data_list[j][i] = str(data_key[data_list[j][i]])

    for itr in range(20):
        result.append(data_list_name)
        result.append(itr+1)
        result.append(alpha)
        for i in range(len(data_list[0])):
            for j in range(len(data_list)):
                for k in range(len(data_list[0])-1):
                    pre = pre + (w[k+1] * float(data_list[j][k]))

                pre_exp = (pre - float(data_list[j][len(data_list[0])-1]))
                e = e + (pre_exp**2)/2
                del_e = pre_exp
                if i > 0:
                    del_e = del_e * float(data_list[j][i-1])
                total = total + del_e
                pre = w[0]
            temp_w.append(w[i]-alpha*total)
            total = 0
            temp = e
            e = 0
        result.append(temp)
        write.writerow(result)
        result.clear()
        w.clear()
        w = temp_w.copy()
        pre = w[0]
        temp_w.clear()
    file.close()
    output.close()
