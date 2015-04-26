
def get_freebaseids(filepath, sep='\t'):
    freebaseids = set([])
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            freebaseid = line.split(sep)[0]
            freebaseids.add(freebaseid)
    return  freebaseids

def write_filtered_freebaseid_to_wiki_file(freebaseids, freebaseid_to_wiki_filepath, outfilepath, sep='\t'):
    with open(outfilepath, 'w') as outf:
        with open(freebaseid_to_wiki_filepath) as in_f:
            for line in in_f:
                freebaseid = line.split(sep)[0]
                if freebaseid not in freebaseids:
                    continue
                outf.write(line)

def main():
    train_freebaseids_filepath = "/iesl/canvas/proj/processedClueweb12/freebase/msr/msrFreebaseTrain.v0.tsv"
    freebaseid_to_wiki_filepath = "/iesl/canvas/proj/processedClueweb12/freebase/msr/entity.tsv"
    outfilepath = "/iesl/canvas/proj/processedClueweb12/freebase/msr/freebaseid_2_wikipedia-train_only.tsv"
    freebaseids = get_freebaseids(train_freebaseids_filepath)
    write_filtered_freebaseid_to_wiki_file(freebaseids, freebaseid_to_wiki_filepath, outfilepath)

if __name__ == "__main__":
    main()