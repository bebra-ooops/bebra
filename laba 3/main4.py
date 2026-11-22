import sys
# Импортируем наши функции из первого файла (variant4_mod.py)
from variant4_mod import parse_frame, filter_known_slaves, format_telemetry_dict

def main():
    # Чтение настроек из sys.argv (аргументов командной строки)
    if len(sys.argv) > 1:
        try:
            device_id = int(sys.argv[1])
        except ValueError:
            print("Ошибка: ID устройства должен быть числом. Используем 5 по умолчанию.")
            device_id = 5
    else:
        device_id = 5

    # Множество разрешенных адресов (для проверки)
    allowed_slaves = {1, 3, 5, 12}

    # Формируем тестовые данные (кадр Modbus)
    raw_frame = [device_id, 3, 0, 100, 0, 2, 180, 22]
    
    print(" СВОДНЫЙ ОТЧЕТ СИСТЕМЫ ТЕЛЕМЕТРИИ ")
    print(f"Запущен скрипт: {sys.argv[0]}")
    print(f"Анализируемый кадр: {raw_frame}")

    # Вызываем функции из модуля
    try:
        # Извлекаем данные
        addr, func, data = parse_frame(raw_frame)
        
        # Проверяем, разрешен ли адрес
        is_allowed = filter_known_slaves(addr, allowed_slaves)
        
        # Формируем словарь телеметрии
        telemetry = format_telemetry_dict(addr, data)
        
        # Выводим результат
        print("\n РЕЗУЛЬТАТ ДЕКОДИРОВАНИЯ ")
        print(f"Адрес устройства: {addr}")
        print(f"Код функции: {func}")
        print(f"Данные: {data}")
        
        if is_allowed:
            print("Статус адреса: РАЗРЕШЕН (устройство в белом списке)")
        else:
            print("Статус адреса: ЗАПРЕЩЕН (неизвестное устройство!)")
            
        print("\n СЛОВАРЬ ТЕЛЕМЕТРИИ ")
        for key, value in telemetry.items():
            print(f"  {key}: {value}")
            
        # Демонстрация среза: берем первые 2 байта данных
        print(f"\nПервые 2 байта данных (срез): {data[:2]}")
        
    except ValueError as e:
        print(f"\n ОШИБКА: {e}")

if __name__ == '__main__':
    main()