from enum import Enum
from pydantic import BaseModel
from typing import Optional


class Status(Enum):
    SUCCESS = "success"
    ERROR = "error"


async def getResponse(status: Status,
                      data: any = None,
                      details: any = None) -> dict:

    return {
        "status": status,
        "data": data,
        "details": details
    }


class ResponseBaseSchema(BaseModel):
    status: Status
    # Extend this class and add data field
    details: Optional[str]
