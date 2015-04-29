
import codecs

def get_idfmap(idf_filepath, sep='\t'):
    d = {}
    with open(idf_filepath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            token, idf = line.split(sep)
            token = token.strip()
            d[token] = float(idf)
    return d

def write_tf_idf(tf_filepath, idfmap, outfilepath, sep='\t', encoding='utf8'):
    print 'encoding in', encoding
    with codecs.open(outfilepath, 'w', encoding=encoding) as outfile:
        with open(tf_filepath) as infile:
            for line in infile:
                line = line.strip()
                if not line:
                    continue
                freebaseid, token, tf = line.split(sep)
                token = token.strip()
                tf = int(tf)
                idf = idfmap[token]
                tfidf = tf * idf
                outline = freebaseid + sep + token + sep + str(tfidf) + '\n'
                outline = outline.decode('iso-8859-1').encode('utf-8')
                outfile.write(outline)

def main():
    tf_filepath = '/iesl/canvas/proj/processedClueweb12/enwiki-20150304-pages-articles_freebase-train-only_token-counts.txt'
    idf_filepath = '/iesl/canvas/proj/processedClueweb12/enwiki-20150304-pages-articles_freebase-train-only_token-idfs.txt'
    out_filepath = '/iesl/canvas/proj/processedClueweb12/enwiki-20150304-pages-articles_freebase-train-only_token-tf-idfs.txt'
    idfmap = get_idfmap(idf_filepath)
    write_tf_idf(tf_filepath, idfmap, out_filepath)

if __name__ == '__main__':
    main()
