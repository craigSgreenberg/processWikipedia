
def relpath_to_title(relpath, prefix='/wikipedia/en_title/', code_length=5):
    # field has quotes surrounding it because reasons
    relpath = relpath.strip('"')
    print relpath
    assert relpath.startswith(prefix)
    relpath = relpath[len(prefix):]
    relpath = relpath.replace("_", " ")
    # encodes unicode as $XXXX with XXXX being the hex unicode codepoint
    bad_index = relpath.find('$')
    while bad_index != -1:
        # +1 to skip the starting $
        hex_unicode_point = relpath[bad_index+1:bad_index+code_length]
        replace_char = unichr(int(hex_unicode_point, 16)).encode('utf-8')
        relpath = relpath[:bad_index] + replace_char + relpath[bad_index+code_length:]
        bad_index = relpath.find('$')
    return relpath

def write_freebaseid_to_wikititle(infilepath, outfilepath, sep='\t'):
    with open(outfilepath, 'w') as outf:
        with open(infilepath) as inf:
            for line in inf:
                line = line.strip()
                if not line:
                    continue
                freebaseid, _, relpath = line.split(sep)
                title = relpath_to_title(relpath)
                print title
                outf.write(freebaseid+sep+title+'\n')

def main():
    infilepath = '/iesl/canvas/proj/processedClueweb12/freebase/msr/freebaseid_2_wikipedia-train_only.tsv'
    outfilepath = '/iesl/canvas/proj/processedClueweb12/freebase/msr/freebaseid_2_wikititle-train_only.tsv'
    write_freebaseid_to_wikititle(infilepath, outfilepath)

if __name__ == '__main__':
    main()
