import sqlite3
from datetime import datetime
from pathlib import Path


class BackupService:
    def __init__(self, database_path):
        self.database_path = database_path

    def create_backup(self, destination_directory):
        destination_directory = Path(
            destination_directory
        )

        destination_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        backup_name = (
            f"moneyze_backup_{timestamp}.db"
        )

        destination_path = (
            destination_directory / backup_name
        )

        source = sqlite3.connect(
            self.database_path
        )

        destination = sqlite3.connect(
            destination_path
        )

        try:
            with destination:
                source.backup(destination)

        finally:
            source.close()
            destination.close()

        return destination_path

    def validate_backup(self, backup_path):
        backup_path = Path(backup_path)

        if not backup_path.exists():
            return False

        if not backup_path.is_file():
            return False

        try:
            connection = sqlite3.connect(
                backup_path
            )

            cursor = connection.cursor()

            cursor.execute(
                "PRAGMA integrity_check;"
            )

            result = cursor.fetchone()

            connection.close()

            return result == ("ok",)

        except sqlite3.Error:
            return False

    def restore_backup(self, backup_path):
        backup_path = Path(backup_path)

        if not self.validate_backup(backup_path):
            raise ValueError(
                "O arquivo selecionado não é um backup SQLite válido."
            )

        database_path = Path(
            self.database_path
        )

        rollback_path = database_path.with_name(
            f".{database_path.stem}_restore_backup.db"
        )

        current_database = sqlite3.connect(
            database_path
        )

        rollback_database = sqlite3.connect(
            rollback_path
        )

        try:
            with rollback_database:
                current_database.backup(
                    rollback_database
                )

        finally:
            current_database.close()
            rollback_database.close()

        try:
            backup_database = sqlite3.connect(
                backup_path
            )

            current_database = sqlite3.connect(
                database_path
            )

            try:
                with current_database:
                    backup_database.backup(
                        current_database
                    )

            finally:
                backup_database.close()
                current_database.close()

        except Exception:
            try:
                rollback_database = sqlite3.connect(
                    rollback_path
                )

                current_database = sqlite3.connect(
                    database_path
                )

                try:
                    with current_database:
                        rollback_database.backup(
                            current_database
                        )

                finally:
                    rollback_database.close()
                    current_database.close()

            finally:
                if rollback_path.exists():
                    rollback_path.unlink()

            raise

        if rollback_path.exists():
            rollback_path.unlink()

        return True