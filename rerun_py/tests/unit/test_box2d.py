from __future__ import annotations

import itertools
from typing import Optional, cast

import rerun.experimental as rr2
from rerun.experimental import cmp as rrc
from rerun.experimental import dt as rrd

from .common_arrays import (
    class_ids_arrays,
    class_ids_expected,
    colors_arrays,
    colors_expected,
    draw_order_expected,
    draw_orders,
    instance_keys_arrays,
    instance_keys_expected,
    is_empty,
    labels_arrays,
    labels_expected,
    radii_arrays,
    radii_expected,
)
from .common_arrays import (
    vec2ds_arrays as centers_arrays,
)
from .common_arrays import (
    vec2ds_arrays as half_sizes_arrays,
)
from .common_arrays import (
    vec2ds_expected as centers_expected,
)
from .common_arrays import (
    vec2ds_expected as half_sizes_expected,
)


def test_boxes2d() -> None:
    all_arrays = itertools.zip_longest(
        half_sizes_arrays,
        centers_arrays,
        colors_arrays,
        radii_arrays,
        labels_arrays,
        draw_orders,
        class_ids_arrays,
        instance_keys_arrays,
    )

    for half_sizes, centers, colors, radii, labels, draw_order, class_ids, instance_keys in all_arrays:
        half_sizes = half_sizes if half_sizes is not None else half_sizes_arrays[-1]

        # make Pyright happy as it's apparently not able to track typing info trough zip_longest
        half_sizes = cast(rrd.Vec2DArrayLike, half_sizes)
        centers = cast(rrd.Vec2DArrayLike, centers)
        radii = cast(Optional[rrc.RadiusArrayLike], radii)
        colors = cast(Optional[rrd.ColorArrayLike], colors)
        labels = cast(Optional[rrd.Utf8ArrayLike], labels)
        draw_order = cast(Optional[rrc.DrawOrderArrayLike], draw_order)
        class_ids = cast(Optional[rrd.ClassIdArrayLike], class_ids)
        instance_keys = cast(Optional[rrc.InstanceKeyArrayLike], instance_keys)

        print(
            f"rr2.Boxes2D(\n"
            f"    half_sizes={half_sizes}\n"
            f"    centers={centers}\n"
            f"    radii={radii}\n"
            f"    colors={colors}\n"
            f"    labels={labels}\n"
            f"    draw_order={draw_order}\n"
            f"    class_ids={class_ids}\n"
            f"    instance_keys={instance_keys}\n"
            f")"
        )
        arch = rr2.Boxes2D(
            half_sizes=half_sizes,
            centers=centers,
            radii=radii,
            colors=colors,
            labels=labels,
            draw_order=draw_order,
            class_ids=class_ids,
            instance_keys=instance_keys,
        )
        print(f"{arch}\n")

        assert arch.half_sizes == half_sizes_expected(is_empty(half_sizes), rrc.HalfSizes2DArray)
        assert arch.centers == centers_expected(is_empty(centers), rrc.Position2DArray)
        assert arch.colors == colors_expected(is_empty(colors))
        assert arch.radii == radii_expected(is_empty(radii))
        assert arch.labels == labels_expected(is_empty(labels))
        assert arch.draw_order == draw_order_expected(is_empty(draw_order))
        assert arch.class_ids == class_ids_expected(is_empty(class_ids))
        assert arch.instance_keys == instance_keys_expected(is_empty(instance_keys))


if __name__ == "__main__":
    test_boxes2d()
