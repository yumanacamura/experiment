import collections

k = 5

def get_vec(filename):
    with open(filename,'r') as f:
        sens = f.read().split('\n')
    return [{word:float(tfidf) for word,tfidf in map(lambda x:x.split(':'),sen.split(' '))} for sen in sens]

def cos_sim(v1,v2):
    key = set(v1.keys()) | set(v2.keys())
    vec = [[v[k] if k in v else 0 for k in key] for v in [v1,v2]]
    norm = (lambda x:(x[0]*x[1])([sum(map(lambda x:x**2,v)) for v in vec])**0.5
    return sum(map(lambda x:x[0]*x[1],zip(vec*)))/norm

def annotate(data,label):
    return list(map(lambda x:(x,label),data))

suf = ['cleaner','mp3player','test']
clnr_vec,mp3_vec,test_vec = [get_vec('../vec/{0}.vec=tfidf.txt'.format(name)) for name in suf]

teacher_vec = annotate(clnr_vec,'cleaner') + annotate(mp3_vec,'mp3')

ans = []

for vec in test_vec:
    teacher_vec.sort(lambda x:cos_sim(x[0],vec))
    if len(filter(lambda x:x[1]=='cleaner',teacher_vec[:k])) > k/2:
        ans.append('cleaner')
    else:
        ans.append('mp3')

with open('../k_mean/output.txt','w') as f:
    f.write('\n'.join(ans))
