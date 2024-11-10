# Aiogram Bot Template

A structured template for building Telegram bots using the `aiogram` library and PostgreSQL. This template includes essential modules and configurations for easy setup and scalable bot development.

## Features

- **Database Integration**: Supports PostgreSQL with migrations managed by Alembic.
- **Modular Design**: Organized directories for handlers, middlewares, routers, and utilities.
- **Localization Support**: Pre-configured localization for multi-language bots.
- **Dependency Injection**: Simplifies passing dependencies within the bot.
- **Customizable Keyboards and Filters**: Easily set up custom keyboards and filters for user interaction.

## Project Structure

```
src/
├── alembic/                  # Directory for Alembic migrations
├── bot/
│   ├── database/             # Database models and connections
│   ├── filters/              # Custom filters for message handling
│   ├── keyboards/            # Inline and reply keyboards
│   ├── locales/              # Localization files (e.g., Russian language)
│   │   └── ru/LC_MESSAGES/   # Example locale (Russian)
│   ├── middlewares/          # Middleware components for logging, etc.
│   ├── repositories/         # Data access and repository pattern implementation
│   ├── routers/              # Routers to organize handlers
│   ├── utils/                # Utility functions and helpers
│   ├── __init__.py           # Initialization file for the bot module
│   ├── __main__.py           # Main bot entry point
│   ├── config_reader.py      # Configuration file for reading environment variables
│   ├── dependencies.py       # Dependency management and injection
│   └── ui_commands.py        # Command UI setup
├── alembic.ini               # Alembic configuration file
├── .gitignore                # Git ignore file
├── LICENSE                   # License information
├── README.md                 # Project documentation
├── env-dist                  # Example .env file
└── requirements.txt          # Python dependencies
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/aiogram-bot-template.git
   cd aiogram-bot-template
   ```

2. **Set Up the Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   - Create a `.env` file by copying `env-dist`:
     ```bash
     cp env-dist .env
     ```
   - Update `.env` with your Telegram bot token and database connection details:
     ```
     BOT_TOKEN=your-telegram-bot-token
     DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
     ```

5. **Run Database Migrations**
   ```bash
   alembic upgrade head
   ```

6. **Start the Bot**
   ```bash
   python src/bot/__main__.py
   ```

## Key Components

- **Database**: Located in `bot/database/`, with models and async connection handling.
- **Filters**: Custom filters for filtering incoming messages.
- **Keyboards**: Contains inline and reply keyboard setups.
- **Localization**: The `locales/` directory includes localization support, e.g., Russian language in `locales/ru/LC_MESSAGES/`.
- **Middlewares**: Middlewares for logging or preprocessing data.
- **Routers**: Organized message handlers for managing different bot commands and responses.
- **Utils**: Helper functions used throughout the bot codebase.

## Alembic for Migrations

The project uses Alembic for database migrations. To generate a new migration after modifying models, run:
```bash
alembic revision --autogenerate -m "Migration message"
```

## Contributing

Pull requests and feature suggestions are welcome. Please fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
