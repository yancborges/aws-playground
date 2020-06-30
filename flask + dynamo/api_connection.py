with open(
    'C://Users//Yan//Desktop//Scripting//save api keys here, dummy//genius.txt', 
    'r'
) as f:

    data = f.readlines()
    data = [line.split('=') for line in data]

    genius_keys = {
        'client': data[0],
        'client_secret': None,
        'acess_token': data[2]
    }
