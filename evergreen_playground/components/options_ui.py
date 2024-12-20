import reflex as rx
from .. import styles
from ..backend.options import OptionsState
from ..backend.generation import GeneratorState


def sidebar_header() -> rx.Component:
    return rx.hstack(
        rx.text("🌲 Playground", size="5"),
        rx.spacer(),
        rx.color_mode.button(
            style={"padding": "0", "height": "1.15em", "width": "1.15em"},
        ),
        align="center",
        width="100%",
        border_bottom=styles.border,
        padding="1em",
    )


def endpoint() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon("type", size=17, color=rx.color("green", 9)),
            rx.text("Endpoint", size="3"),
            rx.spacer(),
            rx.hstack(
                rx.cond(
                    OptionsState.endpoint,
                    rx.icon(
                        "eraser",
                        size=20,
                        color=rx.color("gray", 10),
                        cursor="pointer",
                        _hover={"opacity": "0.8"},
                        on_click=OptionsState.setvar("endpoint", ""),
                    ),
                ),
                spacing="4",
                align="center",
            ),
            spacing="2",
            align="center",
            width="100%",
        ),
        rx.input(
            placeholder="What do you want to see?",
            width="100%",
            height="30px",
            size="3",
            value=OptionsState.endpoint,
            on_change=OptionsState.set_endpoint,
        ),
        width="100%",
    )


def _negative_prompt() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon("type", size=17, color=rx.color("red", 9)),
            rx.text("Negative Prompt", size="3"),
            rx.tooltip(
                rx.icon(
                    "info",
                    size=15,
                    color=rx.color("gray", 10),
                ),
                content="Things you want to avoid in the image",
            ),
            rx.spacer(),
            rx.hstack(
                rx.cond(
                    OptionsState.negative_prompt,
                    rx.icon(
                        "eraser",
                        size=20,
                        color=rx.color("gray", 10),
                        cursor="pointer",
                        _hover={"opacity": "0.8"},
                        on_click=OptionsState.setvar("negative_prompt", ""),
                    ),
                ),
                spacing="4",
                align="center",
            ),
            spacing="2",
            align="center",
            width="100%",
        ),
        rx.text_area(
            placeholder="What do you want to avoid?",
            width="100%",
            size="3",
            value=OptionsState.negative_prompt,
            on_change=OptionsState.set_negative_prompt,
        ),
        width="100%",
    )


def _seed_input() -> rx.Component:
    return (
        rx.vstack(
            rx.hstack(
                rx.icon("sprout", size=17, color=rx.color("grass", 10)),
                rx.text("Seed", size="3"),
                rx.spacer(),
                rx.hstack(
                    rx.cond(
                        OptionsState.seed > 0,
                        rx.icon(
                            "eraser",
                            size=20,
                            color=rx.color("gray", 10),
                            cursor="pointer",
                            _hover={"opacity": "0.8"},
                            on_click=OptionsState.setvar("seed", 0),
                        ),
                    ),
                    spacing="4",
                    align="center",
                ),
                spacing="2",
                align="center",
                width="100%",
            ),
            rx.tooltip(
                rx.box(
                    rx.input(
                        type="number",
                        value=OptionsState.seed,
                        on_change=OptionsState.set_seed,
                        placeholder="0 (Auto)",
                        max_length=5,
                        width="100%",
                    ),
                    width="100%",
                ),
                content="A number that determines the randomness of the image. Use the same seed to get the same result every time. 0 = Auto",
                side="right",
            ),
            spacing="2",
        ),
    )


def _scheduler_input() -> rx.Component:
    return (
        rx.vstack(
            rx.hstack(
                rx.icon("align-left", size=17, color=rx.color("iris", 10)),
                rx.text("Scheduler", size="3"),
                align="center",
                width="100%",
                spacing="2",
            ),
            rx.tooltip(
                rx.box(
                    rx.select(
                        [
                            "DDIM",
                            "DPMSolverMultistep",
                            "HeunDiscrete",
                            "KarrasDPM",
                            "K_EULER_ANCESTRAL",
                            "K_EULER",
                            "PNDM",
                            "DPM++2MSDE",
                        ],
                        width="100%",
                        value=OptionsState.scheduler,
                        on_change=OptionsState.set_scheduler,
                    ),
                    width="100%",
                ),
                content="Schedulers guide the process of removing noise from the image",
                side="right",
            ),
            spacing="2",
        ),
    )


def _guidance_scale_input() -> rx.Component:
    return (
        rx.vstack(
            rx.hstack(
                rx.icon("scale", size=17, color=rx.color("cyan", 10)),
                rx.text("Guidance Scale", size="3"),
                rx.spacer(),
                rx.text(f"{OptionsState.guidance_scale}", size="3"),
                align="center",
                width="100%",
                spacing="2",
            ),
            rx.tooltip(
                rx.box(
                    rx.slider(
                        min=0,
                        max=50,
                        step=0.01,
                        size="1",
                        default_value=OptionsState.guidance_scale,
                        on_change=OptionsState.set_guidance_scale,
                    ),
                    width="100%",
                ),
                content="Controls the strength of the promptguidance. Recommended 0. (minimum: 0, maximum: 50)",
                side="right",
            ),
            spacing="2",
        ),
    )


def _steps_input() -> rx.Component:
    return (
        rx.vstack(
            rx.hstack(
                rx.icon("footprints", size=17, color=rx.color("purple", 10)),
                rx.text("Steps", size="3"),
                rx.spacer(),
                rx.text(f"{OptionsState.steps}", size="3"),
                align="center",
                width="100%",
                spacing="2",
            ),
            rx.tooltip(
                rx.box(
                    rx.slider(
                        min=1,
                        max=10,
                        step=1,
                        size="1",
                        default_value=OptionsState.steps,
                        on_change=OptionsState.set_steps,
                    ),
                    width="100%",
                ),
                content="Number of denoising steps. 4 for best results. (minimum: 1, maximum: 10)",
                side="right",
            ),
            spacing="2",
        ),
    )


def _advanced_options_grid() -> rx.Component:
    return rx.grid(
        _seed_input(),
        _steps_input(),
        _scheduler_input(),
        _guidance_scale_input(),
        width="100%",
        columns="2",
        rows="2",
        spacing_x="5",
        spacing_y="5",
        justify="between",
        align="center",
    )


def advanced_options() -> rx.Component:
    return rx.vstack(
        rx.cond(
            OptionsState.advanced_options_open,
            rx.hstack(
                rx.icon(
                    "eye",
                    size=17,
                    color=rx.color("jade", 10),
                ),
                rx.text("Advanced Options", size="3"),
                align="center",
                spacing="2",
                width="100%",
                cursor="pointer",
                _hover={"opacity": "0.8"},
                on_click=OptionsState.setvar("advanced_options_open", False),
            ),
            rx.hstack(
                rx.icon(
                    "eye-off",
                    size=17,
                    color=rx.color("jade", 10),
                ),
                rx.text("Advanced Options", size="3"),
                align="center",
                spacing="2",
                width="100%",
                cursor="pointer",
                _hover={"opacity": "0.8"},
                on_click=OptionsState.setvar("advanced_options_open", True),
            ),
        ),
        rx.cond(
            OptionsState.advanced_options_open,
            rx.vstack(_negative_prompt(), _advanced_options_grid(), width="100%"),
        ),
        width="100%",
    )


def generate_button() -> rx.Component:
    return rx.box(
        rx.cond(
            ~GeneratorState.is_generating,
            rx.button(
                rx.icon("sparkles", size=18),
                "Generate",
                size="3",
                cursor="pointer",
                width="100%",
                on_click=GeneratorState.generate_image,
            ),
            rx.button(
                rx.spinner(size="3"),
                "Cancel",
                size="3",
                width="100%",
                color_scheme="tomato",
                cursor="pointer",
                on_click=GeneratorState.cancel_generation,
            ),
        ),
        position="sticky",
        bottom="0",
        padding="1em",
        bg=rx.color("gray", 2),
        border_top=styles.border,
        width="100%",
    )
