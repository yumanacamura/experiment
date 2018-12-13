import collections
print('\n'.join((['{0}\t{1}'.format(item[0],item[1]) for item in collections.Counter([[w.split('\t')[0] for w in sen.split('\n')[:-1]] for sen in open('kekka','r',encoding='euc-jp').read()[:-1].split('EOS\n')][0]).most_common()])))

