



def DefanginganIPAddress(address):
    newList = []
    for char in address.split('.'):
        newList += [char]

    return '[.]'.join(newList)
    # return address.replace('.', '[.]')


address = "1.1.1.1"
print(DefanginganIPAddress(address))