IP = [2 , 6 , 3 , 1 , 4 , 8 ,  5 , 7]

IP_1 = [4 , 1 , 3 , 5 , 7 , 2 , 8 , 6]

E_P = [4 , 1 , 2 , 3 , 2 , 3 , 4 , 1]

P10 = [3 , 5 , 2 , 7 , 4 , 10 , 1 , 9 , 8 , 6]

P8 = [6 , 3 , 7 , 4 , 8 , 5 , 10 , 9]

p4= [2 , 4 , 3 , 1]

S0 = [[01 , 11 , 00 , 11],[00 , 10 , 10 , 01],[11 , 01 , 01 , 11],[01 , 00 , 11 , 10]]

S1 = [[00 , 10 , 11 , 10],[10 , 00 , 00 , 10],[10 , 01 , 01 , 00],[11 , 11 , 00 , 11]]

def encrypt(pl, key):
    
    state = pl 
    
    skyes = g_sk(key)
    
    state = IP(state)

    state = fiestel(state,skeys)

    state = IP_1(state)

    ct = state

    return ct
def g_sk(key):
    
    key = P10(key)

    key_1 = key[:5]
    key_1_sh = key[:5]
    key_r = key[5:]
    key_r_sh = key[5:]
    for i in range(0, len(key_1)):
        key_1_sh[len(key_1)-(5-i)] = key_1[i]
    key = key_1_sh + key_r_sh    
    subkey_0 = P8 (key)

    
    key_1 = key[:5]
    key_1_sh = key[:5]
    key_r = key[5:]
    key_r_sh = key[5:]
    key = key_1_sh + key_r_sh    
    subkey_1 = P8 (key)


    return subkey_0, subkey_1


def fiestel(state,keys):

    state_1 = state[:4]
    state_r = state[4:]
    state_r = e_p(state_r)

def P10(input):
    output = ""
    p10 = [3 , 5 , 2 , 7 , 4 , 10 , 1 , 9 , 8 , 6]
    

    for i in range(10):
        for j in P10:
            output[i] = input[j]

    return output
def P8(input):
    output = ""
    P8 = [6 , 3 , 7 , 4 , 8 , 5 , 10 , 9]    

    for i in range(10):
        for j in P8:
            output[i] = input[j]

    return output

def ip(input):
    output = ""
    IP = [2 , 6 , 3 , 1 , 4 , 8 ,  5 , 7]

    for i in range(10):
        for j in IP:
            output[i] = input[j]


    return output

def IP_1(input):
    output = ""
    IP_1 = [4 , 1 , 3 , 5 , 7 , 2 , 8 , 6]

    for i in range(10):
        for j in IP_1:
            output[i] = input[j]


    return output
def e_p(input):
    output = ""
    E_P = [4 , 1 , 2 , 3 , 2 , 3 , 4 , 1]

    for i in range(10):
        for j in E_P:
            output[i] = input[j]


    return output
def p4(input):
    output = ""
    p4= [2 , 4 , 3 , 1]

    for i in range(10):
        for j in p4:
            output[i] = input[j]
    
    
    
    return output