# Weight Challenge App

Веб-приложение для челленджа по снижению веса с локальным хранением данных.

## 🚀 Развертывание

### Вариант 1: GitHub Pages (Рекомендуется)

1. **Создайте репозиторий на GitHub** с названием `weight-challenge-app`
2. **Загрузите код** в репозиторий:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/[ВАШ_USERNAME]/weight-challenge-app.git
   git push -u origin main
   ```
3. **Включите GitHub Pages** в настройках репозитория:
   - Settings → Pages
   - Source: Deploy from a branch
   - Branch: gh-pages
4. **Приложение будет доступно** по адресу: `https://[ВАШ_USERNAME].github.io/weight-challenge-app`

### Вариант 2: Локальный сервер

1. **Установите Python** (если не установлен)
2. **Запустите сервер**:
   ```bash
   # Windows
   start_server.bat
   
   # Или вручную
   python start_server.py
   ```
3. **Приложение будет доступно** по адресу: `http://localhost:8080`

## 📁 Структура проекта

- `index.html` - основное приложение (без Firebase)
- `start_server.py` - локальный HTTP сервер
- `start_server.bat` - скрипт запуска для Windows
- `.github/workflows/deploy.yml` - GitHub Actions для автоматического развертывания

## 🔧 Конфигурация

Проект настроен для:
- **GitHub Pages** - автоматическое развертывание
- **Локального сервера** - для разработки и тестирования
- **Локального хранения данных** - использует localStorage браузера

## 📱 Функции приложения

- ✅ Регистрация и авторизация пользователей
- ✅ Создание и участие в челленджах по снижению веса
- ✅ Отслеживание прогресса с графиками
- ✅ Локальное хранение данных (localStorage)
- ✅ Система взносов для участия
- ✅ Административная панель

## 🔑 Доступ к админ панели

**Учетные данные администратора:**
- **Имя пользователя:** `admin`
- **Email:** `randeako@gmail.com`
- **Пароль:** `admin123`

## 🌐 Доступ к приложению

После развертывания приложение будет доступно по адресу:
- **GitHub Pages**: `https://[ВАШ_USERNAME].github.io/weight-challenge-app`
- **Локально**: `http://localhost:8080`

## 💾 Хранение данных

Приложение использует **localStorage браузера** для хранения:
- Пользователей
- Челленджей
- Записей веса

**Данные сохраняются локально в браузере каждого пользователя!**
