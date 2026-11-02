# NLR-PSM-2-EPW — Convert NLR PSM / NSRDB Solar Data to EnergyPlus EPW Weather Files

[![Build-Test](https://github.com/SustainableUrbanSystemsLab/NLR-PSM-2-EPW/actions/workflows/build-test.yml/badge.svg?branch=main)](https://github.com/SustainableUrbanSystemsLab/NLR-PSM-2-EPW/actions/workflows/build-test.yml)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nlr-psm-2-epw.streamlit.app/)
[![Latest Release](https://img.shields.io/github/v/release/SustainableUrbanSystemsLab/NLR-PSM-2-EPW?label=release)](https://github.com/SustainableUrbanSystemsLab/NLR-PSM-2-EPW/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Free, open-source Python tool and Streamlit app that turns **NLR Physical Solar Model (PSM, NSRDB)**
data into **EnergyPlus Weather (EPW)** files. Click a point on the map, pick a year or a
**Typical Meteorological Year (TMY)**, and download a ready-to-use `.epw`.

👉 **Live app:** <https://nlr-psm-2-epw.streamlit.app/>

> **Coverage:** the GOES dataset covers the Americas only. Points elsewhere return "No data available".

<details>
<summary><b>Features</b></summary>

- **Interactive map** — click a location or enter latitude / longitude.
- **TMY and single-year data** — `tmy`, `tgy`, `tdy`, or a specific year (1998 to last full year).
- **Resilient downloads** — falls back to core attributes when a dataset is sparse at a location.
- **Secure** — API key via Streamlit secrets, verified with a hash check.
- **Modern stack** — `uv`, `ruff`, 100% unit-test coverage.

</details>

<details>
<summary><b>What is an EPW file?</b></summary>

The standard hourly weather format used by EnergyPlus, OpenStudio, Ladybug / Honeybee,
DesignBuilder, IES-VE and most building energy simulation tools. One file holds a full year
(8760 hours) of solar, temperature, humidity, wind and sky-cover data for one location.

</details>

<details>
<summary><b>Run locally</b></summary>

```bash
uv sync --extra dev                                # install
uv run streamlit run app/streamlit_app.py          # run (Windows: run_streamlit.bat)
uv run pytest                                      # test
uv run ruff check --fix . && uv run ruff format .  # lint & format
```

API key: create `app/.streamlit/secrets.toml` with

```toml
APIKEY = "YOUR_NLR_API_KEY"
```

Get a key at <https://developer.nlr.gov/signup>; docs at <https://developer.nlr.gov>.

</details>

<details>
<summary><b>Project structure</b></summary>

- `app/streamlit_app.py` — Streamlit entry point.
- `nlr_psm_2_epw/` — NSRDB download + EPW writer.
- `tests/` — unit and integration tests (100% coverage).

</details>

<details>
<summary><b>Keywords</b></summary>

`EPW` · `EnergyPlus Weather file` · `PSM` · `NSRDB` · `NLR` · `TMY` · `typical meteorological year` ·
`solar radiation data` · `GHI / DNI / DHI` · `building energy simulation` · `weather data converter` · `climate data`

</details>

Released under the [MIT License](LICENSE).
