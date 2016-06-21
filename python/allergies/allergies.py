class Allergies(object):
    lst = []
    allergies = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }

    def __init__(self, score):
        self._score = score
        self.lst = []
        allergies = sorted(self.allergies.items(), key=self.allergies.get, reverse=True)

        for allergy, cur_score in allergies:
            if cur_score <= score and score > 0:
                self.lst.append(allergy)
                score -= cur_score

    def is_allergic_to(self, substance):
        return substance in self.lst
