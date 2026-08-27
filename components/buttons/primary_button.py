import qtawesome as qta

from PySide6.QtWidgets import QPushButton


class PrimaryButton(QPushButton):

    def __init__(
        self,
        text: str,
        icon_name: str | None = None,
    ):
        super().__init__(text)

        self.setObjectName(
            "primaryButton"
        )

        if icon_name:

            self.setIcon(
                qta.icon(
                    icon_name,
                    color="white",
                )
            )