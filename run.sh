#!/bin/sh
cd /iesl/canvas/csgreenberg/c0d3/universalSchema_fork/univSchema
if [ ! -e CP.hack ]; then
    echo "Run make_cp.sh script first"
    exit    
fi

classpath=`cat CP.hack`
app="java -Xmx30g -cp ${classpath} cc.factorie.app.nlp.load.LoadWikipediaPlainText"
$app 1000 /iesl/canvas/proj/processedClueweb12/wikipedia/enwiki/enwiki-20150304-pages-articles.xml.bz2
#--train=/iesl/canvas/proj/processedClueweb12/freebase/msr/msrFreebaseTrain.v0.tsv --dev=/iesl/canvas/proj/processedClueweb12/freebase/msr/msrFreebaseDev70.v0.tsv --test=/iesl/canvas/proj/processedClueweb12/freebase/msr/msrFreebaseTest70.v0.tsv --testRelationsFile=/iesl/canvas/proj/processedClueweb12/freebase/msr/release_v0.4/70Types --size $1 --rate $2 --regularizer $3 --negative $4 --threads $5 --options 3  --epochs 30 --frequency 10 --tree $6
