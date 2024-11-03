import reflex as rx
from .. import styles
from ..components.options_ui import (
    sidebar_header,
    endpoint,
    generate_button,
)

def nodes_actions():
    return rx.box(
        rx.grid(
            rx.icon("sprout", size=17, color=rx.color("grass", 10)),
            rx.icon("sprout", size=17, color=rx.color("grass", 10)),
            rx.icon("sprout", size=17, color=rx.color("grass", 10)),
            rx.icon("sprout", size=17, color=rx.color("grass", 10)),
            columns="2",
            rows="2",
            justify="between",
            align="center",
        )
    )

def sidebar():
    return rx.box(
        rx.vstack(
            sidebar_header(),
            rx.flex(
                rx.vstack(
                    endpoint(),
                    nodes_actions(),
                    # advanced_options(),
                    width="100%",
                    overflow_y="auto",
                    align="start",
                    padding="1em",
                    spacing="6",
                ),
                overflow_y="auto",
                flex="1",
                height="100%",
                width="100%",
            ),
            width="100%",
            height="100%",
            spacing="0",
        ),
        generate_button(),
        display=["none", "none", "none", "block"],
        width=styles.sidebar_width,
        height="100vh",
        position="sticky",
        top="0px",
        left="0px",
        bg=styles.sidebar_bg,
        border_right=styles.border,
    )
