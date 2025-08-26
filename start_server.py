#!/usr/bin/env python3
"""
Простой HTTP сервер для локального развертывания Weight Challenge App
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# Настройки сервера
PORT = 8080
DIRECTORY = "."

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Добавляем CORS заголовки для работы с Firebase
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_server():
    """Запускает локальный HTTP сервер"""
    
    # Проверяем наличие index.html
    if not os.path.exists('index.html'):
        print("❌ Ошибка: файл index.html не найден!")
        print("Убедитесь, что вы находитесь в папке с проектом")
        return
    
    # Создаем сервер
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"🚀 Сервер запущен на http://localhost:{PORT}")
        print(f"📱 Ваше приложение доступно по адресу: http://localhost:{PORT}")
        print(f"🌐 Для доступа с других устройств используйте: http://[ВАШ_IP]:{PORT}")
        print("\n📋 Инструкции:")
        print("1. Откройте браузер и перейдите по адресу выше")
        print("2. Для доступа с других устройств в сети:")
        print("   - Узнайте ваш IP адрес: ipconfig")
        print("   - Используйте: http://[ВАШ_IP]:8080")
        print("3. Нажмите Ctrl+C для остановки сервера")
        
        # Автоматически открываем браузер
        try:
            webbrowser.open(f'http://localhost:{PORT}')
        except:
            pass
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Сервер остановлен")

if __name__ == "__main__":
    start_server()
