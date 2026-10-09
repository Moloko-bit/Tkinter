import tkinter as tk
from tkinter import ttk
from converter import CONVERSIONS, convert_units

def perform_conversion():
    """Считывает ввод пользователя, обрабатывает ошибки и выводит результат."""
    try:
        # Заменяем запятую на точку на случай ввода с русской локалью
        raw_value = value_entry.get().replace(",", ".")
        value = float(raw_value)
    except ValueError:
        result_label.config(text="Ошибка: введите число (например, 12.5)")
        return
    
    conversion_name = conversion_box.get()
    
    try:
        converted = convert_units(conversion_name, value)
        result_label.config(text=f"Результат: {converted:.2f}")
    except Exception as e:
        result_label.config(text=f"Ошибка расчета: {e}")

# Создание главного окна
root = tk.Tk()
root.title("Конвертер единиц")
root.geometry("380x260")
root.resizable(False, False)

# Заголовок
heading = ttk.Label(root, text="Мой конвертер", font=("Arial", 14, "bold"))
heading.pack(pady=12)

# Поле для ввода значения
value_entry = ttk.Entry(root, font=("Arial", 11), width=25)
value_entry.pack(pady=6)
value_entry.insert(0, "10")  

# Выпадающий список (Combobox) с вариантами конвертации
conversion_box = ttk.Combobox(
    root,
    values=list(CONVERSIONS.keys()),
    state="readonly",
    font=("Arial", 11),
    width=23
)
conversion_box.current(0)
conversion_box.pack(pady=6)

# Кнопка запуска конвертации
convert_button = ttk.Button(root, text="Конвертировать", command=perform_conversion)
convert_button.pack(pady=8)

# Метка для вывода результата
result_label = ttk.Label(root, text="Результат появится здесь", font=("Arial", 11))
result_label.pack(pady=6)

# Запуск главного цикла обработки событий
if __name__ == "__main__":
    root.mainloop()