
from __future__ import division
from math import  log

def write_idfs(infilepath, outfilepath, num_docs_in_corpus=2213898, sep='\t'):
    with open(outfilepath, 'w') as outfile:
        with open(infilepath) as infile:
            for line in infile:
                line = line.strip()
                if not line:
                    continue
                num_docs_containing_token = line.split()[0]
                token = line[len(num_docs_containing_token)+1:]
                num_docs_containing_token = int(num_docs_containing_token)
                ## default log is e, we're choosing log base 2
                idf = log(num_docs_in_corpus/num_docs_containing_token, 2)
                outfile.write(token+sep+str(idf)+'\n')

def main():
    infilepath = '/iesl/canvas/proj/processedClueweb12/enwiki-20150304-pages-articles_freebase-train-only_token-dfs.txt'
    outfilepath = '/iesl/canvas/proj/processedClueweb12/enwiki-20150304-pages-articles_freebase-train-only_token-idfs.txt'
    write_idfs(infilepath, outfilepath)

if __name__ == '__main__':
    main()
