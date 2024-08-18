from pathlib import Path
import os
from dotenv import load_dotenv

def load_settings():
    """Carrega as configurações a partir de variáveis de ambiente."""
    dotenv_path = Path.cwd() / '.env'
    load_dotenv(dotenv_path=dotenv_path)

    settings = {
        "user": os.getenv("USER"),
        "password": os.getenv("PASSWORD"),
        "db": os.getenv("DB"),
        "host": os.getenv("HOST"),
        "api_key": os.getenv("API_KEY"),
        "port": os.getenv("PORT"),
    }
    return settings