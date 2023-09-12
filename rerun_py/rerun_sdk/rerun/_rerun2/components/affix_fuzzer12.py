# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/testing/components/fuzzy.fbs".


from __future__ import annotations

from typing import Sequence, Union

import pyarrow as pa
from attrs import define, field

from .._baseclasses import (
    BaseExtensionArray,
    BaseExtensionType,
)

__all__ = ["AffixFuzzer12", "AffixFuzzer12Array", "AffixFuzzer12ArrayLike", "AffixFuzzer12Like", "AffixFuzzer12Type"]


@define
class AffixFuzzer12:
    # You can define your own __init__ function by defining a function called "affix_fuzzer12__init_override"

    many_strings_required: list[str] = field()


AffixFuzzer12Like = AffixFuzzer12
AffixFuzzer12ArrayLike = Union[
    AffixFuzzer12,
    Sequence[AffixFuzzer12Like],
]


# --- Arrow support ---


class AffixFuzzer12Type(BaseExtensionType):
    def __init__(self) -> None:
        pa.ExtensionType.__init__(
            self,
            pa.list_(pa.field("item", pa.utf8(), nullable=False, metadata={})),
            "rerun.testing.components.AffixFuzzer12",
        )


class AffixFuzzer12Array(BaseExtensionArray[AffixFuzzer12ArrayLike]):
    _EXTENSION_NAME = "rerun.testing.components.AffixFuzzer12"
    _EXTENSION_TYPE = AffixFuzzer12Type

    @staticmethod
    def _native_to_pa_array(data: AffixFuzzer12ArrayLike, data_type: pa.DataType) -> pa.Array:
        raise NotImplementedError  # You need to implement "affix_fuzzer12__native_to_pa_array_override" in rerun_py/rerun_sdk/rerun/_rerun2/components/_overrides/affix_fuzzer12.py


AffixFuzzer12Type._ARRAY_TYPE = AffixFuzzer12Array

# TODO(cmc): bring back registration to pyarrow once legacy types are gone
# pa.register_extension_type(AffixFuzzer12Type())
