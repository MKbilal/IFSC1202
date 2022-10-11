def Propercase(s):
    str = ''
    str += s[0].upper()
    for i in range(1, len(s)):
        str += s[i].lower()
    s = str
    return s

def Trim(s):
    res = s.strip()
    if(len(res)>0):
        res = Propercase(res)
        return res
    else:
        return res

def FirstName(s):
    ind = s.find(" ")
    firstname = Trim(s[:ind])
    return firstname

def LastName(s):
    ind = s.rfind(" ")
    lastname = Trim(s[ind+1:])
    return lastname

def MiddleName(s):
    first = s.find(' ')
    last = s.rfind(' ')
    if last - first == 0:
        return ""
    elif last - first == 2:
        return Propercase(Trim(s[first+1:last])) + "."
    else:
        return Propercase(Trim(s[first+1:last]))

file1 = open("07.11 Names.txt")

print("First " + " " * 6 + "Middle " + " " * 6 + "Last " + "" * 6 )
print("-------------------------------")
for x in file1:
    s = Trim(x)
    print("%-10s %-10s %-10s" %(FirstName(s), MiddleName(s), LastName(s)))