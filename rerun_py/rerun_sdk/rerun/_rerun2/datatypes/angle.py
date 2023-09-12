# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/datatypes/angle.fbs".


from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal, Sequence, Union

import pyarrow as pa
from attrs import define, field

from .._baseclasses import (
    BaseExtensionArray,
    BaseExtensionType,
)
from ._overrides import angle__init_override  # noqa: F401

__all__ = ["Angle", "AngleArray", "AngleArrayLike", "AngleLike", "AngleType"]


@define(init=False)
class Angle:
    """Angle in either radians or degrees."""

    def __init__(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        angle__init_override(self, *args, **kwargs)

    inner: float = field(converter=float)
    """
    Radians (float):
        3D rotation angle in radians. Only one of `degrees` or `radians` should be set.

    Degrees (float):
        3D rotation angle in degrees. Only one of `degrees` or `radians` should be set.
    """

    kind: Literal["radians", "degrees"] = field(default="radians")


if TYPE_CHECKING:
    AngleLike = Union[
        Angle,
        float,
    ]
    AngleArrayLike = Union[
        Angle,
        float,
        Sequence[AngleLike],
    ]
else:
    AngleLike = Any
    AngleArrayLike = Any

# --- Arrow support ---


class AngleType(BaseExtensionType):
    def __init__(self) -> None:
        pa.ExtensionType.__init__(
            self,
            pa.dense_union(
                [
                    pa.field("_null_markers", pa.null(), nullable=True, metadata={}),
                    pa.field("Radians", pa.float32(), nullable=False, metadata={}),
                    pa.field("Degrees", pa.float32(), nullable=False, metadata={}),
                ]
            ),
            "rerun.datatypes.Angle",
        )


class AngleArray(BaseExtensionArray[AngleArrayLike]):
    _EXTENSION_NAME = "rerun.datatypes.Angle"
    _EXTENSION_TYPE = AngleType

    @staticmethod
    def _native_to_pa_array(data: AngleArrayLike, data_type: pa.DataType) -> pa.Array:
        raise NotImplementedError  # You need to implement "angle__native_to_pa_array_override" in rerun_py/rerun_sdk/rerun/_rerun2/datatypes/_overrides/angle.py


AngleType._ARRAY_TYPE = AngleArray

# TODO(cmc): bring back registration to pyarrow once legacy types are gone
# pa.register_extension_type(AngleType())
