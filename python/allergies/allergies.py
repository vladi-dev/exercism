class Allergies(object):
    score = 0
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
        self.score = score

    def is_allergic_to(self, substance):
        return self.allergies[substance] <= self.score

    @property
    def lst(self):
        res = []
        allergies = sorted(self.allergies.items(), key=self.allergies.get)

        for allergy, score in allergies:
            if score <= self.score and self.score > 0:
                res.append(allergy)
                self.score -= score

        return res
