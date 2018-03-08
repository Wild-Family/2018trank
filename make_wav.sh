if [ $# -ne 2 ]; then
  echo "./make_wav.sh txt filename.wav"
  exit 1
fi

say $1 -o tmp.aiff
ffmpeg -i tmp.aiff $2
rm tmp.aiff