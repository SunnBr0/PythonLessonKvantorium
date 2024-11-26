import numpy as np
import pywt
def haar_transform(image):
    # Выполняем вейвлет-преобразование Хаара для изображения
    coeffs = pywt.wavedec(image, 'haar', level=1)
    return coeffs
def inverse_haar_transform(coeffs):
    # Выполняем обратное вейвлет-преобразование Хаара для коэффициентов
    image = pywt.waverec(coeffs, 'haar')
    return image
def d2(alpha, beta_n):
    # Вычисляем квадрат Евклидова расстояния между alpha и beta_n
    return np.sum((np.array(alpha) - np.array(beta_n)) ** 2)
def main():
    # Заданное изображение alpha
    alpha = np.array([211, 215, 218, 220, 252, 216, 198, 142], dtype=np.float32)
    # Выполняем вейвлет-преобразование Хаара
    coeffs = haar_transform(alpha)
    # Преобразуем коэффициенты в один массив для удобства удаления
    all_coeffs = np.concatenate([c.flatten() for c in coeffs])
    # Сортируем коэффициенты по модулю
    sorted_indices = np.argsort(np.abs(all_coeffs))
    # Инициализация переменных для хранения минимального значения и соответствующего изображения
    max_n = 10
    best_beta_n = None
    maxCount = 0
    # Проходим по всем коэффициентам и удаляем наименьшие по модулю
    for n in range(1, max_n + 1):
        # Создаем копию коэффициентов
        modified_coeffs = all_coeffs.copy()
        # Удаляем n наименьших по модулю коэффициентов
        modified_coeffs[sorted_indices[:n]] = 0
        # Восстанавливаем структуру коэффициентов
        idx = 0
        for i in range(len(coeffs)):
            shape = coeffs[i].shape
            size = coeffs[i].size
            coeffs[i] = modified_coeffs[idx:idx + size].reshape(shape)
            idx += size
        # Выполняем обратное вейвлет-преобразование
        beta_n = inverse_haar_transform(coeffs)
        # Вычисляем квадрат Евклидова расстояния
        current_d2 = d2(alpha, beta_n)
        # Проверяем, удовлетворяет ли условие
        if current_d2 < 3.5:
            best_beta_n = beta_n
        else:
            maxCount = n
            break
    # Выводим результат
    if best_beta_n is not None:
        print("Максимальное значение n:", maxCount)
        print("Соответствующее декодированное изображение:", best_beta_n)
    else:
        print("Не найдено декодированное изображение с d2 < 3.5")

if __name__ == "__main__":
    main()