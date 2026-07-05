from .data_loader import load_data

from .analytics import (
    get_kpi,
    get_statistics,
    get_top_provinces,
    get_bottom_provinces,
    get_ranking,
    get_vehicle_composition,
    get_vehicle_percentage,
    prepare_map_data,
    get_map_kpi,
    get_growth,
    get_yearly_trend,
    generate_insight,
)

from .charts import *

from .sidebar import sidebar_filter

from .helper import (
    load_css,
    section_title,
    card,
    hero,
)

from .formatter import *