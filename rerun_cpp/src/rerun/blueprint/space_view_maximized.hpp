// DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/re_types/definitions/rerun/blueprint/space_view_maximized.fbs".

#pragma once

#include "../result.hpp"

#include <cstdint>
#include <memory>
#include <optional>
#include <utility>
#include <vector>

namespace arrow {
    class DataType;
    class ListBuilder;
    class MemoryPool;
} // namespace arrow

namespace rerun {
    namespace blueprint {
        /// **Blueprint**: Whether a space view is maximized.
        ///
        /// Unstable. Used for the ongoing blueprint experimentations.
        struct SpaceViewMaximized {
            std::optional<std::vector<uint8_t>> id;

          public:
            SpaceViewMaximized() = default;

            SpaceViewMaximized(std::optional<std::vector<uint8_t>> id_) : id(std::move(id_)) {}

            SpaceViewMaximized& operator=(std::optional<std::vector<uint8_t>> id_) {
                id = std::move(id_);
                return *this;
            }

            /// Returns the arrow data type this type corresponds to.
            static const std::shared_ptr<arrow::DataType>& arrow_datatype();

            /// Creates a new array builder with an array of this type.
            static Result<std::shared_ptr<arrow::ListBuilder>> new_arrow_array_builder(
                arrow::MemoryPool* memory_pool
            );

            /// Fills an arrow array builder with an array of this type.
            static Error fill_arrow_array_builder(
                arrow::ListBuilder* builder, const SpaceViewMaximized* elements, size_t num_elements
            );
        };
    } // namespace blueprint
} // namespace rerun