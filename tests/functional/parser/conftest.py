from typing import Any, Dict

import pytest
from pydantic import BaseModel, ValidationError

from aws_lambda_powertools.utilities.parser.envelopes.base import BaseEnvelope
from aws_lambda_powertools.utilities.parser.exceptions import SchemaValidationError


@pytest.fixture
def dummy_event():
    return {"payload": {"message": "hello world"}}


@pytest.fixture
def dummy_schema():
    """Wanted payload structure"""

    class MyDummyModel(BaseModel):
        message: str

    return MyDummyModel


@pytest.fixture
def dummy_envelope_schema():
    """Event wrapper structure"""

    class MyDummyEnvelopeSchema(BaseModel):
        payload: Dict

    return MyDummyEnvelopeSchema


@pytest.fixture
def dummy_envelope(dummy_envelope_schema):
    class MyDummyEnvelope(BaseEnvelope):
        """Unwrap dummy event within payload key"""

        def parse(self, event: Dict[str, Any], schema: BaseModel):
            try:
                parsed_enveloped = dummy_envelope_schema(**event)
            except (ValidationError, TypeError) as e:
                raise SchemaValidationError("Dummy input doesn't conform with schema") from e
            return self._parse(event=parsed_enveloped.payload, schema=schema)

    return MyDummyEnvelope