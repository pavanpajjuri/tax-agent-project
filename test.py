import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Ping(BaseModel):
    ok: bool = True

print("Python runs")
print("Pydantic model:", Ping().model_dump())
print("ENV TEST (DUMMY_KEY):", os.getenv("DUMMY_KEY"))