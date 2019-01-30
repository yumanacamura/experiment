from make_vec import nbs, tests

ans = []

for test in tests:
    cln = 0
    mp3 = 0
    for w,n in test.items():
        nb = nbs[w]
        cln += n*nb[0]
        mp3 += n*nb[1]
    if cln > mp3:
        ans.append('cleaner')
    else:
        ans.append('mp3player')

with open('./output.txt','w') as f:
    f.write('\n'.join(ans))

