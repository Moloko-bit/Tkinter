import tkinter as tk
from tkinter import ttk
from converter import CONVERSIONS, convert_units, swap_units

# Список для хранения истории последних конвертаций (максимум 5 записей)
history_list = []

def update_history_display():
    """Обновляет отображение истории в интерфейсе."""
    history_box.config(state="normal")
    history_box.delete("1.0", tk.END)
    for item in history_list:
        history_box.insert(tk.END, item + "\n")
    history_box.config(state="disabled")

def perform_conversion():
    """Считывает ввод пользователя, обрабатывает ошибки, считает и записывает в историю."""
    try:
        raw_value = value_entry.get().replace(",", ".")
        value = float(raw_value)
    except ValueError:
        result_label.config(text="Ошибка: введите число (например, 12.5)")
        return
    
    conversion_name = conversion_box.get()
    
    try:
        converted = convert_units(conversion_name, value)
        result_text = f"{value} {conversion_name} = {converted:.2f}"
        result_label.config(text=f"Результат: {converted:.2f}")
        
        # Добавляем в историю (сохраняем последние 5)
        history_list.insert(0, result_text)
        if len(history_list) > 5:
            history_list.pop()
        update_history_display()
        
    except Exception as e:
        result_label.config(text=f"Ошибка расчета: {e}")

def handle_swap():
    """Меняет местами исходную и целевую единицы в выпадающем списке."""
    current = conversion_box.get()
    new_selection = swap_units(current)
    if new_selection != current:
        conversion_box.set(new_selection)

# Создание главного окна
root = tk.Tk()
root.title("Продвинутый конвертер единиц")
root.geometry("400x480")
root.resizable(False, False)

# Заголовок
heading = ttk.Label(root, text="Конвертер с историей", font=("Arial", 14, "bold"))
heading.pack(pady=10)

# Поле для ввода значения
value_entry = ttk.Entry(root, font=("Arial", 11), width=28)
value_entry.pack(pady=5)
value_entry.insert(0, "1")

# Выпадающий список (Combobox) с вариантами
conversion_box = ttk.Combobox(
    root,
    values=list(CONVERSIONS.keys()),
    state="readonly",
    font=("Arial", 11),
    width=26
)
conversion_box.current(0)
conversion_box.pack(pady=5)

# Кнопка «Поменять единицы местами»[cite: 20]
swap_button = ttk.Button(root, text="⇄ Поменять местами", command=handle_swap)
swap_button.pack(pady=5)

# Кнопка запуска конвертации
convert_button = ttk.Button(root, text="Конвертировать", command=perform_conversion)
convert_button.pack(pady=5)

# Метка для вывода текущего результата
result_label = ttk.Label(root, text="Результат появится здесь", font=("Arial", 11, "bold"))
result_label.pack(pady=8)

# Панель истории (последние конвертации)[cite: 20, 21]
history_label = ttk.Label(root, text="История последних операций:", font=("Arial", 10, "italic"))
history_label.pack(anchor="w", padx=45)

history_box = tk.Text(root, height=6, width=42, font=("Arial", 9), state="disabled", bg="#f4f4f4")
history_box.pack(pady=5)

# Запуск главного цикла
if __name__ == "__main__":
    root.mainloop()