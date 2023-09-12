# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/datatypes/translation_rotation_scale3d.fbs".


from __future__ import annotations

from typing import Sequence, Union

import pyarrow as pa
from attrs import define, field

from .. import datatypes
from .._baseclasses import (
    BaseExtensionArray,
    BaseExtensionType,
)
from ._overrides import translation_rotation_scale3d__init_override  # noqa: F401

__all__ = [
    "TranslationRotationScale3D",
    "TranslationRotationScale3DArray",
    "TranslationRotationScale3DArrayLike",
    "TranslationRotationScale3DLike",
    "TranslationRotationScale3DType",
]


def _translation_rotation_scale3d__translation__special_field_converter_override(
    x: datatypes.Vec3DLike | None,
) -> datatypes.Vec3D | None:
    if x is None:
        return None
    elif isinstance(x, datatypes.Vec3D):
        return x
    else:
        return datatypes.Vec3D(x)


def _translation_rotation_scale3d__rotation__special_field_converter_override(
    x: datatypes.Rotation3DLike | None,
) -> datatypes.Rotation3D | None:
    if x is None:
        return None
    elif isinstance(x, datatypes.Rotation3D):
        return x
    else:
        return datatypes.Rotation3D(x)


def _translation_rotation_scale3d__scale__special_field_converter_override(
    x: datatypes.Scale3DLike | None,
) -> datatypes.Scale3D | None:
    if x is None:
        return None
    elif isinstance(x, datatypes.Scale3D):
        return x
    else:
        return datatypes.Scale3D(x)


@define(init=False)
class TranslationRotationScale3D:
    """Representation of an affine transform via separate translation, rotation & scale."""

    def __init__(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        translation_rotation_scale3d__init_override(self, *args, **kwargs)

    from_parent: bool = field(converter=bool)
    """
    If true, the transform maps from the parent space to the space where the transform was logged.
    Otherwise, the transform maps from the space to its parent.
    """

    translation: datatypes.Vec3D | None = field(
        default=None, converter=_translation_rotation_scale3d__translation__special_field_converter_override
    )
    """
    3D translation vector, applied last.
    """

    rotation: datatypes.Rotation3D | None = field(
        default=None, converter=_translation_rotation_scale3d__rotation__special_field_converter_override
    )
    """
    3D rotation, applied second.
    """

    scale: datatypes.Scale3D | None = field(
        default=None, converter=_translation_rotation_scale3d__scale__special_field_converter_override
    )
    """
    3D scale, applied first.
    """


TranslationRotationScale3DLike = TranslationRotationScale3D
TranslationRotationScale3DArrayLike = Union[
    TranslationRotationScale3D,
    Sequence[TranslationRotationScale3DLike],
]


# --- Arrow support ---


class TranslationRotationScale3DType(BaseExtensionType):
    def __init__(self) -> None:
        pa.ExtensionType.__init__(
            self,
            pa.struct(
                [
                    pa.field(
                        "translation",
                        pa.list_(pa.field("item", pa.float32(), nullable=False, metadata={}), 3),
                        nullable=True,
                        metadata={},
                    ),
                    pa.field(
                        "rotation",
                        pa.dense_union(
                            [
                                pa.field("_null_markers", pa.null(), nullable=True, metadata={}),
                                pa.field(
                                    "Quaternion",
                                    pa.list_(pa.field("item", pa.float32(), nullable=False, metadata={}), 4),
                                    nullable=False,
                                    metadata={},
                                ),
                                pa.field(
                                    "AxisAngle",
                                    pa.struct(
                                        [
                                            pa.field(
                                                "axis",
                                                pa.list_(
                                                    pa.field("item", pa.float32(), nullable=False, metadata={}), 3
                                                ),
                                                nullable=False,
                                                metadata={},
                                            ),
                                            pa.field(
                                                "angle",
                                                pa.dense_union(
                                                    [
                                                        pa.field(
                                                            "_null_markers", pa.null(), nullable=True, metadata={}
                                                        ),
                                                        pa.field("Radians", pa.float32(), nullable=False, metadata={}),
                                                        pa.field("Degrees", pa.float32(), nullable=False, metadata={}),
                                                    ]
                                                ),
                                                nullable=False,
                                                metadata={},
                                            ),
                                        ]
                                    ),
                                    nullable=False,
                                    metadata={},
                                ),
                            ]
                        ),
                        nullable=True,
                        metadata={},
                    ),
                    pa.field(
                        "scale",
                        pa.dense_union(
                            [
                                pa.field("_null_markers", pa.null(), nullable=True, metadata={}),
                                pa.field(
                                    "ThreeD",
                                    pa.list_(pa.field("item", pa.float32(), nullable=False, metadata={}), 3),
                                    nullable=False,
                                    metadata={},
                                ),
                                pa.field("Uniform", pa.float32(), nullable=False, metadata={}),
                            ]
                        ),
                        nullable=True,
                        metadata={},
                    ),
                    pa.field("from_parent", pa.bool_(), nullable=False, metadata={}),
                ]
            ),
            "rerun.datatypes.TranslationRotationScale3D",
        )


class TranslationRotationScale3DArray(BaseExtensionArray[TranslationRotationScale3DArrayLike]):
    _EXTENSION_NAME = "rerun.datatypes.TranslationRotationScale3D"
    _EXTENSION_TYPE = TranslationRotationScale3DType

    @staticmethod
    def _native_to_pa_array(data: TranslationRotationScale3DArrayLike, data_type: pa.DataType) -> pa.Array:
        raise NotImplementedError  # You need to implement "translation_rotation_scale3d__native_to_pa_array_override" in rerun_py/rerun_sdk/rerun/_rerun2/datatypes/_overrides/translation_rotation_scale3d.py


TranslationRotationScale3DType._ARRAY_TYPE = TranslationRotationScale3DArray

# TODO(cmc): bring back registration to pyarrow once legacy types are gone
# pa.register_extension_type(TranslationRotationScale3DType())
