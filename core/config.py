from pathlib import Path


APP_NAME = "MoneyZe"

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

APP_VERSION = "1.0.0"

SIDEBAR_WIDTH = 250


if Path.home().joinpath(
    "AppData",
    "Roaming",
).exists():

    DATA_DIRECTORY = (
        Path.home()
        / "AppData"
        / "Roaming"
        / APP_NAME
    )

else:

    DATA_DIRECTORY = (
        Path.home()
        / f".{APP_NAME.lower()}"
    )


DATA_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True,
)

DATABASE_NAME = "moneyze.db"

DATABASE_PATH = (
    DATA_DIRECTORY
    / DATABASE_NAME
)