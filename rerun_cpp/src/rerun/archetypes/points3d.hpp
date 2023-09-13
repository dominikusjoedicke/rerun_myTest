// DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/re_types/definitions/rerun/archetypes/points3d.fbs".

#pragma once

#include "../arrow.hpp"
#include "../component_batch.hpp"
#include "../components/class_id.hpp"
#include "../components/color.hpp"
#include "../components/instance_key.hpp"
#include "../components/keypoint_id.hpp"
#include "../components/position3d.hpp"
#include "../components/radius.hpp"
#include "../components/text.hpp"
#include "../data_cell.hpp"
#include "../result.hpp"

#include <cstdint>
#include <optional>
#include <utility>
#include <vector>

namespace rerun {
    namespace archetypes {
        /// A 3D point cloud with positions and optional colors, radii, labels, etc.
        ///
        /// ## Example
        ///
        ///```
        ///// Log some very simple points.
        ///
        /// #include <rerun.hpp>
        ///
        /// namespace rr = rerun;
        ///
        /// int main() {
        ///    auto rec = rr::RecordingStream("rerun_example_points3d_simple");
        ///    rec.connect("127.0.0.1:9876").throw_on_failure();
        ///
        ///    rec.log("points", rr::Points3D({{0.0f, 0.0f, 0.0f}, {1.0f, 1.0f, 1.0f}}));
        /// }
        ///```
        struct Points3D {
            /// All the 3D positions at which the point cloud shows points.
            std::vector<rerun::components::Position3D> positions;

            /// Optional radii for the points, effectively turning them into circles.
            std::optional<std::vector<rerun::components::Radius>> radii;

            /// Optional colors for the points.
            std::optional<std::vector<rerun::components::Color>> colors;

            /// Optional text labels for the points.
            std::optional<std::vector<rerun::components::Text>> labels;

            /// Optional class Ids for the points.
            ///
            /// The class ID provides colors and labels if not specified explicitly.
            std::optional<std::vector<rerun::components::ClassId>> class_ids;

            /// Optional keypoint IDs for the points, identifying them within a class.
            ///
            /// If keypoint IDs are passed in but no class IDs were specified, the class ID will
            /// default to 0.
            /// This is useful to identify points within a single classification (which is
            /// identified with `class_id`). E.g. the classification might be 'Person' and the
            /// keypoints refer to joints on a detected skeleton.
            std::optional<std::vector<rerun::components::KeypointId>> keypoint_ids;

            /// Unique identifiers for each individual point in the batch.
            std::optional<std::vector<rerun::components::InstanceKey>> instance_keys;

            /// Name of the indicator component, used to identify the archetype when converting to a
            /// list of components.
            static const char INDICATOR_COMPONENT_NAME[];

          public:
            Points3D() = default;

            Points3D(std::vector<rerun::components::Position3D> _positions)
                : positions(std::move(_positions)) {}

            Points3D(rerun::components::Position3D _positions)
                : positions(1, std::move(_positions)) {}

            /// Optional radii for the points, effectively turning them into circles.
            Points3D& with_radii(std::vector<rerun::components::Radius> _radii) {
                radii = std::move(_radii);
                return *this;
            }

            /// Optional radii for the points, effectively turning them into circles.
            Points3D& with_radii(rerun::components::Radius _radii) {
                radii = std::vector(1, std::move(_radii));
                return *this;
            }

            /// Optional colors for the points.
            Points3D& with_colors(std::vector<rerun::components::Color> _colors) {
                colors = std::move(_colors);
                return *this;
            }

            /// Optional colors for the points.
            Points3D& with_colors(rerun::components::Color _colors) {
                colors = std::vector(1, std::move(_colors));
                return *this;
            }

            /// Optional text labels for the points.
            Points3D& with_labels(std::vector<rerun::components::Text> _labels) {
                labels = std::move(_labels);
                return *this;
            }

            /// Optional text labels for the points.
            Points3D& with_labels(rerun::components::Text _labels) {
                labels = std::vector(1, std::move(_labels));
                return *this;
            }

            /// Optional class Ids for the points.
            ///
            /// The class ID provides colors and labels if not specified explicitly.
            Points3D& with_class_ids(std::vector<rerun::components::ClassId> _class_ids) {
                class_ids = std::move(_class_ids);
                return *this;
            }

            /// Optional class Ids for the points.
            ///
            /// The class ID provides colors and labels if not specified explicitly.
            Points3D& with_class_ids(rerun::components::ClassId _class_ids) {
                class_ids = std::vector(1, std::move(_class_ids));
                return *this;
            }

            /// Optional keypoint IDs for the points, identifying them within a class.
            ///
            /// If keypoint IDs are passed in but no class IDs were specified, the class ID will
            /// default to 0.
            /// This is useful to identify points within a single classification (which is
            /// identified with `class_id`). E.g. the classification might be 'Person' and the
            /// keypoints refer to joints on a detected skeleton.
            Points3D& with_keypoint_ids(std::vector<rerun::components::KeypointId> _keypoint_ids) {
                keypoint_ids = std::move(_keypoint_ids);
                return *this;
            }

            /// Optional keypoint IDs for the points, identifying them within a class.
            ///
            /// If keypoint IDs are passed in but no class IDs were specified, the class ID will
            /// default to 0.
            /// This is useful to identify points within a single classification (which is
            /// identified with `class_id`). E.g. the classification might be 'Person' and the
            /// keypoints refer to joints on a detected skeleton.
            Points3D& with_keypoint_ids(rerun::components::KeypointId _keypoint_ids) {
                keypoint_ids = std::vector(1, std::move(_keypoint_ids));
                return *this;
            }

            /// Unique identifiers for each individual point in the batch.
            Points3D& with_instance_keys(std::vector<rerun::components::InstanceKey> _instance_keys
            ) {
                instance_keys = std::move(_instance_keys);
                return *this;
            }

            /// Unique identifiers for each individual point in the batch.
            Points3D& with_instance_keys(rerun::components::InstanceKey _instance_keys) {
                instance_keys = std::vector(1, std::move(_instance_keys));
                return *this;
            }

            /// Returns the number of primary instances of this archetype.
            size_t num_instances() const {
                return positions.size();
            }

            /// Collections all component lists into a list of component collections. *Attention:*
            /// The returned vector references this instance and does not take ownership of any
            /// data. Adding any new components to this archetype will invalidate the returned
            /// component lists!
            std::vector<AnonymousComponentBatch> as_component_batches() const;
        };
    } // namespace archetypes
} // namespace rerun
