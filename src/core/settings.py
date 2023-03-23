from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str
    port: int
    debug: bool
    dev_tools_props_check: bool
    back_url: str


settings = Settings(
    _env_file='../.env',
    _env_file_encoding='utf-8',
)
