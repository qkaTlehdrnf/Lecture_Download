def url_number_None(url,digit):
    i=0
    while True:
        i+=-1
        try:
            int(url[i])
            last_int=i
            while True:
                i+=-1
                try:
                    int(url[i])
                    first_int=i
                except BaseException:
                    first_int=i+1
                    break
                    pass
            break
        except BaseException:
            pass
    url_f=url[0:int(first_int)]+digit+url[last_int+1:]
    return url_f,first_int,last_int
