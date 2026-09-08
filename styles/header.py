from styles.fonts import (
    TITLE_SIZE,
    SUBTITLE_SIZE,
    FONT_FAMILY,
)


def get_header_style(theme):
    return f"""

#pageHeader {{

    background-color: transparent;

}}


#headerTitle {{

    color: {theme["text"]};

    font-size: {TITLE_SIZE}px;

    font-weight: 700;

    font-family: "{FONT_FAMILY}";

}}


#headerSubtitle {{

    color: {theme["secondary_text"]};

    font-size: {SUBTITLE_SIZE}px;

    font-family: "{FONT_FAMILY}";

}}


#basePage {{

    background-color: {theme["background"]};

}}


#pageContent {{

    background-color: transparent;

}}

"""