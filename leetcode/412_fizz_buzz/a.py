from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output: List[str] = []
        for num in range(1, n + 1):
            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)
            if divisible_by_3 and divisible_by_5:
                output.append('FizzBuzz')
            elif divisible_by_3:
                output.append('Fizz')
            elif divisible_by_5:
                output.append('Buzz')
            else:
                output.append(str(num))
        return output
