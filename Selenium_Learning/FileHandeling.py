with open("firstdoc.txt","w") as fw:
    fw.write("this is first line")

with open("firstdoc.txt","r") as fr:
    print(fr.read())