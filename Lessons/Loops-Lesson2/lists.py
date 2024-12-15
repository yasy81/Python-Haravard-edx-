results = ["Mario", "Luigi"]

results.append("Princess")
results.append("Yoshi")

#or:

results.append(["buddy","sis","laser"])
results.remove(["buddy","sis","laser"])
results.extend(["buddy","sis","laser"])
print(results)


teenwolf = ["Scott","Stiles","Malia","Allison","Derek","Petter","Melissa","Cristoff","Jackson","Lydia","Issac","Kate","Victoria"]

teenwolf.remove("Allison")
teenwolf.append("Allison")
teenwolf.insert(1,"Allison")
teenwolf.reverse()
print(teenwolf)