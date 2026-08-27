from styles.colors import (
    TEXT,
    SECONDARY_TEXT,
)

from styles.fonts import (
    TITLE_SIZE,
    SUBTITLE_SIZE,
    FONT_FAMILY,
)


HEADER_STYLE = f"""

#pageHeader {{

    background-color: transparent;

}}


#headerTitle {{

    color: {TEXT};

    font-size: {TITLE_SIZE}px;

    font-weight: 700;

    font-family: "{FONT_FAMILY}";

}}


#headerSubtitle {{

    color: {SECONDARY_TEXT};

    font-size: {SUBTITLE_SIZE}px;

    font-family: "{FONT_FAMILY}";

}}


#basePage {{

    background-color: #0B1220;

}}


#pageContent {{

    background-color: transparent;

}}

"""