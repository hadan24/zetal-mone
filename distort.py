# Applying the distortion effects
from wav_io import data
from numpy import column_stack, transpose

# Amplitude at which to clip waveforms
hard_clip_cutoff = .05

# Based exactly on the 1st homework assignment
def hard_clip(data, cutoff):
	for i in range(data.size):
		if (data[i] > cutoff):
			data[i] = cutoff
		elif (data[i] < -cutoff):
			data[i] = -cutoff


# a 2D array indicates a stereo file, so it must be transposed, and the channels processed independently
# https://numpy.org/doc/stable/reference/generated/numpy.transpose.html
if (data.ndim == 2):
	transposed = transpose(data)
	left_channel = transposed[0]
	right_channel = transposed[1]
	hard_clip(left_channel, hard_clip_cutoff)
	hard_clip(right_channel, hard_clip_cutoff)
    
	# putting the channels back together once they've been filtered
	stereo_data = column_stack((left_channel, right_channel))
	distorted = stereo_data

# otherwise, the file is mono and can be processed normally.
else:
	distorted = data
	hard_clip(distorted, hard_clip_cutoff)
