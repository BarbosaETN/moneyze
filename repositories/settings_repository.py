from repositories.base_repository import BaseRepository

from database.models.setting import Setting


class SettingsRepository(BaseRepository):

    def __init__(self, session):

        super().__init__(
            session,
            Setting,
        )

    def get_by_key(
        self,
        key,
    ):

        return (
            self.session
            .query(Setting)
            .filter(
                Setting.key == key
            )
            .first()
        )