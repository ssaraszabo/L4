def logic(player, calc):
    s = 0
    if player == 1:
        if calc == 'stein':
            s = -1
        elif calc == 'papier':
            s = 1                 #apar toate combinatiile de alegere, mai putin cele identice
    elif player == 2:
        if calc == 'schere':
            s = 1
        elif calc == 'papier':
            s = -1
    elif player == 3:
        if calc == 'schere':
            s = -1
        elif calc == 'stein':
            s = 1
    return s
