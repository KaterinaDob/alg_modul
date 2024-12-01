#  128587656 - ID


def platform_counter(lst_of_weights: list[int], limit: int) -> int:
    """
    Функция считает количество платформ, которые могут быть использованы
    для перевозки роботов-исследователей с учетом весового ограничения
    платформы.
    """
    lst_of_weights_sorted: list[int] = sorted(lst_of_weights)
    cnt: int = 0  # Счетчик платформ
    left_pointer: int = 0
    right_pointer: int = len(lst_of_weights_sorted) - 1

    while left_pointer <= right_pointer:
        if (len(lst_of_weights_sorted) > 1 and
                lst_of_weights_sorted[left_pointer] +
                lst_of_weights_sorted[right_pointer] <= limit):
            cnt += 1
            left_pointer += 1
            right_pointer -= 1
        else:
            cnt += 1
            right_pointer -= 1

    return cnt  # Возвращаем общее количество платформ


if __name__ == '__main__':
    lst_of_weights: list[int] = [int(i) for i in input().split()]
    limit: int = int(input())
    print(platform_counter(lst_of_weights, limit))
