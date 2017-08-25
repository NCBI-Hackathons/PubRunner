#!/bin/bash
set -eo pipefail

usage() {
	echo "$0 -i <MEDLINE_DIR> -o <OUT_DIR>"
	echo "  MEDLINE_DIR: Directory with MEDLINE XML files"
	echo "  OUT_DIR: Directory in which save word2vec vector"
	echo
}

while [[ $# > 0 ]]
do
	key="$1"

	case $key in
		-h|--help)
		usage
		exit 0
		;;
		-i)
		MEDLINE_DIR="$2"
		shift # past argument
		;;
		-o)
		OUT_DIR="$2"
		shift # past argument
		;;
		*)
		echo "Unknown parameters: $key"
		exit 255
		;;
	esac
	
	if [[ $# > 0 ]]; then
		shift # past argument or value
	fi
done

if [ -z "$MEDLINE_DIR" ]; then
	echo "ERROR: -i <MEDLINE_DIR> must be set" >&2; usage; exit 255
elif [ -z "$OUT_DIR" ]; then
	echo "ERROR: -o <OUT_DIR> must be set" >&2; usage; exit 255
elif [ ! -d $MEDLINE_DIR ]; then
	echo "ERROR: <MEDLINE_DIR> must be a directory" >&2; usage; exit 255
fi

TMP_TXT_DIR=tmp.medline.parts

HERE="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SRC_DIR=word2vec/src
BIN_DIR=word2vec/bin
TEXT_DATA=tmp.medline.txt
WORD2VEC_REPO=https://github.com/jakelever/word2vec.git
OUT_VECTOR=$OUT_DIR/vectors

echo
echo "#####################"
echo "Cloning word2vec repo ($WORD2VEC_REPO)"
echo "#####################"
rm -fr word2vec
git clone $WORD2VEC_REPO

echo
echo "#####################"
echo "Building word2vec"
echo "#####################"
cd $SRC_DIR
make
cd -

echo
echo "#####################"
echo "Converting Pubmed XML files to raw text"
echo "#####################"
rm -fr $TMP_TXT_DIR
mkdir $TMP_TXT_DIR
time python $HERE/PubMed2Txt.py -i $MEDLINE_DIR -o $TMP_TXT_DIR

echo
echo "#####################"
echo "Combining all Pubmed text files into one"
echo "#####################"
cat $TMP_TXT_DIR/*.txt > $TEXT_DATA
rm -fr $TMP_TXT_DIR

echo
echo "#####################"
echo "Running word2vec"
echo "#####################"
mkdir -p $OUT_DIR
time $BIN_DIR/word2vec -train $TEXT_DATA -output $OUT_VECTOR -cbow 0 -size 200 -window 5 -negative 0 -hs 1 -sample 1e-3 -threads 12 -binary 1

echo
echo "#####################"
echo "Cleanup"
echo "#####################"
rm -fr $TEXT_DATA
rm -fr word2vec

echo
echo "#####################"
echo "Complete. Vectors stored at $OUT_VECTOR"
echo "#####################"
