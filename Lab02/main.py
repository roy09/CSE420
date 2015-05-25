import re

with open("emails.txt") as input:
    for email in input:
        email = email.strip()
        fail = False
        name = ""
        domain = ""
        err = ""

        if len(email.split("@")) == 2:
            name, domain = email.split("@")
            if len(name) < 5:
                fail = True
        else:
            fail = True
            err = "no domain"

        if not str(domain) == "bracu.ac.bd":
            fail = True
            err = "invalid domain"

        if not fail:
            if name[0].isdigit() or name[0] == '_':
                fail = True
                err = "cannot have _ or numbers at the beginning"

        for i in name:
            if i.isdigit() or (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90) or i == '_' or i == '.':
                pass
            else:
                fail = True
                err = "false char"
                break


        print email + " " +  str(not fail) + " " + err
