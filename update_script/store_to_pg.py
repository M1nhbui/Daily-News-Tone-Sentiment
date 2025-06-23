from db.db_config import engine
from db.models import NewsSentiment
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Session = sessionmaker(bind=engine)

def store_record(cleaned_text, tone, source="Unknown", timestamp=None):
    session = Session()
    try:
        record = NewsSentiment(
            timestamp=timestamp or datetime.utcnow(),
            source=source,
            cleaned_text=cleaned_text,
            tone=tone
        )
        session.add(record)
        session.commit()
        print("✅ Stored to DB")
    except Exception as e:
        session.rollback()
        print("❌ Error:", e)
    finally:
        session.close()
