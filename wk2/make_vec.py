import collections
import numpy as np
SENTENSE_NUM = 1000

def get_tf(filename):
	return [{item[0]:item[1] for item in collections.Counter([w.split('\t')[0] for w in sen.split('\n')[:-1]]).most_common()} for sen in open(filename,'r').read().split('EOS\n')[:-1]]

def get_bin(tf):
    return {name:1 for name,count in tf.items()}

def get_idf(bins):
    words = set()
    docs = []
    for bin in bins:
        doc = [w for w in bin.keys()]
        docs.append(doc)
        words = words | set(doc)
    return {word:np.log(SENTENSE_NUM / len([1 for doc in docs if word in doc])) + 1  for word in words}

def get_tf_idf(tf, idf):
    return {word:tf2*idf[word] for word,tf2 in tf.items()}

def output(filename, data):
    with open(filename,'w') as f:
        f.write('\n'.join([' '.join(['{0}:{1}'.format(w,v) for w,v in dt.items()]) for dt in data]))

suf = ['cleaner','mp3player','test']
tfs = [get_tf('../mecab/' + name + '.mecab') for name in suf]
bins = [[get_bin(tf) for tf in tfs2] for tfs2 in tfs]
all_bin = []
for bins2 in bins:
    all_bin.extend(bins2)
idf = get_idf(all_bin)
tf_idf = [[get_tf_idf(tf,idf) for tf in tfs2] for tfs2 in tfs]

for i in range(3):
    output('../output/' + suf[i] + '.vec=bi.txt', bins[i])
    output('../output/' + suf[i] + '.vec=tf.txt', tfs[i])
    output('../output/' + suf[i] + '.vec=tfidf.txt', tf_idf[i])
