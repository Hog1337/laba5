def search(list, val):
    for i in range(len(list)):
        if list[i][0] == val:
            return i
    return -1

def create(list):
    list_1 = []
    for i in range(len(list)):
        ind = search(list_1, list[i])
        if ind > -1:
            list_1[ind][1] += 1
        else:
            list_1.append([list[i], 1])
    for i in range(len(list_1)):
        list_1[i][1] /= len(list)
    return list_1

def vinzoring(list):
    for i in range(len(list)):
        if list[i] == []:
            ind = -1
            ind_next = i
            ind_priv = i
            while True:
                ind_next += 1
                ind_priv -= 1
                if ind_next < len(list) and list[ind_next] != []:
                    ind = ind_next
                    break
                if ind_priv >= 0 and list[ind_priv] != []:
                    ind = ind_priv
                    break
            list[i] = list[ind]

def linear_approximation(list):
    for i in range(len(list)):
        if list[i] == []:
            ind_next = i
            ind_priv = i
            while True:
                ind_next += 1
                if ind_next >= len(list) or list[ind_next] != []:
                    break
            while True:
                ind_priv -= 1
                if ind_priv < 0 or list[ind_priv] != []:
                    break
            if ind_next >= len(list):
                ind_next = ind_priv - 1
                while True:
                    if ind_next >= 0 and list[ind_next] != []:
                        break
                    ind_next -= 1
            if ind_priv < 0:
                ind_priv = ind_next + 1
                while True:
                    if ind_priv < len(list) and list[ind_priv] != []:
                        break
                    ind_priv += 1
            if list[ind_priv] == list[ind_next]:
                list[i] = list[ind_next]
            else:
                a = (ind_priv - ind_next) / (list[ind_priv] - list[ind_next])
                b = ind_next - a * list[ind_next]
                list[i] = (i - b)/a

def correlation_recovery(list_A, list_B):
    for i in range(len(list_A)):
        if list_A[i] == []:
            ind = -1
            ind_next = i
            ind_priv = i
            while True:
                ind_next += 1
                ind_priv -= 1
                if ind_next < len(list_A) and list_A[ind_next] != []:
                    ind = ind_next
                    break
                if ind_priv >= 0 and list_A[ind_priv] != []:
                    ind = ind_priv
                    break
            list_A[i] = (list_B[i]/list_B[ind])*list_A[ind]