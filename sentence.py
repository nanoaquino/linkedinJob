def sentences(str1, str2):
    #only replace commond chars
    strFmt1 = str1.replace('.',' ').replace(',',' ').replace('!',' ').replace('?',' ')
    strFmt2 = str2.replace('.',' ').replace(',',' ').replace('!',' ').replace('?',' ')
    strLow1 = strFmt1.lower()
    strLow2 = strFmt2.lower()
    listSplit1 = strLow1.split(' ')
    listSplit2 = strLow2.split(' ')
    list1 = [string for string in listSplit1 if string != ""]
    list2 = [string for string in listSplit2 if string != ""]
    inCommon = list(set(list1).intersection(list2))
    notCommon = list(set(list1) - set(list2))
    return inCommon, notCommon
