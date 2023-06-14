from wav_io import write_wav, play, args, rate
from band_eq import filtered

# Either writing the new wav file, or playing it - whichever was selected.
if(args.out):
    write_wav(args.out, rate, filtered)
else:
    play(rate, filtered)