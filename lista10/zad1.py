import re

myEmail = "python2020@gusun_tomail.com"
myWord = "usun.to"

def delete(email, word):
    startIndex = re.search(word, email).start()
    endIndex = re.search(word, email).end()
    output = ""

    for i in range(0, len(email)):
        if ((i >= startIndex) and (i < endIndex)):
            pass
        else:
            output = output + email[i]

    return output

print(delete(myEmail, myWord))