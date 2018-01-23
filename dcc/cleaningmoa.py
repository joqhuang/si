f = open("dlpsid.csv","r")
dlpsids = f.readlines()
f.close()
f = open("moa1.csv","r")
rawmoa1ids = f.readlines()
f.close()
moa1ids = []
for raw in rawmoa1ids:
    raw.strip().replace("\n,","")
    if len(raw)>2:
        moa1ids.append(raw[:7])

rawids = []
picids = []
for line in dlpsids:
    rawids.append(line.replace("\n","").lower().split(",")[0])
    try:
        picids.append(line.lower().replace("\n","").split(",")[1])
    except:
        picids.append("moa id")

formattedids = []
for rawid in rawids:
    if len(rawid) == 7:
        formattedids.append(rawid+".0001.001")
    elif len(rawid) == 16:
        formattedids.append(rawid)
    else:
        formattedids.append("*"+rawid)

textclasslist = []
for formattedid in formattedids:
    if formattedid[0] != "*":
        try:
            textclasslist.append("/n1/obj/{}/{}/{}/{}".format(formattedid[0],formattedid[1],formattedid[2],formattedid))
        except:
            textclasslist.append("there's and issue with this one")
    else:
        try:
            textclasslist.append("/n1/obj/{}/{}/{}/{}".format(formattedid[1],formattedid[2],formattedid[3],formattedid[1:]))
        except:
            textclasslist.append("there's and issue with this one")

pairtreelist = []
for picid in picids:
    try:
        pairtreelist.append("/n1/asset/m/misc/pairtree_root/mo/a{}/{}/{}".format(picid[3],picid[4:],picid))
    except:
        pairtreelist.append("?")

outputfilelineslist = []
for idx in range(len(formattedids)):
    outputfilelineslist.append("{},{},{},{}\n".format(formattedids[idx],textclasslist[idx],picids[idx],pairtreelist[idx]))

f = open("moa4.csv","w")
for line in outputfilelineslist:
    if line.split(",")[0][:7] not in moa1ids:
        f.write(line)
f.close()
