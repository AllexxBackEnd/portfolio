from app.database import Base, engine, SessionLocal
from app.models.projects import Project


def create_db():
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()

    projects = [
        # --- Sites ---
        Project(
            name_en="Task Tracker",
            name_ru="Трекер задач",
            description_en="A full-stack task management app with user authentication, project boards, and real-time updates.",
            description_ru="Полноценное приложение для управления задачами с авторизацией, досками проектов и обновлениями в реальном времени.",
            image_url="assets/img/portfolio/sphere-01.jpg",
            live_url="https://task-tracker.example.com",
            github_url="https://github.com/username/task-tracker",
            technologies="FastAPI, PostgreSQL, SQLAlchemy, React",
            project_type="site",
        ),
        Project(
            name_en="Weather Dashboard",
            name_ru="Панель погоды",
            description_en="A responsive weather dashboard that fetches data from external APIs and displays forecasts with interactive charts.",
            description_ru="Адаптивная панель погоды, получающая данные из внешних API и отображающая прогнозы с интерактивными графиками.",
            image_url="assets/img/portfolio/sphere-02.jpg",
            live_url="https://weather.example.com",
            github_url="https://github.com/username/weather-dashboard",
            technologies="FastAPI, Redis, Chart.js, Jinja2",
            project_type="site",
        ),
        Project(
            name_en="URL Shortener",
            name_ru="Сокращатель ссылок",
            description_en="A high-performance URL shortener service with analytics, custom aliases, and rate limiting.",
            description_ru="Высокопроизводительный сервис сокращения ссылок с аналитикой, кастомными алиасами и ограничением запросов.",
            image_url="assets/img/portfolio/sphere-03.jpg",
            live_url="https://short.example.com",
            github_url="https://github.com/username/url-shortener",
            technologies="FastAPI, PostgreSQL, Redis, SQLAlchemy",
            project_type="site",
        ),
        # --- Bots ---
        Project(
            name_en="Expense Tracker Bot",
            name_ru="Бот учёта расходов",
            description_en="A Telegram bot for tracking personal expenses with categories, reports, and monthly summaries.",
            description_ru="Telegram-бот для учёта личных расходов с категориями, отчётами и ежемесячными сводками.",
            image_url="assets/img/portfolio/sphere-04.jpg",
            bot_url="https://t.me/expense_tracker_bot",
            github_url="https://github.com/username/expense-bot",
            technologies="Aiogram, SQLAlchemy, PostgreSQL, APScheduler",
            project_type="bot",
        ),
        Project(
            name_en="Quiz Bot",
            name_ru="Бот-викторина",
            description_en="An interactive quiz bot with multiple categories, leaderboards, and timed questions.",
            description_ru="Интерактивный бот-викторина с категориями, таблицей лидеров и вопросами на время.",
            image_url="assets/img/portfolio/sphere-01.jpg",
            bot_url="https://t.me/quiz_master_bot",
            github_url="https://github.com/username/quiz-bot",
            technologies="Aiogram, SQLAlchemy, Redis",
            project_type="bot",
        ),
        Project(
            name_en="Reminder Bot",
            name_ru="Бот напоминаний",
            description_en="A Telegram bot that schedules reminders with recurring events, timezone support, and inline mode.",
            description_ru="Telegram-бот для планирования напоминаний с повторяющимися событиями, поддержкой часовых поясов и инлайн-режимом.",
            image_url="assets/img/portfolio/sphere-02.jpg",
            bot_url="https://t.me/smart_reminder_bot",
            github_url="https://github.com/username/reminder-bot",
            technologies="Aiogram, SQLAlchemy, APScheduler, Redis",
            project_type="bot",
        ),
    ]

    session.add_all(projects)
    session.commit()
    session.close()
    print(f"Database created. {len(projects)} projects inserted.")


if __name__ == "__main__":
    create_db()
