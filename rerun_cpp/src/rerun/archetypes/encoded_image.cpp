// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/store/re_types/definitions/rerun/archetypes/encoded_image.fbs".

#include "encoded_image.hpp"

#include "../collection_adapter_builtins.hpp"

namespace rerun::archetypes {}

namespace rerun {

    Result<std::vector<ComponentBatch>> AsComponents<archetypes::EncodedImage>::serialize(
        const archetypes::EncodedImage& archetype
    ) {
        using namespace archetypes;
        std::vector<ComponentBatch> cells;
        cells.reserve(5);

        {
            auto result = ComponentBatch::from_loggable(
                archetype.blob,
                ComponentDescriptor(
                    "rerun.archetypes.EncodedImage",
                    "blob",
                    "rerun.components.Blob"
                )
            );
            RR_RETURN_NOT_OK(result.error);
            cells.push_back(std::move(result.value));
        }
        if (archetype.media_type.has_value()) {
            auto result = ComponentBatch::from_loggable(
                archetype.media_type.value(),
                ComponentDescriptor(
                    "rerun.archetypes.EncodedImage",
                    "media_type",
                    "rerun.components.MediaType"
                )
            );
            RR_RETURN_NOT_OK(result.error);
            cells.push_back(std::move(result.value));
        }
        if (archetype.opacity.has_value()) {
            auto result = ComponentBatch::from_loggable(
                archetype.opacity.value(),
                ComponentDescriptor(
                    "rerun.archetypes.EncodedImage",
                    "opacity",
                    "rerun.components.Opacity"
                )
            );
            RR_RETURN_NOT_OK(result.error);
            cells.push_back(std::move(result.value));
        }
        if (archetype.draw_order.has_value()) {
            auto result = ComponentBatch::from_loggable(
                archetype.draw_order.value(),
                ComponentDescriptor(
                    "rerun.archetypes.EncodedImage",
                    "draw_order",
                    "rerun.components.DrawOrder"
                )
            );
            RR_RETURN_NOT_OK(result.error);
            cells.push_back(std::move(result.value));
        }
        {
            auto indicator = EncodedImage::IndicatorComponent();
            auto result = ComponentBatch::from_loggable(indicator);
            RR_RETURN_NOT_OK(result.error);
            cells.emplace_back(std::move(result.value));
        }

        return cells;
    }
} // namespace rerun
