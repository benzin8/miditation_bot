import asyncio
from core.database import create_tables
from backend.models import *

async def main():
    await create_tables()
    print(f"Tables created: {list(Base.metadata.tables.keys())} successfully.")

if __name__ == "__main__":
    asyncio.run(main())