from math import sqrt


class Statistics:
    @staticmethod
    def result(arr):
        elements = []
        nums = []
        for i in range(16):
            elements.append(i)
        for j in range(len(elements)):
            count = 0
            for m in range(len(arr)):
                if arr[m] == elements[j]:
                    count += 1
            nums.append(count)

        results = [[],[]]
        for l in range(len(elements)):
            results[0].append(elements[l])
            results[1].append(nums[l])
        return results

    @staticmethod
    def mean(arr):
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
        mean = sum / len(arr)
        return mean

    @staticmethod
    def sd(arr):
        sum = 0

        for i in range(len(arr)):
            sum += arr[i]
        mean = sum / len(arr)

        sq_sum = 0
        for j in range(len(arr)):
            sq_sum += (arr[j] - mean) ** 2

        deviation = 0
        if len(arr) != 1:
            deviation = sqrt(sq_sum / (len(arr) - 1))
        return deviation