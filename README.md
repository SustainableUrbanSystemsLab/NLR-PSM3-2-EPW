# NLR-PSM3-2-EPW — Convert NREL PSM3 / NSRDB Solar Data to EnergyPlus EPW Weather Files

[![Build-Test](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/actions/workflows/build-test.yml/badge.svg?branch=main)](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/actions/workflows/build-test.yml)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nrel-psm3-2-epw.streamlit.app/)
[![Latest Release](https://img.shields.io/github/v/release/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW?label=release)](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**NLR-PSM3-2-EPW** is a free, open-source Python tool and Streamlit web app that converts
**NREL Physical Solar Model (PSM v3.2.2 / v4.0.0, NSRDB)** solar and meteorological data into
**EnergyPlus Weather (EPW)** files for building energy simulation. Pick any location by
latitude / longitude and download a ready-to-use `.epw` for a specific year or a
**Typical Meteorological Year (TMY)**.

👉 **Try the live app:** <https://nrel-psm3-2-epw.streamlit.app/>

## What it does

Downloads solar irradiance (**GHI, DNI, DHI**), dry-bulb temperature, dew point, relative
humidity, atmospheric pressure, wind speed/direction, cloud cover, surface albedo and
precipitable water from the **NSRDB** API, then writes a standards-compliant **EPW** weather
file compatible with **EnergyPlus, OpenStudio, Ladybug / Honeybee, DesignBuilder, IES-VE**
and other building-performance simulation tools.

## Why

Getting hourly weather data into an EnergyPlus-ready EPW file usually means manual API calls
and column wrangling. This tool automates the full **NSRDB → EPW** pipeline — click a point
on a map, choose a year or TMY, and download the weather file.

## Features

- **PSM3 / NSRDB → EPW conversion** — turns NREL solar climate data into EnergyPlus Weather format.
- **Interactive map** — pick a location by clicking, or enter latitude / longitude manually.
- **TMY and single-year datasets** — download `tmy`, `tgy`, `tdy`, or a specific historical year (≥ 1998).
- **Resilient downloads** — automatically falls back to core attributes when a dataset is
  sparse at a location, so remote points still produce a valid EPW.
- **Secure** — API keys are managed via Streamlit secrets and verified with a hash check.
- **Modern stack** — `uv` for dependency management, `ruff` for linting, 100% unit-test coverage.

## What is an EPW file?

An **EnergyPlus Weather (EPW)** file is the standard hourly weather format consumed by
EnergyPlus and most building energy simulation engines. It contains a full year (8760 hours)
of solar, temperature, humidity, wind and sky-cover data for a single location, and is the
starting point for energy modeling, daylighting and thermal-comfort analysis.

## Keywords

`EPW` · `EnergyPlus Weather file` · `PSM3` · `PSM v4` · `NSRDB` · `NREL` · `TMY` ·
`typical meteorological year` · `solar radiation data` · `GHI / DNI / DHI` ·
`building energy simulation` · `weather data converter` · `climate data`

## Project Structure

- `app/`: Streamlit application.
    - `streamlit_app.py`: Main entry point.
    - `.streamlit/secrets.toml`: (Not committed) Stores your API key.
- `nlr_psm3_2_epw/`: Core transformation logic (NSRDB download + EPW writer).
- `tests/`: Unit and integration tests (100% coverage).

## How to Run Locally

1. **Install dependencies with uv**:
    ```bash
    uv sync --extra dev
    ```

2. **Configure your API key**:
    - Create `app/.streamlit/secrets.toml`:
        ```toml
        APIKEY = "YOUR_NLR_API_KEY"
        ```
    - Request or manage your API key at <https://developer.nlr.gov/signup>
    - API documentation is available at <https://developer.nlr.gov>
    - *Note: the app verifies the default API key integrity.*

3. **Run the app**:
    ```bash
    uv run streamlit run app/streamlit_app.py
    ```
    *(Windows users can use `run_streamlit.bat`.)*

4. **Run tests**:
    ```bash
    uv run pytest
    ```

5. **Lint & format**:
    ```bash
    uv run ruff check --fix .
    uv run ruff format .
    ```

## Demo

Live Streamlit app: <https://nrel-psm3-2-epw.streamlit.app/>

## License

Released under the [MIT License](LICENSE).
