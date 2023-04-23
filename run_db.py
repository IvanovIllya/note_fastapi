from backend.app.db.session import SessionLocal
from backend.app.db.init_db import init_db



def init():
    db = SessionLocal()
    init_db(db)


def main():
    logger.info('Run initialization')
    init()
    # try:
    #     init()
    # except Exception as error:
    #     logger.error(f"An error during db initialization {error}")
    # else:
    #     logger.info('End initialization')


if __name__ == "__main__":
    main()