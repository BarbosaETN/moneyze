from core.config import DATABASE_PATH
from services.backup_service import BackupService

backup_service = BackupService(DATABASE_PATH)

print(
    backup_service.validate_backup(
        "arquivo_inválido.db"
    )
)