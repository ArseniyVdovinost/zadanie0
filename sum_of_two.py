from typing import List, Optional

def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Возвращает индексы двух чисел из nums, сумма которых равна target.
    Если решение отсутствует, возвращает None.
    """
    seen = {}  # число -> индекс
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None


def main():
    """
    Опциональный ввод с клавиатуры.
    Пример ввода:
    2,7,11,15
    9
    """
    try:
        nums_input = input("Введите числа через запятую (например: 2,7,11,15): ")
        nums = list(map(int, nums_input.split(',')))
        target = int(input("Введите target: "))
        result = two_sum(nums, target)
        if result:
            print(f"Индексы: {result}")
        else:
            print("Решение не найдено.")
    except ValueError:
        print("Ошибка: некорректный ввод.")


if __name__ == "__main__":
    main()
