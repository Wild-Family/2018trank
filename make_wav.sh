if [ $# -ne 3 ]; then
  echo "./make_wav.sh txt filename(aiff) filename(wav)"
  exit 1
fi

say $1 -o $2
ffmpeg -i $2 $3
rm $2