max = 15
step = 4



numbers = [i for i in range(2,max+1)]
tasks = []

for index, val in enumerate(numbers):
    tasks.append(val)
    #if len(tasks) == step or ((len(numbers)-index) <= step):
    if len(tasks) == step or (index==max-2):
        print(tasks)
        tasks=[]




