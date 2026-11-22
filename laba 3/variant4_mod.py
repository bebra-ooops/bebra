""""
Модуль маршрутизации и декодирования кадров Modbus/PLC.
"""

def parse_frame(frame_list):
    """
    Извлекает адрес, код функции и данные из кадра.
    """
    if len(frame_list) < 4:
        raise ValueError("Кадр слишком короткий.")

    slave_id = frame_list[0]
    function_code = frame_list[1:2]
    data_bytes = frame_list[2:-2]

    return slave_id, function_code, data_bytes


def filter_known_slaves(slave_id, allowed_set):
    """
    Проверяет, есть ли адрес в разрешённом множестве.
    """
    return slave_id in allowed_set

def format_telemetry_dict(device_id, reg_dict):
    """
    Формирует словарь телеметрии.
    """
    return {
        "device_id": device_id,
        "registers": reg_dict,
        "status": "OK" if reg_dict else "NO_DATA"
    }

if __name__ == '__main__':
    print(" АВТОНОМНЫЙ ТЕСТ МОДУЛЯ ")
    test_frame = [5, 3, 0, 100, 0, 2, 180, 22]
    allowed = {1, 3, 5, 12}

    addr, func, data = parse_frame(test_frame)
    print(f"Адрес={addr}, Функция={func}, Данные={data}")
    print(f"Разрешён: {filter_known_slaves(addr, allowed)}")