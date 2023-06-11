from wav_io import args, write_wav, rate, play
from band_eq import filtered

# either writing the new wav file, or playing it - whichever was selected.
if(args.out):
    write_wav(args.out, rate, filtered)
else:
    play(rate, filtered)