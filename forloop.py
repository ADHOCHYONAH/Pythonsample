# loops mostly used in data structures

cars=["nissan","toyota","benz","isuzu"]

for i in cars:
    print(i)
    if i == "toyata":
        break

for x in range(2,6):
    print(x)

    #nested loop  (loop within a loop)

color=["red","big","tasty"]
fruits=["apples","oranges","cherry"]

for rangi in color:
    for matunda in fruits:
     print(rangi,matunda)