def get_temperature(t_from, t_to, value):
    temperature = {
        'C': {'step': 1, 'default': 0},
        'F': {'step': 1.8, 'default': 32},  # default - единица по цельсию
        'K': {'step': 1, 'default': 273.15, },
        'R': {'step': 1.8, 'default': 491.67, },
        'Re': {'step': 0.8, 'default': 0}
    }
    # получаю значение 0 относительно единицы измерения с которой и в которую перевожу
    default = temperature[t_to]['default'] - temperature[t_from]['default'] / (
                temperature[t_from]['step'] / temperature[t_to]['step'])

    result = default + temperature[t_to]['step'] / temperature[t_from]['step'] * value
    print(result)


get_temperature('C', 'K', 0)
