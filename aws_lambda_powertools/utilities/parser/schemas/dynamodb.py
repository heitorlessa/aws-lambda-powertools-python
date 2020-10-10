from datetime import date
from typing import Any, Dict, List, Optional

from pydantic import BaseModel
from typing_extensions import Literal


class DynamoScheme(BaseModel):
    ApproximateCreationDateTime: Optional[date]
    Keys: Dict[str, Dict[str, Any]]
    NewImage: Optional[Dict[str, Any]]
    OldImage: Optional[Dict[str, Any]]
    SequenceNumber: str
    SizeBytes: int
    StreamViewType: Literal["NEW_AND_OLD_IMAGES", "KEYS_ONLY", "NEW_IMAGE", "OLD_IMAGE"]

    # context on why it's commented: https://github.com/awslabs/aws-lambda-powertools-python/pull/118
    # since both images are optional, they can both be None. However, at least one must
    # exist in a legal schema of NEW_AND_OLD_IMAGES type
    # @root_validator
    # def check_one_image_exists(cls, values): # noqa: E800
    #     new_img, old_img = values.get("NewImage"), values.get("OldImage") # noqa: E800
    #     stream_type = values.get("StreamViewType") # noqa: E800
    #     if stream_type == "NEW_AND_OLD_IMAGES" and not new_img and not old_img: # noqa: E800
    #         raise TypeError("DynamoDB streams schema failed validation, missing both new & old stream images") # noqa: E800,E501
    #     return values # noqa: E800


class UserIdentity(BaseModel):
    type: Literal["Service"]  # noqa: VNE003, A003
    principalId: Literal["dynamodb.amazonaws.com"]


class DynamoRecordSchema(BaseModel):
    eventID: str
    eventName: Literal["INSERT", "MODIFY", "REMOVE"]
    eventVersion: float
    eventSource: Literal["aws:dynamodb"]
    awsRegion: str
    eventSourceARN: str
    dynamodb: DynamoScheme
    userIdentity: Optional[UserIdentity]


class DynamoDBSchema(BaseModel):
    Records: List[DynamoRecordSchema]