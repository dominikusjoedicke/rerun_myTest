// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/store/re_types/definitions/rerun/components/albedo_factor.fbs".

#pragma once

#include "../datatypes/rgba32.hpp"
#include "../result.hpp"

#include <cstdint>
#include <memory>

namespace rerun::components {
    /// **Component**: A color multiplier, usually applied to a whole entity, e.g. a mesh.
    struct AlbedoFactor {
        rerun::datatypes::Rgba32 albedo_factor;

      public:
        AlbedoFactor() = default;

        AlbedoFactor(rerun::datatypes::Rgba32 albedo_factor_) : albedo_factor(albedo_factor_) {}

        AlbedoFactor& operator=(rerun::datatypes::Rgba32 albedo_factor_) {
            albedo_factor = albedo_factor_;
            return *this;
        }

        AlbedoFactor(uint32_t rgba_) : albedo_factor(rgba_) {}

        AlbedoFactor& operator=(uint32_t rgba_) {
            albedo_factor = rgba_;
            return *this;
        }

        /// Cast to the underlying Rgba32 datatype
        operator rerun::datatypes::Rgba32() const {
            return albedo_factor;
        }
    };
} // namespace rerun::components

namespace rerun {
    static_assert(sizeof(rerun::datatypes::Rgba32) == sizeof(components::AlbedoFactor));

    /// \private
    template <>
    struct Loggable<components::AlbedoFactor> {
        static constexpr const char Name[] = "rerun.components.AlbedoFactor";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype() {
            return Loggable<rerun::datatypes::Rgba32>::arrow_datatype();
        }

        /// Serializes an array of `rerun::components::AlbedoFactor` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const components::AlbedoFactor* instances, size_t num_instances
        ) {
            return Loggable<rerun::datatypes::Rgba32>::to_arrow(
                &instances->albedo_factor,
                num_instances
            );
        }
    };
} // namespace rerun