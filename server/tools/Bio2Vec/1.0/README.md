# Word Vectors for the Biomedical Domain

This is a small repo with scripts that install word2vec, convert PubMed XML files to raw text and runs word2vec. This is http://bio.nlplab.org resources for biomedical text mining

## Usage

The basic usage of this requires a downloaded copy of the Pubmed XML files (yearbly baseline available from ftp://ftp.ncbi.nlm.nih.gov/pubmed/baseline/). It will process these files and compile a copy of word2vec and run the tool. The single command looks like below.

``` sh
./run.sh -i PUBMED_BASELINE_DIRECTORY -o output_dir
```

## Relevant citations
- Word2Vec (http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf)
- Distributional Semantics Resources for Biomedical Text Processing (http://bio.nlplab.org/pdf/pyysalo13literature.pdf)
