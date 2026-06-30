import os
import re
from datetime import datetime
from importlib.metadata import version
from typing import Optional

import requests
import streamlit as st
import folium
from streamlit_folium import st_folium

__version__ = version("nlr-psm3-2-epw")

from nlr_psm3_2_epw.assets import download_epw
from nlr_psm3_2_epw.constants import DEVELOPER_DOCS_URL, DEVELOPER_SIGNUP_URL
from nlr_psm3_2_epw.validation import (
    API_KEY_LENGTH,
    is_api_key_valid,
    is_api_key_verified,
    normalize_api_key,
)

# --- CONSTANTS ---
ATTRIBUTES = (
    "air_temperature,clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_type,dew_point,dhi,dni,fill_flag,"
    "ghi,relative_humidity,solar_zenith_angle,surface_albedo,surface_pressure,total_precipitable_water,"
    "wind_direction,wind_speed"
)
INTERVAL = "60"
UTC = "false"
YOUR_NAME = "John+Doe"
REASON_FOR_USE = "beta+testing"
YOUR_AFFILIATION = "aaa"
YOUR_EMAIL = "Joe@Doe.edu"
MAILING_LIST = "false"
LEAP_YEAR = "false"
MIN_YEAR = 1998
VALID_API_KEY_HASH = "1c2c12cf359f7aba48e0aaf39ac031d98fee2418f3c4e482ec1044904032fefe"


def _load_api_key() -> Optional[str]:
    """
    Attempts to load the API key from various sources in order of precedence:
    1. streamlit secrets
    2. environment variable
    3. local 'api_key' file
    4. local '.env' file
    """
    cwd = os.getcwd()

    # 1. Secrets
    # Check if secrets file exists to avoid Streamlit rendering a missing secrets warning in the UI
    secrets_paths = [
        os.path.join(cwd, ".streamlit", "secrets.toml"),
        os.path.join(os.path.expanduser("~"), ".streamlit", "secrets.toml"),
    ]
    if any(os.path.isfile(p) for p in secrets_paths):
        try:
            if "APIKEY" in st.secrets:
                return st.secrets.get("APIKEY")
        except Exception:
            pass

    # 2. Environment Variable
    api_key = os.environ.get("APIKEY")
    if api_key:
        return api_key

    # 3. api_key file
    api_key_path = os.path.join(cwd, "api_key")
    if os.path.isfile(api_key_path):
        with open(api_key_path, "r") as f:
            return f.readline().strip()

    # 4. .env file
    env_path = os.path.join(cwd, ".env")
    if os.path.isfile(env_path):
        with open(env_path, "r") as f:
            for line in f:
                stripped = line.strip()
                if not stripped or stripped.startswith("#") or "=" not in stripped:
                    continue
                key, value = stripped.split("=", 1)
                if key.strip() == "APIKEY" and value.strip():
                    return value.strip()
    return None


@st.cache_data(show_spinner="📍 Reverse geocoding...")
def get_location_name(lat: float, lon: float) -> str:
    """
    Reverse geocodes the given latitude and longitude using OpenStreetMap Nominatim API.
    Returns a meaningful location name or 'Unknown Location' if it fails.
    """
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
    headers = {"User-Agent": f"NLR-PSM3-2-EPW-App/{__version__}"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()

        if "address" in data:
            addr = data["address"]
            city = (
                addr.get("city") or addr.get("town") or addr.get("village") or addr.get("hamlet") or addr.get("county")
            )
            state = addr.get("state")
            country = addr.get("country")

            parts = [p for p in (city, state, country) if p]
            if parts:
                return ", ".join(parts)

        if "display_name" in data:
            # Fallback to the first few parts of the display name
            parts = data["display_name"].split(", ")
            if len(parts) > 3:
                return ", ".join(parts[:3])
            return data["display_name"]

    except Exception as e:
        print(f"Error in reverse geocoding: {e}")

    return "Unknown Location"


@st.cache_resource
def get_map():
    """
    Bolt Optimization:
    Cache the folium map object to prevent re-instantiating it on every Streamlit rerun.
    This saves CPU time and prevents the frontend from fully destroying and
    re-rendering the map iframe during unrelated app interactions (like typing in text inputs).
    """
    m = folium.Map(location=[33.770, -84.3824], zoom_start=4)
    m.add_child(folium.LatLngPopup())
    return m


def main():
    st.set_page_config(page_title="NLR to EPW", page_icon="☀️")
    st.title("NLR-PSM3-2-EPW")
    st.caption(f"**Version {__version__}**")
    st.markdown("This script converts climate data from NLR to the EnergyPlus Weather (EPW) format.")

    # API Key Handling
    default_api_key = _load_api_key()

    if not default_api_key:
        st.info(
            "👋 **First time here?** You'll need an API key to download data. "
            f"[Request an NLR API key]({DEVELOPER_SIGNUP_URL}) for free. "
            f"[API docs]({DEVELOPER_DOCS_URL}) are also available.",
            icon="💡",
        )

    api_key = ""
    api_key_source = "none"

    # Verify the default key once, up front: it drives both the auto-expand
    # behaviour below and the request-button validity further down.
    default_key_verified = is_api_key_verified(default_api_key, VALID_API_KEY_HASH)
    is_default_key_unverified = bool(default_api_key) and not default_key_verified

    with st.expander("🔑 API Key Configuration", expanded=not bool(default_api_key) or is_default_key_unverified):
        label = "Provide your own NLR API key (optional)" if default_api_key else "Provide your NLR API key (required)"
        help_text = (
            f"Overrides the default API key if provided. You can [request a free NLR API key]({DEVELOPER_SIGNUP_URL}) if needed."
            if default_api_key
            else f"An NLR API key is strictly required to request data. You can [request a free NLR API key]({DEVELOPER_SIGNUP_URL})."
        )
        api_key_override = st.text_input(
            label,
            value="",
            type="password",
            max_chars=40,
            placeholder="Enter your 40-character API key",
        )
        st.caption(help_text)

        if api_key_override:
            api_key = normalize_api_key(api_key_override)
            api_key_source = "user"
            if len(api_key) == API_KEY_LENGTH:
                st.success("User API key loaded.", icon="✅")
        elif default_api_key:
            api_key = normalize_api_key(default_api_key)
            api_key_source = "default"

            if default_key_verified:
                st.success("Default API key loaded (Verified).", icon="✅")
            else:
                st.warning(
                    "Default API key loaded (Unverified). Please verify the key in your .streamlit/secrets.toml file.",
                    icon="⚠️",
                )

    st.header("Location & Time Details", divider="gray")

    # Show a map to pick lat/lon
    st.info("**Tip:** Select a location on the map, or enter coordinates manually in the fields provided.", icon="🗺️")
    m = get_map()

    # Initialize session state for lat/lon if they don't exist
    if "input_lat" not in st.session_state:
        st.session_state.input_lat = 33.770
    if "input_lon" not in st.session_state:
        st.session_state.input_lon = -84.3824

    # Default location string
    default_location = "Atlanta"

    # Bolt Optimization:
    # Use returned_objects=["last_clicked"] to prevent Streamlit from completely rerunning
    # the entire Python backend and frontend UI every time the user pans or zooms the map.
    map_data = st_folium(
        m,
        center=[st.session_state.input_lat, st.session_state.input_lon],
        height=400,
        use_container_width=True,
        returned_objects=["last_clicked"],
    )

    # Update lat/lon from map click if available
    if map_data and map_data.get("last_clicked"):
        click_lat = map_data["last_clicked"]["lat"]
        click_lon = map_data["last_clicked"]["lng"]

        click_id = f"{click_lat}-{click_lon}"
        prev_click_id = st.session_state.get("last_map_click")

        # If this is a new map click, update session state and rerun to sync inputs
        if prev_click_id != click_id:
            st.session_state["last_map_click"] = click_id
            st.session_state.input_lat = float(click_lat)
            st.session_state.input_lon = float(click_lon)

            # Reverse geocode the location
            loc_name = get_location_name(click_lat, click_lon)
            if loc_name != "Unknown Location":
                st.toast(f"Location updated to **{loc_name}**", icon="📍")
            else:
                st.toast(f"Location updated to coordinates: {click_lat:.4f}, {click_lon:.4f}", icon="📍")

            st.rerun()

    lat = st.session_state.input_lat
    lon = st.session_state.input_lon

    # Check if current lat/lon differs from default before reverse geocoding to pre-fill location input
    if lat != 33.770 or lon != -84.3824:
        loc_name = get_location_name(lat, lon)
        default_location = loc_name if loc_name != "Unknown Location" else ""

    col1, col2 = st.columns(2)
    with col1:
        st.number_input(
            "Latitude (required)",
            min_value=-90.0,
            max_value=90.0,
            key="input_lat",
            format="%.4f",
            step=0.0001,
            placeholder="33.7700",
        )
        st.caption("Latitude of the location in decimal degrees (e.g., 33.770)")
    with col2:
        st.number_input(
            "Longitude (required)",
            min_value=-180.0,
            max_value=180.0,
            key="input_lon",
            format="%.4f",
            step=0.0001,
            placeholder="-84.3824",
        )
        st.caption("Longitude of the location in decimal degrees (e.g., -84.3824)")

    col3, col4 = st.columns(2)
    with col3:
        location = st.text_input(
            "Location Name (required)",
            value=default_location,
            placeholder="e.g., Atlanta",
            max_chars=60,
        )
        st.caption("A descriptive name for the location, used to generate the output filename.")
        st.caption("💡 *Auto-updates when you select a new location on the map.*")
        location_is_valid = bool(str(location).strip())
    with col4:
        year = st.text_input(
            "Year (required)",
            value="tmy",
            placeholder="e.g., 2012, tmy, tmy-2024",
            max_chars=15,
        )
        st.caption("A specific year (>=1998) or a TMY identifier like 'tmy' or 'tmy-2024'")
        st.caption("💡 *TMY (Typical Meteorological Year) datasets represent long-term average climate conditions.*")

    current_year = datetime.now().year
    year_str = str(year).strip()
    year_is_valid = True
    year_warning = ""

    # Dynamic filename preview
    safe_loc = re.sub(r"[^a-zA-Z0-9]", "_", str(location).strip()) if str(location).strip() else "Unnamed"
    preview_name = f"{safe_loc}_{lat:.2f}_{lon:.2f}_{year_str or 'YYYY'}_{current_year}.epw"
    st.caption(f"📝 *Output filename:* `{preview_name}`")

    # Basic Year Validation
    if not year_str:
        year_is_valid = False
        year_warning = "A year or TMY identifier is required."
    elif year_str.isdigit():
        year_int = int(year_str)
        if year_int >= current_year - 1:
            year_is_valid = False
            year_warning = (
                f"NLR does not provide data for the year {year}. "
                f"Data is typically only available up to {current_year - 2}. Please enter an earlier year."
            )
        elif year_int < MIN_YEAR:
            year_is_valid = False
            year_warning = f"NLR does not provide data for the year {year}. The earliest year data is available for is {MIN_YEAR}. Please enter a more recent year."
    else:
        if not year_str.lower().startswith(("tmy", "tgy", "tdy")):
            year_is_valid = False
            year_warning = "Year must be a numeric year (>=1998) or a TMY name like tmy or tmy-2024."

    # A verified default key is usable regardless of length; any other key must
    # be exactly API_KEY_LENGTH characters (whitespace already trimmed on load).
    api_key_is_valid = is_api_key_valid(
        api_key, is_verified=(api_key_source == "default" and default_key_verified)
    )

    # Full-width validation warnings below inputs
    if not location_is_valid:
        st.warning("A location name is required to generate the file.", icon="⚠️")

    if not year_is_valid:
        st.warning(year_warning, icon="⚠️")

    if not api_key:
        st.warning("Please provide an API key in the 'API Key Configuration' section to request data.", icon="🔑")
    elif not api_key_is_valid:
        st.warning("The provided API key must be exactly 40 characters long to request data.", icon="⚠️")

    if st.button(
        "Request from NLR",
        type="primary",
        disabled=not api_key_is_valid or not year_is_valid or not location_is_valid,
        icon=":material/cloud_download:",
        use_container_width=True,
    ):
        with st.spinner("Requesting data from NLR..."):
            try:
                file_name = download_epw(
                    lon,
                    lat,
                    year,
                    location,
                    ATTRIBUTES,
                    INTERVAL,
                    UTC,
                    YOUR_NAME,
                    api_key,
                    REASON_FOR_USE,
                    YOUR_AFFILIATION,
                    YOUR_EMAIL,
                    MAILING_LIST,
                    LEAP_YEAR,
                )
            except Exception as exc:
                st.error("Request failed: The data could not be retrieved from NLR.", icon="❌")
                with st.expander("🛠️ View technical details"):
                    st.code(str(exc), language="text")
                if api_key_source == "default":
                    st.info(
                        "If this failure is related to the default API key, enter your own key in the API Key Configuration section and retry.",
                        icon="💡",
                    )
                elif api_key_source == "user":
                    st.info(
                        "Please verify that your custom API key is correct and active. You can check your account at the NLR Developer portal.",
                        icon="💡",
                    )
                st.stop()

        if os.path.exists(file_name):
            file_size_mb = os.path.getsize(file_name) / (1024 * 1024)
            with open(file_name, "rb") as f:
                s = f.read()

            with st.container(border=True):
                st.success(
                    f"Data successfully processed! Your EPW file (**{os.path.basename(file_name)}**) is ready for download ({file_size_mb:.2f} MB).",
                    icon="✅",
                )

                with st.expander("👀 Preview File Contents (First 10 Lines)"):
                    # Bolt Optimization:
                    # By splitting on the raw byte string `s` with maxsplit=10 *before* decoding,
                    # we avoid completely decoding the entire 2.5MB+ file into memory and allocating
                    # an 8760+ element list just to extract the first 10 lines.
                    preview_lines = b"\n".join(s.split(b"\n", 10)[:10]).decode("utf-8", errors="replace")
                    st.code(preview_lines, language="csv")

                st.download_button(
                    label="Download EPW",
                    data=s,
                    file_name=file_name,
                    mime="text/plain",
                    type="primary",
                    icon=":material/download:",
                    use_container_width=True,
                )

            st.markdown("---")
            st.info(
                "**Visualize your EPW file**\n\n"
                "Once downloaded, you can visualize your EPW file using these free online tools:\n\n"
                "- **[EPWvis](https://mdahlhausen.github.io/epwvis/)**: View summary charts and graphs for temperature, radiation, and wind.\n"
                "- **[CBE Clima Tool](https://clima.cbe.berkeley.edu/)**: Advanced interactive climate analysis and psychrometric charts.",
                icon="📊",
            )
        else:
            st.error(
                "Data unavailable for this location and year. Please verify coverage or try a different year.",
                icon="❌",
            )
        st.stop()


if __name__ == "__main__":
    main()
