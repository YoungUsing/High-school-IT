for cock in range(1, 20):
    for hen in range(1, 33):
        chick = 100 - cock - hen
        if (chick % 3 == 0) and (cock * 5 + hen * 3 + chick/3 == 100):
            print("cock: ", cock, " hen: ", hen, " chick: ", chick)