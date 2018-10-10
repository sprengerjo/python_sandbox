class QuickSort(object):
    @staticmethod
    def sort(list):
        if not list or len(list) <= 1:
            return list

        else:
            head = list[0]
            h = []
            l = []

            for i in list[1:]:
                if i >= head:
                    h.append(i)
                else:
                    if i < head:
                        l.append(i)

            return QuickSort.sort(l) + [head] + QuickSort.sort(h)
