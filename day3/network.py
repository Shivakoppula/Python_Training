import pprint

def f1():
    network_params = {} # empty dict
    return network_params

def f2(network_params):
    with open('network.cfg','r') as fobj:
        for var in fobj.readlines():
            var = var.strip() # remove \n
            K,V = var.split("=")
            network_params[K] = V # adding new data to dict
    return network_params

def f3(network_params):
    pprint.pprint(network_params)

def f4(network_params):
    network_params['Interface'] = 'eth1'
    network_params['bootproto'] = 'static'
    network_params['onboot'] = 'yes'
    network_params['IPADD'] = '192.168.1.10'
    network_params['PREFIX'] = 24
    network_params['DNS1']= '122.33.344.555'
    return network_params

def f5(network_params):
    with open('new_network.cfg','w') as wobj:
        for var in network_params:
            wobj.write(f'{var} = {network_params.get(var)}\n')


rv1 = f1()
rv2 = f2(rv1)
f3(rv2)
rv3 = f4(rv2)
print("\nUpdated network details:-")
f3(rv3) 
f5(rv3)