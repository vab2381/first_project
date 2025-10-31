print('Hello from repository!')

from dotenv import load_dotenv
import os


def print_author():
    # Загружаем переменные из файла .env
    load_dotenv()
    
    # Считываем значение переменной AUTHOR
    author = os.getenv("AUTHOR")
    
    # Выводим результат
    print(f"Автор проекта: {author}")


if __name__ == "__main__":
    print_author()
