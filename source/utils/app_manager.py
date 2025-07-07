import subprocess

from ..settings import PROGRAMS

class AppManager:
    def __init__(self):
        self.program_paths = PROGRAMS
        self.processes = {}  

    def run_program(self, program_name: str):
        """Запускает программу и сохраняет процесс."""
        if program_name not in self.program_paths:
            print(f"Программа '{program_name}' не найдена.")
            return

        path = self.program_paths[program_name]
        try:
            process = subprocess.Popen(path)
            if program_name not in self.processes:
                self.processes[program_name] = []
            self.processes[program_name].append(process)
            print(f"Запущена '{program_name}' с PID {process.pid}")
        except Exception as e:
            print(f"Не удалось запустить '{program_name}': {e}")

    def close_program(self, program_name: str):
        print("Закрытие программы:", program_name)
        """Закрывает все запущенные экземпляры указанной программы."""
        if program_name not in self.processes or not self.processes[program_name]:
            print(f"Нет запущенных процессов '{program_name}' для закрытия.")
            return

        for i, process in enumerate(self.processes[program_name]):
            try:
                process.terminate()
                process.wait(timeout=5)
                print(f"Закрыт '{program_name}' экземпляр {i+1}")
            except Exception as e:
                print(f"Не удалось закрыть '{program_name}' экземпляр {i+1}: {e}")

        # Очищаем список процессов после закрытия
        self.processes[program_name] = []
