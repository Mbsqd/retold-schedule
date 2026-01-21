from src.alert.client import AlertClient
from src.alert.enums import AlertStatusResponseEnum


class AlertService:
    def __init__(self, alert_client: AlertClient) -> None:
        self.client: AlertClient = alert_client

    async def is_air_raid_active(self, uid: int) -> bool:
        status: AlertStatusResponseEnum = await self.client.get_air_raid_status(uid)

        return status in (
            AlertStatusResponseEnum.A,
            AlertStatusResponseEnum.P,
        )
