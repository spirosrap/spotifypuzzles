"""
a = [
    (197812,'re_hash'),
    (267903,'tomorrow_comes_today'),
    (78906,'5_4'),
    (39453,'new_genious'),
    (210492,'clint_eastwood'),
    (26302,'man_research'),
    (22544,'punk'),
    (19727,'sound_check'),
    (17535,'double_bass'),
    (18782,'rock_the_house'),
    (198189,'19_2000'),
    (13151,'latin_simone'),
    (12139,'starshine'),
    (11272,'slow_country'),
    (10521,'m1_a1'),
]
"""
n, m = raw_input().split()
a=[]
for i in range(0,int(n)):
    d1, d2 = raw_input().split()
    a.append((int(d1),str(d2)))
    
#print a



b=[]
for i in range(0,len(a)):
    c =  float(a[i][0])*float(i+1)
    b.append((c,a[i][1],(len(a)-i)))

a = sorted(b, key=lambda s: (s[0],s[2]))   
a.reverse()
#print a

for i in range(0,int(m)):
    print a[i][1]
