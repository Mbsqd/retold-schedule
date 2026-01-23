from src.alert.client import AlertClient
from src.alert.service import AlertService
from src.config import settings


async def get_alert_service() -> AlertService:
    client = AlertClient(settings.alert_api_token, settings.alert_api_base_url, 10)
    await client.start()

    return AlertService(client)
