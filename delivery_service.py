def platform_counter(lst_of_weights: list[int], limit: int) -> int:
    """
    Функция считает количество платформ, которые могут быть использованы
    для перевозки роботов-исследователей с учетом весового ограничения
    платформы.
    """
    cnt = 0  # Счетчик платформ
    while len(lst_of_weights) > 0:
        if (len(lst_of_weights) > 1 and
                lst_of_weights[0] + lst_of_weights[-1] <= limit):
            cnt += 1
            lst_of_weights.pop(0)
            lst_of_weights.pop(-1)
        else:
            cnt += 1
            lst_of_weights.pop(-1)
    return cnt   # Возвращаем общее количество платформ


if __name__ == '__main__':
    lst_of_weights = list(map(int, input().split()))
    lst_of_weights.sort()
    limit = int(input())
    print(platform_counter(lst_of_weights, limit))
