from enum import Enum


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
