# class slicer():
#     def __init__(self, toslice, step):
#         self.i = 0
#         self.n = len(toslice) - step + 1
#         self.toslice = toslice
#         self.step = step
#         if self.step > len(toslice) or not (self.step):
#             raise ValueError()
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.i < self.n:
#             i = self.i
#             self.i += 1
#             return list(map(int, self.toslice[i:i + self.step]))
#         else:
#             raise StopIteration
#
#
# slices = lambda toslice, step: [x for x in slicer(toslice, step)]


def slices(raw, thickness):
    if thickness > len(raw) or not (thickness):
        raise ValueError('Can not slice this')

    return [map(int, raw[x:x + thickness]) for x in xrange(len(raw) - thickness + 1)]
