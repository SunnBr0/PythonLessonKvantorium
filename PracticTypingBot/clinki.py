import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Параметры системы
g = 9.81        # Ускорение свободного падения (м/с^2)
L0 = 0.165        # Длина растянутой пружины (м)
m = 0.089         # Масса каждого звена (кг)
l = L0 / 2      # Длина одного звена (м)
k_t = 1.8       # Жесткость торсионной пружины (Нм/рад)
c_t = 0.05      # Коэффициент демпфирования (Нм·с/рад)

# Уравнения движения системы (из Лагранжа)
def equations(y, t):
    theta1, omega1, theta2, omega2 = y

    # Угловые ускорения (из Лагранжа)
    alpha1 = (-g / l) * np.sin(theta1) - (k_t / m) * (theta1 - theta2) - (c_t / m) * (omega1 - omega2)
    alpha2 = (-g / l) * np.sin(theta2) + (k_t / m) * (theta1 - theta2) + (c_t / m) * (omega1 - omega2)

    return [omega1, alpha1, omega2, alpha2]

# Начальные условия: углы и скорости
theta1_0 = np.pi / 6  # 30 градусов
theta2_0 = np.pi / 3  # 60 градусов
omega1_0 = 0
omega2_0 = 0

y0 = [theta1_0, omega1_0, theta2_0, omega2_0]

# Временной интервал
t = np.linspace(0, 5, 1000)  # 5 секунд, 1000 точек

# Решение системы уравнений
solution = odeint(equations, y0, t)
theta1, omega1, theta2, omega2 = solution.T

# Энергии системы
T_kin = 0.5 * m * (omega1**2 * l**2 + omega2**2 * l**2)
V_pot = m * g * l * (1 - np.cos(theta1)) + m * g * l * (1 - np.cos(theta2))
E_total = T_kin + V_pot

# Построение графиков
plt.figure(figsize=(10, 6))

# График углов
plt.subplot(2, 2, 1)
plt.plot(t, theta1, label=r'$\theta_1(t)$')
plt.plot(t, theta2, label=r'$\theta_2(t)$', linestyle='dashed')
plt.xlabel('Время (с)')
plt.ylabel('Угол (рад)')
plt.legend()
plt.title('Углы звеньев во времени')

# График угловых скоростей
plt.subplot(2, 2, 2)
plt.plot(t, omega1, label=r'$\dot{\theta}_1(t)$')
plt.plot(t, omega2, label=r'$\dot{\theta}_2(t)$', linestyle='dashed')
plt.xlabel('Время (с)')
plt.ylabel('Угловая скорость (рад/с)')
plt.legend()
plt.title('Угловые скорости во времени')

# График энергий
plt.subplot(2, 2, 3)
plt.plot(t, T_kin, label='Кинетическая энергия')
plt.plot(t, V_pot, label='Потенциальная энергия', linestyle='dashed')
plt.plot(t, E_total, label='Полная энергия', linestyle='dotted')
plt.xlabel('Время (с)')
plt.ylabel('Энергия (Дж)')
plt.legend()
plt.title('Энергия системы')

plt.tight_layout()
plt.show()
