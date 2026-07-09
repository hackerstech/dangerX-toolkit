import os,time,random
l=[1,2,3,4,5,6,7,8,9,0]
fol=open('filex.txt','a')
os.system('touch filex.txt')

print('starting .... made by hackerZX anon @kxzen_xx')
while True:
    tar=random.choices(l,k=9)
    targ=''.join(str(x) for x in tar) 
    rnd=random.randint(6,9)
    target=str(rnd)+str(targ)
    print(target)
    time.sleep(1.3)
    fol.write(target)
    fol.close()
    os.system(f'xdg-open tg://resolve?phone=91{target}')


# you can integrate any files or database works in linux with telegram and integrate other num lists if u wan
