import imageio
imageio.plugins.ffmpeg.download()
import nltk
for l in ['vader_lexicon','averaged_perceptron_tagger']:
    nltk.download(l)
