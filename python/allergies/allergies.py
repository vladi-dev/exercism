class Allergies(object):
    tbl = {
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
        '''
        Explanation:
        Numbers in tbl in binary representation are numbers with one bit equals 1 and other bits are 0
        The next number is a shift by one bit to the left of the previous number
        Binary AND (&) operator copies a bit to the result if it exists in both operands

        Examples:
        1.
        0100 - 4 (Shellfish)
        0101 - 5 (Score)
        4 & 5 = 4 (0100) one bit exists in both numbers, at position 3

        2.
        1000 - 8 (Strawberries)
        0101 - 5 (Score)
        8 & 5 = 0 - no bits exist in both numbers
                 ^
        3.
        0000 0000 0001 - 1 (Eggs)
        0001 0000 0001 - 257 (Score)
        257 & 1 = 1 - one bit exists in both numbers at position 1
        '''
        self.lst = list(a for a in self.tbl if self.tbl[a] & score == self.tbl[a])

    def is_allergic_to(self, substance):
        return substance in self.lst
