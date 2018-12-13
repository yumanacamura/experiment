import collections
def get_freq(filename):
	return collections.Counter([[w.split('\t')[0] for w in sen.split('\n')[:-1]] for sen in open(filename,'r').read()[:-1].split('EOS\n')][0]).most_common()

