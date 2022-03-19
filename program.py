def encrypts(word:str, key:int):
    huruf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    kata = word.lower()
    key = int(key)

    #tampung angka
    index=list()

    #encrypts
    encr=list()

    huruf_in_kata = list(kata)
    for karakter in huruf_in_kata:
        try:
            angka = huruf.index(karakter) + key
            if (angka>25):
                angka=angka-26
            index.append(angka)
        except:
            index.append(karakter)

    for enc in index:
        try:
            encr.append(huruf[enc])
        except:
            encr.append(enc)
    pr = "".join(encr)
    return pr.upper()


def decrypts(word:str, keys:int):
    huruf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']

    kata = word.lower()
    key = int(keys)

    # tampung angka
    index = list()

    # encrypts
    encr = list()

    huruf_in_kata = list(kata)
    for karakter in huruf_in_kata:
        try:
            angka = huruf.index(karakter) - key
            if (angka < 0):
                angka = angka + 26
            index.append(angka)
        except:
            index.append(karakter)

    for enc in index:
        try:
            encr.append(huruf[enc])
        except:
            encr.append(enc)
    pr = "".join(encr)
    return pr.upper()


