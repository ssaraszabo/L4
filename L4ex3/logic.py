def logic(player, calc):
    if player == 1:
        if calc == 'stein':
            return False
        elif calc == 'papier':
            return True                 #apar toate combinatiile de alegere, mai putin cele identice
    elif player == 2:
        if calc == 'schere':
            return True
        elif calc == 'papier':
            return False
    elif player == 3:
        if calc == 'schere':
            return False
        elif calc == 'stein':
            return True

def test(player, calc):
    if player == 1:
        if calc == 'schere':
            return False
    elif player == 2:               #verifica daca calculatorul si jucatorul au ales acelasi lucru
        if calc == 'stein':
            return False
    elif player == 3:
        if calc == 'papier':
            return False
    else:
        return True