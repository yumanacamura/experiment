import collections
import numpy as np

def get_tf(filename):
	return [{item[0]:item[1] for item in collections.Counter([w.split('\t')[0] for w in sen.split('\n')[:-1]]).most_common()} for sen in open(filename,'r').read().split('EOS\n')[:-1]]

def get_bin(tf):
    return {name:1 for name,count in tf.items()}

def cnt_word(docs, word):
    return len([1 for doc in docs if word in doc])

def get_nb(bins):
    word = set()
    docs = []

    #make word set [set,set]
    #and doc set [[[w,w,w...],[w,w,w...],...],[[w,w,w...],[w,w,w...]]
    for _bins in bins:
        doc = []
        for bin in _bins:
            d = [w for w in bin.keys()]
            doc.append(d)
            word = word | set(d)
        docs.append(doc)
    nbs = {}
    for w in word:
        cln = cnt_word(docs[0],w)
        mp3 = cnt_word(docs[1],w)
        sum = cln+mp3
        nbs[w] = [np.log(1000*n/sum + 1) for n in [cln,mp3]]
    return nbs


suf = ['cleaner','mp3player','test']
tfs = [get_tf('../mecab/' + name + '.mecab') for name in suf]
bins = [[get_bin(tf) for tf in tfs2] for tfs2 in tfs]
nbs = get_nb(bins)

tests = tfs[2]