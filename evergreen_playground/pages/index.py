import reflex as rx
from ..views.sidebar import sidebar
from ..backend.generation import GeneratorState, CopyLocalState, copy_script
from reflex_img_comparison_slider import img_comparison_slider
from ..components.react_zoom import image_zoom
from typing import Union
from .. import styles


def _image_ui() -> rx.Component:
    return rx.cond(
        GeneratorState.upscaled_image
        & ~GeneratorState.is_generating,  # If upscaled image is available and not generating
        img_comparison_slider(
            rx.image(
                src=GeneratorState.output_image, slot="first", **styles.image_props
            ),
            rx.image(
                src=GeneratorState.upscaled_image, slot="second", **styles.image_props
            ),
        ),
        rx.cond(
            ~GeneratorState.is_generating,
            image_zoom(rx.image(src=GeneratorState.output_image, **styles.image_props)),
            rx.skeleton(
                rx.box(rx.image(src=GeneratorState.output_image, **styles.image_props)),
                loading=GeneratorState.is_generating,
            ),
        ),
    )


def _image_list_item(image: str) -> rx.Component:
    return rx.skeleton(
        rx.box(
            rx.image(
                src=image,
                width="100%",
                height="100%",
                decoding="auto",
                style={
                    "transform": rx.cond(
                        image == GeneratorState.output_image,
                        "scale(0.875)",
                        "",
                    ),
                    "filter": rx.cond(
                        image == GeneratorState.output_image,
                        "",
                        "brightness(.75)",
                    ),
                },
                loading="lazy",
                alt="Output image option",
                transition="all 0.2s ease",
                object_fit="cover",
            ),
            width="auto",
            aspect_ratio="1/1",
            max_height="5em",
            max_width="5em",
            cursor="pointer",
            background=rx.color("accent", 9),
            on_click=GeneratorState.setvar("output_image", image),
        ),
    )


def _image_list() -> rx.Component:
    return rx.scroll_area(
        rx.hstack(
            rx.foreach(
                GeneratorState.output_list,
                _image_list_item,
            ),
            spacing="4",
            width="100%",
            align="center",
        ),
        display=rx.cond(
            GeneratorState.output_list,
            "flex",
            "none",
        ),
        type="auto",
        scrollbars="horizontal",
    )


@rx.page(
    "/",
    title="AI Image Generator - Reflex",
    description="Generate an image using AI with Reflex",
)
def index():
    return rx.flex(
        CopyLocalState,
        sidebar(),
        rx.center(
            rx.vstack(
                _image_ui(),
                rx.hstack(
                    justify="end",
                    align="center",
                    width="100%",
                ),
                _image_list(),
                max_width=styles.content_max_width,
                height="100%",
                align="center",
                id="image-ui",
            ),
            width="100%",
            height="100%",
            padding=["1em", "1em", "1em", "3em"],
        ),
        flex_direction=["column", "column", "column", "row"],
        position="relative",
        width="100%",
        height="100%",
        bg=rx.color("gray", 1),
    )
