from Document import Document


class AlphabetMethod:
    def __init__(self, spanish_doc_path: str, german_doc_path: str) -> None:
        self.spanish_alphabet = self.get_alphabet(self.get_text(spanish_doc_path))
        self.german_alphabet = self.get_alphabet(self.get_text(german_doc_path))

    def get_language(self, file_path: str):
        alphabet = self.get_alphabet(self.get_text(file_path))

        if len(alphabet.intersection(self.spanish_alphabet - self.german_alphabet)) == 0:
            return 'НЕМЕЦКИЙ'
        else:
            return 'ИСПАНСКИЙ'

    @staticmethod
    def get_alphabet(text: str):
        alphabet = set()

        for sign in text:
            alphabet.add(sign)

        return alphabet

    @staticmethod
    def get_text(document_path: str) -> str:
        return Document(document_path).get_text(document_path)
