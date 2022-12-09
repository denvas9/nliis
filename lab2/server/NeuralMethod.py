import spacy
from spacy.language import Language
from spacy_language_detection import LanguageDetector


def get_lang_detector(nlp, name):
    return LanguageDetector(seed=42)

class NeuralMethod:
    __slots__ = ('_path_to_file', '_content')

    LANGUAGES = {
        'es': 'ИСПАНСКИЙ',
        'de': 'НЕМЕЦКИЙ'
    }

    def __init__(self, path_to_file: str) -> None:
        self._path_to_file = path_to_file
        self.read_file()


    def read_file(self) -> None:
        with open(self._path_to_file, 'r', encoding='utf-8') as file:
            self._content = file.read()

    def detect_language(self):
        nlp_model = spacy.load("en_core_web_sm")
        Language.factory("language_detector", func=get_lang_detector)
        nlp_model.add_pipe('language_detector', last=True)
        doc = nlp_model(self._content)
        return doc._.language['language']
    
    @property
    def get_result(self) -> str:
        return self.LANGUAGES.get(self.detect_language())


