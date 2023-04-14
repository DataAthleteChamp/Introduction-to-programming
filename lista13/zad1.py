def format_bytes(a):
    bajty=0
    kilobajty=0
    megabajty=0
    gigabajty=0

    bajty = a % 1024
    kilobajty = (a - bajty)/1024
    if (kilobajty>=1024):
        megabajty = (kilobajty - (kilobajty % 1024))/1024
        kilobajty = kilobajty % 1024
        if (megabajty>=1024):
            gigabajty = (megabajty - megabajty % 1024)/1024
            megabajty = megabajty % 1024
    print(f"giga: {int(gigabajty)}, mega: {int(megabajty)}, kilo: {int(kilobajty)}, bajty: {int(bajty)}")

format_bytes(9876543210)

