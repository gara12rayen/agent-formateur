from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):


    DB_HOST:     str = "localhost"
    DB_PORT:     int = 3306
    DB_USER:     str = "root"
    DB_PASSWORD: str 
    DB_NAME:     str 

    SECRET_KEY:               str
    ALGORITHM:                str 
    ACCESS_TOKEN_EXPIRE_DAYS: int 

    UPLOAD_DIR:    str 
    MAX_UPLOAD_MB: int 

    GROQ_API_KEY: str 
  
    MAIL_USER:      str 
    MAIL_PASS:      str
    MAIL_FROM_NAME: str 

    
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?charset=utf8mb4"
        )

    model_config = {
        "env_file":  ".env",
        "extra":     "ignore", 
    }


@lru_cache
def get_settings() -> Settings:
    return Settings()
