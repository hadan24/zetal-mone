# Applying the distortion effects
from wav_io import args, data, rate
from numpy import column_stack, transpose, clip, multiply
from scipy import firwin, lfilter

# Amplitude at which to clip waveforms
clip_ampl = .5 * (.6309573445 ** args.distortion)

# a 2D array indicates a stereo file, so it must be transposed, and the channels processed independently
# https://numpy.org/doc/stable/reference/generated/numpy.transpose.html
if (data.ndim == 2):
	transposed = transpose(data)
	left_channel = transposed[0]
	right_channel = transposed[1]

	# Clipping for basic fuzz-like distortion
	left_channel = clip(left_channel, -clip_ampl, clip_ampl)
	right_channel = clip(right_channel, -clip_ampl, clip_ampl)
    
	# putting the channels back together once they've been filtered
	stereo_data = column_stack((left_channel, right_channel))
	distorted = stereo_data

# otherwise, the file is mono and can be processed normally.
else:
	distorted = clip(data, -clip_ampl, clip_ampl)

# Since clipping cuts the audio's amplitude and thus the volume
# as a side effect, we want to bring it back up roughly to the
# pre-distortion volume. Done by multiplying by this factor,
# found by trial and error.
normalize_factor = (1.88 ** (args.distortion - 8.3)) + 1
distorted *= normalize_factor