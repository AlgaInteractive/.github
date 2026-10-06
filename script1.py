import datetime
import json
import os


class TodoManager:

    def __init__(self, filename="todo_list.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Загружает задачи из JSON-файла."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Ошибка чтения файла данных. Создан новый список.")
                return []
        return []

    def save_tasks(self):
        """Сохраняет задачи в JSON-файл."""
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(self.tasks, file, ensure_ascii=False, indent=4)
        except IOError:
            print("Ошибка при сохранении данных!")

    def add_task(self, title, category, priority, deadline):
        """Добавляет новую задачу."""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "category": category,
            "priority": priority,
            "deadline": deadline,
            "completed": False,
            "created_at": datetime.date.today().isoformat(),
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"\nЗадача '{title}' успешно добавлена!")

    def list_tasks(self, filter_completed=None):
        """Выводит список задач с возможностью фильтрации."""
        if not self.tasks:
            print("\nВаш список задач пуст.")
            return

        print(
            f"\n{'ID':<4} {'Название':<25} {'Категория':<15} {'Приоритет':<10} {'Дедлайн':<12} {'Статус':<10}"
        )
        print("-" * 80)

        for task in self.tasks:
            if (
                filter_completed is not None
                and task["completed"] != filter_completed
            ):
                continue

            status = "✅ Выполнено" if task["completed"] else "❌ В процессе"
            print(
                f"{task['id']:<4} {task['title']:<25} {task['category']:<15} {task['priority']:<10} {task['deadline']:<12} {status:<10}"
            )

    def complete_task(self, task_id):
        """Отмечает задачу как выполненную."""
        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print("\nЭта задача уже выполнена!")
                    return
                task["completed"] = True
                self.save_tasks()
                print(f"\nЗадача ID {task_id} отмечена как выполненная!")
                return
        print("\nЗадача с таким ID не найдена.")

    def delete_task(self, task_id):
        """Удаляет задачу по ID и пересчитывает ID оставшихся."""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                deleted = self.tasks.pop(i)
                # Переиндексация для красоты списка
                for index, t in enumerate(self.tasks):
                    t["id"] = index + 1
                self.save_tasks()
                print(f"\nЗадача '{deleted['title']}' удалена.")
                return
        print("\nЗадача с таким ID не найдена.")


def main():
    manager = TodoManager()

    while True:
        print("\n" + "=" * 30)
        print("   МЕНЕДЖЕР ЗАДАЧ (TODO)")
        print("=" * 30)
        print("1. Показать все задачи")
        print("2. Показать только активные")
        print("3. Добавить задачу")
        print("4. Выполнить задачу (по ID)")
        print("5. Удалить задачу (по ID)")
        print("6. Выйти из программы")

        choice = input("\nВыберите действие (1-6): ").strip()

        if choice == "1":
            manager.list_tasks()
        elif choice == "2":
            manager.list_tasks(filter_completed=False)
        elif choice == "3":
            title = input("Введите название задачи: ").strip()
            if not title:
                print("Название не может быть пустым!")
                continue
            category = input("Введите категорию (например, Работа, Дом): ").strip() or "Общее"
            priority = input("Приоритет (Низкий, Средний, Высокий): ").strip() or "Средний"
            deadline = input("Дедлайн (ГГГГ-ММ-ДД): ").strip() or "Нет"
            manager.add_task(title, category, priority, deadline)
        elif choice == "4":
            try:
                task_id = int(input("Введите ID выполненной задачи: "))
                manager.complete_task(task_id)
            except ValueError:
                print("Пожалуйста, введите корректное число.")
        elif choice == "5":
            try:
                task_id = int(input("Введите ID задачи для удаления: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Пожалуйста, введите корректное число.")
        elif choice == "6":
            print("\nДо свидания! Хорошего дня!")
            break
        else:
            print("\nНеверный ввод. Пожалуйста, выберите пункт от 1 до 6.")


if __name__ == "__main__":
    main()
def complete_task():
    selected = listbox.curselection()
    for index in selected:
        task_text = listbox.get(index)
        # Если ещё не отмечено как выполнено
        if not task_text.startswith("✔ "):
            listbox.delete(index)
            listbox.insert(index, f"✔ {task_text}")
            listbox.itemconfig(index, fg="gray")