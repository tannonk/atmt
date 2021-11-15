from seq2seq.data.dictionary import Dictionary

class BPE():
    def __init__(self, merges=2000):
        self.merges = merges
        self.vocabulary = {}

    def create_vocabulary(self, merges):
        pass

    def apply_bpe_to_file(self, file, vocabulary):
        '''return file with applied bpe segmanetation with eow tag and whitespace between bp
        return: preprocessed/train.en -> preprocessed/bpe1.en
                preprocessed/bpe1.en -> preprocessed/bpe2.en
        '''
        pass

    def bpe_segmentation(self, string, vocab):
        pass

    def dropout(self, probability=0.5):
        pass

