from easynmt import EasyNMT

class Translator:
    def __init__(self):
        self.model = EasyNMT('mbart50_m2m')

    def translate(self, sentence: str, tgt_lang: str):
        src_lang = self.model.language_detection(sentence)
        if src_lang == tgt_lang:
            return sentence, src_lang
        return self.model.translate(sentence, tgt_lang), src_lang
