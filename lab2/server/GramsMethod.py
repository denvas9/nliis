from GramCreator import GramCreator


class GramsMethod:
    def __init__(self, spanish_doc_path: str, german_doc_path: str) -> None:
        self.max = 1000
        self.spanish_grams = GramCreator(spanish_doc_path).sorted_grams
        self.german_grams = GramCreator(german_doc_path).sorted_grams

    def get_measure(self, grams_a: list, grams_b: list):
        measure = 0
        for i in range(len(grams_a)):
            if grams_a[i] in grams_b:
                measure += abs(grams_b.index(grams_a[i]))
            else:
                measure += self.max

        return measure

    def get_language(self, file_path: str):
        grams = GramCreator(file_path).sorted_grams
        print(grams)

        spanish_measure = self.get_measure(grams, self.spanish_grams)
        german_measure = self.get_measure(grams, self.german_grams)

        if spanish_measure < german_measure:
            return 'ИСПАНСКИЙ'
        else:
            return 'НЕМЕЦКИЙ'
