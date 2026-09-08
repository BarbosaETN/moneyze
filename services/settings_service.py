from repositories.settings_repository import (
    SettingsRepository,
)


class SettingsService:

    def __init__(
        self,
        repository,
    ):

        self.repository = repository

    def get_setting(
        self,
        key,
        default=None,
    ):

        setting = (
            self.repository
            .get_by_key(key)
        )

        if setting is None:
            return default

        return setting.value

    def set_setting(
        self,
        key,
        value,
    ):

        setting = (
            self.repository
            .get_by_key(key)
        )

        if setting is None:

            return self.repository.create(
                key=key,
                value=str(value),
            )

        setting.value = str(value)

        return self.repository.update(
            setting
        )

    def get_all_settings(self):

        settings = (
            self.repository
            .get_all()
        )

        return {
            setting.key: setting.value
            for setting in settings
        }