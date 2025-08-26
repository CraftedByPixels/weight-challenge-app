@echo off
echo 🚀 Запуск локального сервера для Weight Challenge App...
echo.

REM Проверяем наличие Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python не найден! Установите Python с https://python.org
    pause
    exit /b 1
)

REM Проверяем наличие index.html
if not exist "index.html" (
    echo ❌ Ошибка: файл index.html не найден!
    echo Убедитесь, что вы находитесь в папке с проектом
    pause
    exit /b 1
)

echo ✅ Python найден
echo ✅ Файлы проекта найдены
echo.
echo 🌐 Запускаю сервер на порту 8080...
echo 📱 Приложение будет доступно по адресу: http://localhost:8080
echo 🌍 Для доступа с других устройств: http://[ВАШ_IP]:8080
echo.
echo 💡 Нажмите Ctrl+C для остановки сервера
echo.

python start_server.py

pause
