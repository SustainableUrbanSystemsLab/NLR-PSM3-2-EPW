# CHANGELOG


## v0.5.4 (2026-07-01)

### Other

- Merge pull request #96 from SustainableUrbanSystemsLab/palette-validation-ux-9508518222143056358
  ([`e9327ce`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/e9327ce840ee3c20dbbc02a8cf2f8ae72eebc217))

🎨 Palette: [validation] distinguish empty state from active invalid input errors

### 🎨

- 🎨 Palette: [validation] distinguish empty state from active invalid input errors
  ([`11c42f1`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/11c42f19a35a33910ba12a29fcefecac066be8c4))

- Upgraded actively invalid input validation messages from st.warning to st.error. - Retained
  st.warning for preliminary empty states.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>


## v0.5.3 (2026-07-01)

### Other

- Merge pull request #95 from SustainableUrbanSystemsLab/chore/seo
  ([`37c1a28`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/37c1a28d6108947c906b216bf8da8c31d3a3ee63))

📝 docs: SEO for README + app meta tags

### 📝

- 📝 docs: add SEO to README and inject page meta tags in the app
  ([`164e7d7`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/164e7d79d3fc6cb5f89d8a7ddcdc661f3e7e9d36))

README is rewritten for discoverability: keyword-rich H1/intro (EPW, EnergyPlus Weather, PSM3/PSM
  v4, NSRDB, NREL, TMY, GHI/DNI/DHI, building energy simulation), a "What is an EPW file?" section,
  a keywords block, and a dynamic release badge (the old one was pinned to a stale v4.0.0).

The Streamlit app now sets a keyword-rich page title and injects meta tags — description, keywords,
  Open Graph, Twitter card and a canonical link — into the host page <head> via a hidden component,
  so JS-capable crawlers can index the app. Verified at runtime (title/description/
  og:*/twitter/canonical all present).

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


## v0.5.2 (2026-07-01)

### Other

- Merge pull request #94 from SustainableUrbanSystemsLab/fix/tmy-attribute-fallback
  ([`9aba2bb`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/9aba2bb98ce12f022bbb9d162eb938380e174221))

🐛 fix: fall back to core attributes when NLR TMY rejects the full set

### 🐛

- 🐛 fix: fall back to core attributes when NLR TMY rejects the full set
  ([`5542b20`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/5542b20dad4d232ccb787128c6ea0839af9e219f))

The app requests 17 attributes for a TMY download. NLR returns 400 "Data processing failure" when a
  requested attribute has no data at the chosen point — e.g. cloud_type / surface_albedo /
  total_precipitable_water are unavailable at some land locations. NYC has them (so CI passed); the
  Montana point in the reported failure does not (so the app failed).

download_epw now: - requests the full attribute set first, then retries with only the core
  solar+meteorological attributes that exist everywhere, and - fills the dropped EPW columns
  (Total/Opaque Sky Cover, Precipitable Water, Albedo) with the standard EPW "missing" sentinels (99
  / 999).

Tests: - unit: mocked retry — first request 400, core-only retry succeeds, dropped columns written
  as sentinels (100% coverage kept). - integration: test_download parametrized over NYC (complete)
  and the Montana point that used to 400. This runs in CI with the real APIKEY secret, so this class
  of location-dependent failure is now caught. Also fixed a copy-paste bug (wind-direction bound
  checked Relative Humidity) and relaxed the sky-cover assertion to accept the sentinel.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


## v0.5.1 (2026-07-01)

### Other

- Add symmetrical inline guidance to Location field
  ([`8a6fa5a`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/8a6fa5aa47c72c2c83e4b4af3fe435869c17fb5a))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Bump gitpython from 3.1.46 to 3.1.47
  ([`7a3ddaa`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/7a3ddaa2b8f51583e7f324d4614dac7d26fddef9))

Bumps [gitpython](https://github.com/gitpython-developers/GitPython) from 3.1.46 to 3.1.47. -
  [Release notes](https://github.com/gitpython-developers/GitPython/releases) -
  [Changelog](https://github.com/gitpython-developers/GitPython/blob/main/CHANGES) -
  [Commits](https://github.com/gitpython-developers/GitPython/compare/3.1.46...3.1.47)

--- updated-dependencies: - dependency-name: gitpython dependency-version: 3.1.47

dependency-type: indirect ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump gitpython from 3.1.47 to 3.1.50
  ([`2540c99`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/2540c994bbe7e60b2cc064b23f0778df47e98dfd))

Bumps [gitpython](https://github.com/gitpython-developers/GitPython) from 3.1.47 to 3.1.50. -
  [Release notes](https://github.com/gitpython-developers/GitPython/releases) -
  [Changelog](https://github.com/gitpython-developers/GitPython/blob/main/CHANGES) -
  [Commits](https://github.com/gitpython-developers/GitPython/compare/3.1.47...3.1.50)

--- updated-dependencies: - dependency-name: gitpython dependency-version: 3.1.50

dependency-type: indirect ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump idna from 3.11 to 3.15
  ([`a72e46d`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/a72e46ddf8f916526976b5a57414716c26d1f16e))

Bumps [idna](https://github.com/kjd/idna) from 3.11 to 3.15. - [Release
  notes](https://github.com/kjd/idna/releases) -
  [Changelog](https://github.com/kjd/idna/blob/master/HISTORY.md) -
  [Commits](https://github.com/kjd/idna/compare/v3.11...v3.15)

--- updated-dependencies: - dependency-name: idna dependency-version: '3.15'

dependency-type: indirect ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump pillow from 11.3.0 to 12.2.0
  ([`5af9e55`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/5af9e5517ea325e1c7f34f7b2efba148776ba99a))

Bumps [pillow](https://github.com/python-pillow/Pillow) from 11.3.0 to 12.2.0. - [Release
  notes](https://github.com/python-pillow/Pillow/releases) -
  [Changelog](https://github.com/python-pillow/Pillow/blob/main/CHANGES.rst) -
  [Commits](https://github.com/python-pillow/Pillow/compare/11.3.0...12.2.0)

--- updated-dependencies: - dependency-name: pillow dependency-version: 12.2.0

dependency-type: indirect ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump pyarrow from 23.0.0 to 23.0.1
  ([`963dace`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/963dace6c6b6625851019d0c8988bf1a1ee032ee))

Bumps [pyarrow](https://github.com/apache/arrow) from 23.0.0 to 23.0.1. - [Release
  notes](https://github.com/apache/arrow/releases) -
  [Commits](https://github.com/apache/arrow/compare/apache-arrow-23.0.0...apache-arrow-23.0.1)

--- updated-dependencies: - dependency-name: pyarrow dependency-version: 23.0.1

dependency-type: indirect ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump pygments from 2.19.2 to 2.20.0
  ([`fc41308`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/fc41308b31a6fd2a92bb9cea213af278a4ae1e88))

Bumps [pygments](https://github.com/pygments/pygments) from 2.19.2 to 2.20.0. - [Release
  notes](https://github.com/pygments/pygments/releases) -
  [Changelog](https://github.com/pygments/pygments/blob/master/CHANGES) -
  [Commits](https://github.com/pygments/pygments/compare/2.19.2...2.20.0)

--- updated-dependencies: - dependency-name: pygments dependency-version: 2.20.0

dependency-type: indirect ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump pytest from 9.0.2 to 9.0.3
  ([`30d0a84`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/30d0a848a78184375c10870ef488d116659bd6fe))

Bumps [pytest](https://github.com/pytest-dev/pytest) from 9.0.2 to 9.0.3. - [Release
  notes](https://github.com/pytest-dev/pytest/releases) -
  [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pytest-dev/pytest/compare/9.0.2...9.0.3)

--- updated-dependencies: - dependency-name: pytest dependency-version: 9.0.3

dependency-type: direct:development ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump requests from 2.32.4 to 2.33.0
  ([`669487b`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/669487b1b2c913747fd51a3a7300ea2899b342b5))

Bumps [requests](https://github.com/psf/requests) from 2.32.4 to 2.33.0. - [Release
  notes](https://github.com/psf/requests/releases) -
  [Changelog](https://github.com/psf/requests/blob/main/HISTORY.md) -
  [Commits](https://github.com/psf/requests/compare/v2.32.4...v2.33.0)

--- updated-dependencies: - dependency-name: requests dependency-version: 2.33.0

dependency-type: direct:production ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump tornado from 6.5.4 to 6.5.5
  ([`27e8bac`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/27e8bac39322b0ce109baa84326bc465b28b9a88))

Bumps [tornado](https://github.com/tornadoweb/tornado) from 6.5.4 to 6.5.5. -
  [Changelog](https://github.com/tornadoweb/tornado/blob/master/docs/releases.rst) -
  [Commits](https://github.com/tornadoweb/tornado/compare/v6.5.4...v6.5.5)

--- updated-dependencies: - dependency-name: tornado dependency-version: 6.5.5

dependency-type: indirect ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump tornado from 6.5.5 to 6.5.6
  ([`7bcc4b0`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/7bcc4b0264291a9858a85527fdba3c70d90c4369))

Bumps [tornado](https://github.com/tornadoweb/tornado) from 6.5.5 to 6.5.6. -
  [Changelog](https://github.com/tornadoweb/tornado/blob/master/docs/releases.rst) -
  [Commits](https://github.com/tornadoweb/tornado/compare/v6.5.5...v6.5.6)

--- updated-dependencies: - dependency-name: tornado dependency-version: 6.5.6

dependency-type: indirect ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump tornado from 6.5.6 to 6.5.7
  ([`9476477`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/94764771e4747d5ffb2f08e5ce4734782737a0c1))

Bumps [tornado](https://github.com/tornadoweb/tornado) from 6.5.6 to 6.5.7. -
  [Changelog](https://github.com/tornadoweb/tornado/blob/master/docs/releases.rst) -
  [Commits](https://github.com/tornadoweb/tornado/compare/v6.5.6...v6.5.7)

--- updated-dependencies: - dependency-name: tornado dependency-version: 6.5.7

dependency-type: indirect ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump urllib3 from 2.6.3 to 2.7.0
  ([`cd574ed`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/cd574ed7e20476f781bb741ce1f1ef4041f9b0c6))

Bumps [urllib3](https://github.com/urllib3/urllib3) from 2.6.3 to 2.7.0. - [Release
  notes](https://github.com/urllib3/urllib3/releases) -
  [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst) -
  [Commits](https://github.com/urllib3/urllib3/compare/2.6.3...2.7.0)

--- updated-dependencies: - dependency-name: urllib3 dependency-version: 2.7.0

dependency-type: indirect ...

Signed-off-by: dependabot[bot] <support@github.com>

- Centralize NLR developer URLs
  ([`3e5a182`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/3e5a182428fa057116d1e2e91270363432670751))

- Chore: consolidate case-colliding .Jules into .jules
  ([`f288087`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/f288087715162c29aa31eeff9dcb3a45eee35326))

git tracked three Jules paths — `.Jules/palette.md`, `.jules/palette.md` and `.jules/bolt.md` — but
  on a case-insensitive filesystem `.Jules` and `.jules` are the same directory. The two palette.md
  blobs differed (46 lines vs 120), so the working copy on disk could only ever match one of them;
  the other showed as a phantom "modified" file and any branch switch / checkout was fragile.

Drop the stale capital-J `.Jules/palette.md` (the diverged 46-line copy) and keep the canonical
  lowercase `.jules/` directory (palette.md + bolt.md), matching the .github/.vscode convention. The
  retained palette.md is the current authoritative content.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>

- Fix heading hierarchy and filename preview placement
  ([`b969d48`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/b969d4869d5c4e6d7bdc94d7dc92812570add447))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Fix: make semantic-release recognize gitmoji commits
  ([`0a9d5e9`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/0a9d5e9fe2bf33bae8e7794d49594ddd2ab1d52c))

Automatic versioning had been frozen at 0.5.0 since January: the Release workflow ran green on every
  push but always concluded "no_release".

Cause: python-semantic-release defaults to the Conventional Commits

parser, but this repo's commits are gitmoji ("🎨 Palette: …" from the Palette/Jules bot, "⚡️ Bolt …"
  perf commits, dependabot "Bump …"). None match feat/fix/etc., so 69 commits since v0.5.0 produced
  no bump.

Switch commit_parser to "emoji" and map the gitmoji actually used in this repo to bump levels (🎨 and
  friends → patch, ✨ → minor, 💥 → major).

Verified with `semantic-release version --print` over real history: before (conventional): next
  release = no_release, stays 0.5.0 after (emoji): next release = patch, 0.5.1

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>

- Fix: re-enable request button for valid API keys
  ([`128d607`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/128d607264c10906d0e3d9cb0ee5c4ee3c7b59c7))

Commit 534827f gated the "Request from NLR" button on `len(api_key) == 40` with no whitespace
  trimming, and the default-key path never stripped the loaded key. A key from st.secrets/env with a
  trailing newline therefore read as 41 chars: it passed hash verification ("Verified ✅") yet left
  the button permanently disabled — the app could no longer request data.

The validation lived entirely in app/streamlit_app.py, which has no tests and is excluded from
  coverage, so the regression shipped unnoticed.

- Extract the key rules into nlr_psm3_2_epw/validation.py (normalize_api_key, is_api_key_verified,
  is_api_key_valid) — a pure, UI-free module that the suite can actually cover. - Trim keys on every
  path; treat a verified default key as valid regardless of length. - Add tests/test_validation.py
  (12 cases incl. the trailing-newline regression). Suite: 35 passed / 1 skipped, 100% coverage
  retained.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>

- Hello! Jules here. I've softened the preliminary validation warnings in the Streamlit app for you:
  ([`0d3f270`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/0d3f270c79b7714a76e6c7fa04b4f2b2dbbadc33))

* I changed the aggressive `st.error` states (with stop sign icons) to `st.warning` (with
  warning/key icons) for preliminary missing inputs (like the API key and empty year fields). * This
  provides a less hostile user experience when the form initially loads or before the user is ready
  to proceed. * I maintained the existing strict backend validation.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Merge pull request #22 from SustainableUrbanSystemsLab/dependabot/uv/tornado-6.5.5
  ([`27d948f`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/27d948f3b53cae680b2a78e157af802f332d6b81))

Bump tornado from 6.5.4 to 6.5.5

- Merge pull request #46 from SustainableUrbanSystemsLab/dependabot/uv/requests-2.33.0
  ([`f5ad035`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/f5ad0359b7c4688e4844654504910c365541d2d0))

Bump requests from 2.32.4 to 2.33.0

- Merge pull request #53 from SustainableUrbanSystemsLab/dependabot/uv/pygments-2.20.0
  ([`08aea2c`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/08aea2c8216379903d4991c24a9a4d8d8a40fdd0))

Bump pygments from 2.19.2 to 2.20.0

- Merge pull request #59 from SustainableUrbanSystemsLab/update-nrel-domain-6825166294154430686
  ([`c391a08`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/c391a0847e34088d3c5f345e50a2715388f1402e))

Update NREL domain to developer.nlr.gov

- Merge pull request #60 from SustainableUrbanSystemsLab/palette-inline-captions-7645150978572403547
  ([`107db3d`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/107db3d6edd5678b91825873eecadf309d95854b))

🎨 Palette: Replace inaccessible tooltips with inline captions

- Merge pull request #62 from
  SustainableUrbanSystemsLab/palette-onboarding-callouts-15242415948000224808
  ([`06e254c`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/06e254cfedd1417303f673a98a83ded9b202c4a3))

🎨 Palette: Improve onboarding callouts and validation clarity

- Merge pull request #63 from SustainableUrbanSystemsLab/dependabot/uv/pillow-12.2.0
  ([`cd4daee`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/cd4daee32dbafdfaa52373eb71700f50e8298aa6))

Bump pillow from 11.3.0 to 12.2.0

- Merge pull request #64 from SustainableUrbanSystemsLab/dependabot/uv/pytest-9.0.3
  ([`05c0fe4`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/05c0fe4dd01204bee99198e1b7d7fd36f83657a4))

Bump pytest from 9.0.2 to 9.0.3

- Merge pull request #65 from SustainableUrbanSystemsLab/dependabot/uv/gitpython-3.1.47
  ([`db1883e`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/db1883eb277a4a38b2cb2a5a227c598e5afdaaae))

Bump gitpython from 3.1.46 to 3.1.47

- Merge pull request #67 from SustainableUrbanSystemsLab/dependabot/uv/gitpython-3.1.50
  ([`cbc968e`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/cbc968ecaeaa93cf3fbd5376d0bef23dc31c29c0))

Bump gitpython from 3.1.47 to 3.1.50

- Merge pull request #68 from SustainableUrbanSystemsLab/dependabot/uv/urllib3-2.7.0
  ([`57db857`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/57db857f95470ee2de7eb04824312eb0893e3d19))

Bump urllib3 from 2.6.3 to 2.7.0

- Merge pull request #69 from SustainableUrbanSystemsLab/dependabot/uv/idna-3.15
  ([`7f60d2f`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/7f60d2fca7048aefaec1300bf5649c94f8e75a12))

Bump idna from 3.11 to 3.15

- Merge pull request #70 from SustainableUrbanSystemsLab/dependabot/uv/pyarrow-23.0.1
  ([`129407e`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/129407e2ccd9253da872adafb4e941ddc3f0ccc5))

Bump pyarrow from 23.0.0 to 23.0.1

- Merge pull request #71 from
  SustainableUrbanSystemsLab/palette/soften-preliminary-validation-17398420198848322312
  ([`fbdc263`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/fbdc26380804042fe39b1ad4ee1ff2697a1aabea))

🎨 Palette: Soften preliminary validation warnings

- Merge pull request #72 from
  SustainableUrbanSystemsLab/palette/dynamic-filename-preview-11049598253098347086
  ([`4c0d1cd`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/4c0d1cde082acb92e53f0780fde27926befb1d32))

🎨 Palette: Add Dynamic Output Filename Preview

- Merge pull request #73 from
  SustainableUrbanSystemsLab/palette/symmetrical-guidance-16234176400303835302
  ([`d903c6b`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/d903c6b76faffc2a264ee3ab26cf38445e5538d0))

🎨 Palette: Add explicit inline instruction to Location field

- Merge pull request #74 from SustainableUrbanSystemsLab/dependabot/uv/tornado-6.5.6
  ([`ff61856`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/ff618569c5f4aa06bff1fe9f2e23b8d0e60897dc))

Bump tornado from 6.5.5 to 6.5.6

- Merge pull request #75 from
  SustainableUrbanSystemsLab/palette/heading-and-hierarchy-9200088913591375438
  ([`868dca2`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/868dca26c0bbe39a96f23bf5d85f7299c6184d3c))

🎨 Palette: Improve heading hierarchy and visual flow

- Merge pull request #76 from
  SustainableUrbanSystemsLab/palette/full-width-warnings-17925917674607352390
  ([`5a9d7f9`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/5a9d7f9afbe7847bd9ed9568f34f7ad4b9f9348a))

🎨 Palette: Full-width validation feedback

- Merge pull request #77 from
  SustainableUrbanSystemsLab/palette-visual-symmetry-validation-13668552525736590435
  ([`fe1dd91`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/fe1dd916be7aaee9d1a636f5258e0a03133ae5a5))

🎨 Palette: Add visual symmetry to layout and future-year form validation

- Merge pull request #78 from
  SustainableUrbanSystemsLab/palette-visual-hierarchy-map-instructions-162723039110846544
  ([`50c8027`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/50c8027341750e26cdad8e7f6dbd24df352891a2))

🎨 Palette: Improve visual hierarchy and map instruction callout

- Merge pull request #79 from
  SustainableUrbanSystemsLab/palette-ux-improvements-17549111273740977864
  ([`2f12f60`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/2f12f60ab634e3914754b0bb4dafc4eed68db386))

🎨 Palette: Improve error message actionability and visual symmetry

- Merge pull request #80 from SustainableUrbanSystemsLab/dependabot/uv/tornado-6.5.7
  ([`7b8ec74`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/7b8ec74a2cc99cff782fb37aba64e1a27fb64339))

Bump tornado from 6.5.6 to 6.5.7

- Merge pull request #81 from SustainableUrbanSystemsLab/palette-result-card-14798868079706585128
  ([`5ba845a`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/5ba845a27edd36c365c96fd226426d436724363a))

🎨 Palette: Add Result Card and Label Symmetry

- Merge pull request #82 from SustainableUrbanSystemsLab/palette/map-sync-ux-9812051039992699195
  ([`2f46816`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/2f46816a84f4e87c584105a3fae27693a7230873))

🎨 Palette: Map bidirectional synchronization

- Merge pull request #83 from
  SustainableUrbanSystemsLab/palette-error-ux-semantic-title-3293971129848956446
  ([`b60c15c`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/b60c15caadaae33eb6bebcd0b2d9a632f178cc4e))

🎨 Palette: [Graceful error degradation & semantic titles]

- Merge pull request #84 from SustainableUrbanSystemsLab/palette-button-tooltips-6250777848032199794
  ([`1c8ac89`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/1c8ac89a5f1caa8bb0669837e787a0653cb86e31))

🎨 Palette: Improve button feedback and actionable help

- Merge pull request #85 from
  SustainableUrbanSystemsLab/palette-ux-validation-guidance-3590063744810696382
  ([`18c48cf`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/18c48cfabf73b817a45d728e8e9eda64aeb1e77f))

🎨 Palette: Context-aware API error guidance and validation cleanup

- Merge pull request #86 from
  SustainableUrbanSystemsLab/palette-add-coordinate-placeholders-8656687197470566834
  ([`fd1480c`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/fd1480c8fe6ffe0a05dd36ccb81cf915ee5d63e4))

🎨 Palette: Add placeholders to coordinate inputs

- Merge pull request #87 from
  SustainableUrbanSystemsLab/palette-actionable-api-warning-7850047280015601575
  ([`95ecb9c`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/95ecb9cbfaa1a2ef1f9444e49586f69a9a0f86e6))

🎨 Palette: Add actionable troubleshooting to unverified API key warning

- Merge pull request #88 from
  SustainableUrbanSystemsLab/palette-proactive-expander-5487330636984665684
  ([`d952e45`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/d952e45ee0ded9b13a12245a06b0bf0a786ae4e4))

🎨 Palette: Proactively expand API configuration on default key failure

- Merge pull request #89 from SustainableUrbanSystemsLab/palette-ux-improvements-4338420814355445154
  ([`de3d255`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/de3d255332689bd632d6844536d444d99f3a3db1))

🎨 Palette: [UX] Forgiving API key formatting & reduced visual clutter

- Merge pull request #90 from
  SustainableUrbanSystemsLab/palette-api-key-validation-13835974635152299914
  ([`a561568`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/a561568214881a6a32c22083f58e9eeed827aedc))

🎨 Palette: [Improve inline API key validation and disabled state]

- Merge pull request #91 from SustainableUrbanSystemsLab/fix/api-key-validation
  ([`0104c21`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/0104c21e8bb5b686398644430370ce3d95f2a5e4))

fix: re-enable request button for valid API keys

- Merge pull request #92 from SustainableUrbanSystemsLab/fix/semantic-release-emoji
  ([`17c7293`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/17c7293b1a41ac00dad1fc191b3ec6361de08af9))

fix: make semantic-release recognize gitmoji commits

- Merge pull request #93 from SustainableUrbanSystemsLab/chore/consolidate-jules
  ([`808bbd6`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/808bbd641e934cbf27cb2e29e1fe3c2d696d697c))

chore: consolidate case-colliding .Jules into .jules

- Normalize Jules directory casing
  ([`6c7e30b`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/6c7e30b7e54a13cb13dab0441114f7183f0b6173))

- Rename package from NREL to NLR
  ([`09d6707`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/09d67071bb2833b412c17b834fcd4af4e9a6c4fd))

- Update NREL domain from developer.nrel.gov to developer.nlr.gov
  ([`1f40294`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/1f40294414a59cae9bd880f65fe4e6319dc7edaf))

Updated all hardcoded URLs pointing to developer.nrel.gov to use developer.nlr.gov to ensure service
  continuity ahead of the April 30, 2026 deadline.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Ux: Improve onboarding callouts and validation clarity
  ([`442875e`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/442875e8f85054385e80e89c4ecfd90bf36fdebe))

Extracted the API key signup link into a visually distinct conditional callout to reduce visual
  fatigue for returning users. Softened the location name validation error to a warning and fixed a
  typo in the final error message.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

### 🎨

- 🎨 Palette: [Graceful error degradation & semantic titles]
  ([`11e925c`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/11e925c63aedfdb5587ff43ece903b8437b9ade9))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: [Improve inline API key validation and disabled state]
  ([`534827f`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/534827fe436b27d7fa1238b2eec6bae231c39fcc))

Here is what I have implemented: - Extracted the API key validation logic outside the expander. -
  Added a full-width inline warning specifically for invalid API key lengths. - Explicitly disabled
  the primary button when the API key is not exactly 40 characters long. - Updated my journal to
  document the learning about not hiding validation warnings in collapsed expanders.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: [UX improvement] Map bidirectional synchronization
  ([`c35b52b`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/c35b52b37f5ec76f2e7159d32c73334f58d03bf3))

- Added st.session_state tracking for input_lat and input_lon - Passed center coordinates
  dynamically to st_folium - Replaced value parameter with key binding in number_input to establish
  a single source of truth

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: [UX] Forgiving API key formatting & reduced visual clutter
  ([`b2d5aa1`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/b2d5aa1ed2bf9f2732c8ef5d37887c3c8c03006e))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Add actionable troubleshooting to unverified API key warning
  ([`a31c8da`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/a31c8da8ce24530d24a3572ecea81b8f7639025a))

Updates the generic "Unverified" default API key warning to provide clear, actionable instructions
  directing the user to check their `.streamlit/secrets.toml` file. This reduces cognitive load and
  provides a clear recovery path for users stuck in an unverified state. Also appends this UX
  learning to the Palette journal.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Add dynamic output filename preview
  ([`6c323f2`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/6c323f2242b0679eecc3598c27bb23aaf1849103))

Added a dynamic, real-time preview of the expected output filename beneath the Location Name input
  field to provide immediate feedback and set clear expectations for the user before downloading.
  Improved accessibility by explicitly labeling 'Location Name' and 'Year' as required.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Add placeholders to coordinate inputs
  ([`3e113ba`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/3e113bac6f07e30cb8992c78d11c1a3aff040705))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Add Result Card and Label Symmetry
  ([`24649f3`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/24649f3cb1ebe0115a065a6c0896711286802fe7))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Add visual symmetry to layout and future-year form validation
  ([`a2be768`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/a2be76846d7a12c3affe044463a95c5863cca6b1))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Context-aware API error guidance and validation cleanup
  ([`2fedf9d`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/2fedf9d203a5369555d8ea8baf7f0740bae0df08))

- Removes a duplicate location validation warning to reduce visual clutter. - Adds context-aware
  troubleshooting guidance for users providing custom API keys. - Appends UX learnings to
  `.Jules/palette.md`.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Improve button feedback and actionable help
  ([`b68a09d`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/b68a09dd67f45d0e2411cf08f6c92c2dabfe66e0))

Removed disabled state explanations from the button `help` tooltip, as tooltips are inaccessible on
  mobile devices. Hoisted these validation errors into prominent `st.warning` blocks so users can
  immediately see why the download action is disabled. Made year validation errors more actionable,
  and added a helpful signup link to the API key section.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Improve error message actionability and visual symmetry
  ([`0f525dd`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/0f525dd23b9ea8bbf893002f249267a51122437c))

- Explain EPW acronym in the introduction - Add actionable troubleshooting steps and an icon to the
  data availability error message - Ensure visual symmetry by making Latitude and Longitude indicate
  "(required)"

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Improve visual hierarchy and map instruction callout
  ([`a96962c`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/a96962cdca1b990f8d4c3921b2d71ffb63ced40a))

- Upgraded the markdown header for "Location & Time Details" to use `st.header(...,
  divider="gray")`. - Replaced plain text map instructions with a visually distinct `st.info`
  callout including an icon. - Appended learning to `.Jules/palette.md`.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Proactively expand API configuration on default key failure
  ([`5cf1c1c`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/5cf1c1ca22d64453ce8ece8c82b19477d753723b))

- Automatically expands the API key configuration `st.expander` when a default API key fails hash
  verification. - Prevents users from being confused by hidden error messages when requests fail.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Render form validation warnings full-width
  ([`889258a`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/889258ab6bee660e2e2e08037316c7935c2812fa))

Extracted the location and year validation warnings from `st.columns` in `streamlit_app.py` and
  placed them chronologically before the primary action button to improve readability and visual
  layout, especially on mobile devices. Documented this finding in the UX journal.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Replace inaccessible tooltips with inline captions
  ([`4ce452e`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/4ce452ee7bf23cf62e36b01ccaf5614fb10cf06c))

Moved critical instructions from `help` parameters (hover-only tooltips) to explicit `st.caption`
  elements placed immediately below the inputs in Streamlit to improve accessibility on mobile and
  touch devices.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>


## v0.5.0 (2026-04-03)

### Other

- Add character limit to location name text input
  ([`53d7e1b`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/53d7e1b715ed35f537bee8ddfdc6fcb38dee89fa))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Add EPW file preview expander before download
  ([`99d93a5`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/99d93a5a0617c0eca5e563ff1abae4801027fd8d))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Add explicit page config for browser tab context
  ([`56f4df3`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/56f4df379e7e5c7da50763b95986659628451554))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Add fine-grained step controls to coordinate inputs
  ([`1ece71b`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/1ece71b6406736d83dd3d790a7d504a9d098bbae))

Sets step=0.0001 on the Streamlit number_input fields for Latitude and Longitude. This replaces the
  default 0.01 step size, allowing users to make precise geographic adjustments (~11m) via UI arrows
  or keyboard controls.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Bump streamlit from 1.42.2 to 1.54.0
  ([`2676ec9`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/2676ec9472e589aaf00cddde23dd00089ef92b1a))

Bumps [streamlit](https://github.com/streamlit/streamlit) from 1.42.2 to 1.54.0. - [Release
  notes](https://github.com/streamlit/streamlit/releases) -
  [Commits](https://github.com/streamlit/streamlit/compare/1.42.2...1.54.0)

--- updated-dependencies: - dependency-name: streamlit dependency-version: 1.54.0

dependency-type: direct:production ...

Signed-off-by: dependabot[bot] <support@github.com>

- Feat: improve location input UX and accessibility
  ([`6574345`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/6574345468446d78b100bc75f0f88e7c277277eb))

- Clears the location name input instead of silently falling back to 'Atlanta' when reverse
  geocoding fails. - Moves the location instructions from an inaccessible mobile tooltip (`help`) to
  an explicit inline `st.caption` to ensure accessibility on all devices.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Merge pull request #36 from
  SustainableUrbanSystemsLab/palette-async-feedback-and-constraints-11238222673988586052
  ([`0ef0c45`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/0ef0c45cba86f4027871b963fb36d5dafd491397))

🎨 Palette: Add async feedback for map geocoding and input constraints

- Merge pull request #37 from SustainableUrbanSystemsLab/bolt-session-pooling-2156584688273582059
  ([`55e672c`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/55e672cf0df9b9c5117bccb1314c2eeadeadec3e))

⚡ Bolt: Implement HTTP connection pooling for API requests

- Merge pull request #38 from SustainableUrbanSystemsLab/palette-location-limit-1344179376662709415
  ([`3e9ac9d`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/3e9ac9d06040b5c6fb377a503c0201ee9e85397d))

🎨 Palette: Add character limit to location text input

- Merge pull request #39 from
  SustainableUrbanSystemsLab/palette-dynamic-api-label-2115644993085277061
  ([`53f6aa0`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/53f6aa08fe901aaa68eb1476e350e6aae02dd035))

🎨 Palette: Dynamically update API Key input label based on required state

- Merge pull request #40 from SustainableUrbanSystemsLab/palette/add-page-config-3266959766459024466
  ([`d8e7d92`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/d8e7d92c3bc7eaab0b820f8e97c63e20ae9b91ef))

🎨 Palette: Add explicit page config for browser tab context

- Merge pull request #41 from SustainableUrbanSystemsLab/bolt-optimize-epw-write-5134566356781262374
  ([`cb34b7a`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/cb34b7a6e0ec2636f11a12911d4f6ce41a27f052))

⚡ Bolt: Optimize EPW CSV write performance

- Merge pull request #42 from
  SustainableUrbanSystemsLab/palette-coordinate-steppers-3426884472935254927
  ([`bbb93a9`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/bbb93a92e2d661657d95f92526869f9241aced87))

🎨 Palette: Add fine-grained step controls to coordinate inputs

- Merge pull request #43 from
  SustainableUrbanSystemsLab/bolt-tmy-timestamp-optimization-8306195363083152227
  ([`e457b27`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/e457b27b934bb0a5a2838a751728abfcb047844a))

⚡ Bolt: [performance improvement] Optimize TMY timestamp parsing

- Merge pull request #44 from
  SustainableUrbanSystemsLab/palette-ux-improvements-14840708416197176650
  ([`4b1257f`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/4b1257fd07885489637bfa7a0f1a2d4f188be012))

🎨 Palette: Fix link accessibility and add API key placeholder

- Merge pull request #45 from SustainableUrbanSystemsLab/dependabot/uv/streamlit-1.54.0
  ([`1baa2ff`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/1baa2ff21d8a4cc5fa91e32f704785daefb0c61e))

Bump streamlit from 1.42.2 to 1.54.0

- Merge pull request #47 from
  SustainableUrbanSystemsLab/palette-full-width-buttons-6201936118589134009
  ([`7785005`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/778500528e669a9c6387572da8599d27c64cdf80))

🎨 Palette: [UX improvement] Use full-width for primary action buttons

- Merge pull request #48 from
  SustainableUrbanSystemsLab/palette-remove-directional-language-15983817482082073740
  ([`d7ba02e`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/d7ba02e0c0934a347a32f321b0131f397dd2ce70))

🎨 Palette: Remove directional language from UI instructions

- Merge pull request #49 from SustainableUrbanSystemsLab/bolt-optimize-epw-write-8339112837654651844
  ([`ba249c0`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/ba249c0f62e88650e2f58cd2096f7c8eeec5f5de))

⚡ Bolt: [performance improvement] optimize epw file writing for mixed-type dataframes

- Merge pull request #50 from SustainableUrbanSystemsLab/palette-ux-improvements-8749359003963610281
  ([`fc8eccb`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/fc8eccbf15c0e978e3e2037a38ed0f4b12b54997))

🎨 Palette: [UX improvement] Enhance accessibility instructions and file size visibility

- Merge pull request #51 from SustainableUrbanSystemsLab/palette-ux-context-tmy-7538813137213512108
  ([`2be3a16`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/2be3a1611039941cbcda6b3f660a572ce5282723))

🎨 Palette: Add contextual explanations for TMY abbreviation and external tools

- Merge pull request #52 from
  SustainableUrbanSystemsLab/bolt-optimize-daterange-12220437882034373476
  ([`650c100`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/650c10017a5cb201c3a03d0c567a51ddb330cd76))

⚡ Bolt: Use native API time columns instead of synthetic pd.date_range

- Merge pull request #54 from
  SustainableUrbanSystemsLab/bolt-remove-redundant-cast-11590846138496253335
  ([`f01f552`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/f01f552b09ee00c1ea6d6a20bcde7f1851b8ed07))

⚡ Bolt: Remove redundant cast on pressure array

- Merge pull request #55 from
  SustainableUrbanSystemsLab/palette/visualize-epw-hierarchy-8507530681680429452
  ([`0b7eb57`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/0b7eb573b30b9272e93accd1d6bb956227e3d266))

🎨 Palette: Improve Post-Download Visual Hierarchy

- Merge pull request #56 from SustainableUrbanSystemsLab/palette/file-preview-14200588603729925716
  ([`040015a`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/040015acce2e9a1344889ade7ae335d88c3b29ce))

🎨 Palette: Add EPW file preview expander

- Merge pull request #57 from
  SustainableUrbanSystemsLab/bolt-optimize-epw-preview-9709900594392156778
  ([`bcf0bca`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/bcf0bca93b5d45e812fd1821efa2d3e50b7e21ab))

⚡ Bolt: Optimize file preview rendering

- Merge pull request #58 from
  SustainableUrbanSystemsLab/palette/ux-location-fallback-and-caption-9196319330848989264
  ([`fb9ff77`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/fb9ff7741837524536bb4df259f39cc3af2483fd))

🎨 Palette: Improve Location Input UX and Fallback Behavior

- Optimize EPW Date Range generation by extracting native time columns
  ([`a32ebb2`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/a32ebb23a49567a07a661a45b3e2dc5572abbe53))

Replaced synthetic `pd.date_range` generation with direct extraction of native time columns (`Year`,
  `Month`, `Day`, `Hour`, `Minute`) directly from the NREL response DataFrame, which avoids dispatch
  and creation overhead and improves DataFrame construction performance.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Optimize TMY timestamp extraction using `to_numpy(dtype=int)`
  ([`5e79759`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/5e797594cf58ac845d4a6effeb405fc7eaea8089))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Perf: optimize epw file preview decoding logic
  ([`69479da`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/69479da52cf94cd6f5aafac77562aadbf98aa67c))

Changed the file preview logic to split the raw byte string with a maxsplit before decoding, rather
  than decoding the entire 2.5MB+ file and splitting it into thousands of list items just to show 10
  lines. This dramatically reduces memory overhead and CPU time during file processing.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Performance: optimize EPW file writing for mixed-type DataFrames
  ([`455a78d`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/455a78dc6b301fd1184c48af89a719dc2db0139a))

Replaced `.values.tolist()` with pandas native `.to_csv()` when writing EPW files to avoid
  significant memory overhead caused by NumPy casting mixed types to object arrays.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Remove redundant .astype(int) cast on Pressure array
  ([`eb3d937`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/eb3d9370dd42a6b89bd101fa92614eddc227d128))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

### ⚡

- ⚡ Bolt: Implement HTTP connection pooling for API requests
  ([`8654ee3`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/8654ee324cfd27bfa312e192f86c4f23a03eb79d))

Added a global `requests.Session()` object in `nrel_psm3_2_epw/assets.py` to reuse the underlying
  TCP connection across repeated API calls, significantly reducing the overhead of TCP handshakes
  and TLS negotiations.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- ⚡ Bolt: Optimize EPW CSV write performance
  ([`f6eac29`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/f6eac299590bab130727976f3dd29c3179dff672))

Replaced pandas.to_csv with csv.writerows and numpy array conversion to speed up serialization of
  the EPW file.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

### 🎨

- 🎨 Palette: [UX improvement] Enhance accessibility instructions and file size visibility
  ([`ea7e16c`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/ea7e16c3161d9439288c6d4a02393d5f29f6798d))

- Updated map instruction to avoid exclusive pointer-driven language. - Added file size display to
  the download success message. - Appended learning to .Jules/palette.md

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: [UX improvement] Use full-width for primary action buttons
  ([`a147833`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/a1478338521a9fe0201740f1aa6e6324403e93d4))

Added `use_container_width=True` to the primary "Request from NREL" and "Download EPW" action
  buttons in the Streamlit interface. This significantly improves usability on mobile devices by
  providing a larger touch target and establishes a stronger visual hierarchy on all devices.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Add async feedback for map geocoding and input constraints
  ([`e37859a`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/e37859a789547d7a8dfab7c0f3f5f6f25bda4c63))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Add contextual explanations for TMY abbreviation and external tools
  ([`f1a4bdb`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/f1a4bdb2b4f379bf632aab83d07ca736f67b5117))

- Added an inline `st.caption` explaining the "TMY" domain jargon beneath the Year input to comply
  with WCAG 3.1.4 (Abbreviations). - Display the explicit downloaded `os.path.basename` filename in
  the success message to clarify what file was generated. - Appended descriptive context to external
  visualization links so users know what to expect before clicking them. - Recorded UX learning in
  `.Jules/palette.md`.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Dynamically update API Key input label based on required state
  ([`57a9c40`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/57a9c40f26749e5ed5f514363e9e32c20cdb9c77))

This commit modifies the Streamlit app to dynamically update the text input label and help text for
  the API Key Configuration section. Instead of statically saying the input is "(optional)", the
  label and help text will now explicitly say "(required)" if a default API key has not been loaded
  by the application. This prevents user confusion and serves as proactive inline feedback.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Fix link accessibility and add API key placeholder
  ([`238cfee`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/238cfee11973532991f0715e04b11d4ba4170f29))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Improve Post-Download Visual Hierarchy
  ([`bfb4cf6`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/bfb4cf642e9c6474503b1d6a057334986b1e3b97))

Consolidate the post-download "Visualize your EPW file" section into a single, cohesive `st.info`
  block. This visually groups the supplementary external tool links and adds a distinct icon,
  improving overall visual hierarchy and readability instead of stacking multiple plain
  `st.markdown` elements.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Remove directional language from UI instructions
  ([`0ea45d9`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/0ea45d9666af38cf474b0eb17b603d82ee223ab7))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>


## v0.4.0 (2026-03-19)

### Other

- Feat(ux): add max_chars constraint to API key input
  ([`b1f33d9`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/b1f33d9203a8e661d46a8120c2b7282c67506743))

Add `max_chars=40` parameter to the API key `st.text_input` in the Streamlit application. This
  provides a helpful visual character counter (0/40) for users and proactively prevents them from
  pasting mistakenly large strings or hidden trailing spaces into the 40-character NREL API key
  field.

Also updated `.Jules/palette.md` with UX learnings regarding this change.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Merge pull request #35 from SustainableUrbanSystemsLab/palette-max-chars-992721552596924747
  ([`2ab702f`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/2ab702fa67aaa8a5599d20cab111417026cea09c))

🎨 Palette: Add max_chars constraint to API key input


## v0.3.0 (2026-03-18)

### Other

- Feat: proactive inline validation for API keys
  ([`fa6ff49`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/fa6ff49b2592cea0c582640b98d0375e9b4c2ef9))

Added inline warning when the loaded user API key does not match the standard NREL length (40 chars)
  to prevent users from making inevitable network failures. Added emojis for better visual parsing.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Merge pull request #23 from
  SustainableUrbanSystemsLab/palette/dynamic-validation-ux-3864661238726438314
  ([`daffa76`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/daffa76dc6fdfe3b18ecae60120eb8ae3a923032))

🎨 Palette: Improve form validation UX with dynamic disabled states

- Merge pull request #24 from
  SustainableUrbanSystemsLab/bolt-optimize-dataframe-datetime-construction-2431001485697188536
  ([`41eef46`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/41eef46d2b263929ae4987dfa40e5de78c10b362))

⚡ Bolt: [performance improvement] optimize DataFrame datetime array extraction

- Merge pull request #25 from
  SustainableUrbanSystemsLab/bolt-optimize-epw-read-pass-8942359334880824241
  ([`9a63dff`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/9a63dff8446ff1728d4297107c4b47e13dccf6c6))

⚡ Bolt: Optimize EPW file reading by removing redundant I/O passes

- Merge pull request #26 from
  SustainableUrbanSystemsLab/palette-map-toast-feedback-7761321540219500663
  ([`3f6d5bc`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/3f6d5bccab98d0300e28641f45c11739118ff403))

🎨 Palette: Add map interaction toast feedback

- Merge pull request #27 from
  SustainableUrbanSystemsLab/bolt-optimize-dataframe-map-16834709869944052540
  ([`720674b`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/720674b5a90e9d3cb5fd93dbbee07e85dff584e1))

⚡ Bolt: Remove redundant set_index and typecast overhead during DataFrame mapping

- Merge pull request #28 from
  SustainableUrbanSystemsLab/palette-inline-validation-7801668513317000021
  ([`cef47f5`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/cef47f50e80b4f7c90458d3826ce712a2e4b6ee3))

🎨 Palette: Add inline validation feedback for Year input

- Merge pull request #29 from
  SustainableUrbanSystemsLab/palette/improve-disabled-state-context-16497181011513664301
  ([`b73c7f2`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/b73c7f269e63634d13eab0c44451cee7cf7f3420))

🎨 Palette: Improve disabled state context and button affordance

- Merge pull request #30 from SustainableUrbanSystemsLab/palette-responsive-map-8633784821668243150
  ([`2846413`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/28464133fd1d065bf84f4ebc97788334d1ce8c21))

🎨 Palette: Make interactive map responsive across all device sizes

- Merge pull request #31 from
  SustainableUrbanSystemsLab/bolt-optimize-tmy-datetime-5537995363432937906
  ([`9cc34f6`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/9cc34f6525bac145816460989412e7cf7efb7c23))

⚡ Bolt: Optimize TMY datetime parsing by using existing numeric columns

- Merge pull request #32 from
  SustainableUrbanSystemsLab/bolt/st-folium-map-cache-13287608151877097483
  ([`bf224b4`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/bf224b446ec81c436da35d13bc24efef6f4284be))

⚡ Bolt: [performance improvement] optimize folium map interactions and rendering

- Merge pull request #33 from
  SustainableUrbanSystemsLab/jules/inline-validation-palette-13552340081463032302
  ([`603c3fb`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/603c3fb58ef3589ee37565931e661a340843b602))

🎨 Palette: Add inline validation for Location Name

- Merge pull request #34 from
  SustainableUrbanSystemsLab/palette-api-key-validation-15526395113371478280
  ([`7ddc582`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/7ddc582974e778384bc1dcc1250a6b8693ba912b))

🎨 Palette: Proactive inline validation for API keys

- Optimize pandas DataFrame construction by avoiding dispatch on DatetimeIndex
  ([`c312544`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/c3125441282c50a14b26e8ad546e3d17d6d6783a))

Extracted underlying raw NumPy int arrays from `pd.DatetimeIndex` properties (like
  `datetimes.year.values`) instead of relying on pandas Series cast via `.astype(int)`. This
  significantly speeds up the EPW DataFrame construction by removing expensive pandas type
  conversion and dispatch logic while maintaining safety and readability.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Optimize TMY datetime parsing by using existing numeric columns
  ([`113de59`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/113de593e1e28bc9f03ccfddfeb3e1730bf8d1bc))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

### ⚡

- ⚡ Bolt: Optimize EPW file reading by removing redundant I/O passes
  ([`ff7433b`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/ff7433b1f1698e692db360215a422ed435bed897))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- ⚡ Bolt: optimize folium map interactions and rendering
  ([`dc00add`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/dc00add8cec92ad6bbe859dbb767b36945028610))

Cache the `folium.Map` using `@st.cache_resource` to avoid HTML iframe regeneration and use
  `returned_objects=["last_clicked"]` to prevent expensive Python backend reruns when the map is
  just panned or zoomed by the user.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- ⚡ Bolt: Remove redundant set_index and typecast overhead during DataFrame mapping
  ([`e2effa9`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/e2effa9d35568b8a8f13f9bdb0094eeb0ffd0985))

- Removed `df.set_index(datetimes)` which was creating a completely unused and unnecessary memory
  copy of an 8760xN DataFrame since `.values` ignores the index anyway. - Removed a redundant
  `.astype(float)` cast before the final `.astype(int)` inside the `Atmospheric Station Pressure`
  multiplier logic. - Updated `.jules/bolt.md` documenting this finding.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

### 🎨

- 🎨 Palette: Add inline validation feedback for Year input
  ([`2d67b3d`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/2d67b3d5a587fac12193e9e55c33ee75fce7034c))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Add inline validation feedback for Year input
  ([`be6e261`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/be6e261d4450fb9dd7ffb20cb5c2acdfc18082ae))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Add inline validation for Location Name
  ([`aed090b`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/aed090b4af31902d8bc2daac325a8ef3d193eba0))

- Adds explicit st.error inline feedback when Location Name is empty - Dynamically disables "Request
  from NREL" button - Provides dynamic context in button tooltip - Appended learning to
  .Jules/palette.md

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Add toast feedback for map interactions
  ([`8c4212a`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/8c4212aa4c1adc57078783a689051fe9797749d6))

- Fixed unused variable `iframe_element` in temporary Playwright test - Restored accidentally
  deleted `verification.png` - Cleaned up duplicated `st.toast` blocks in `app/streamlit_app.py` -
  Avoided phantom toast on initial app load by checking for `last_map_click` existence - Formatted
  long strings to comply with linter line length

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Add toast feedback for map interactions
  ([`990fbbf`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/990fbbfda8c6523d31faac6e04e6c91200aa4685))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Improve disabled state context and button affordance
  ([`2b3ed6d`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/2b3ed6d5763b786c12af66ae4fde3d8efbc3687b))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Improve form validation UX with dynamic disabled states
  ([`6f81000`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/6f81000dd980f2e41d00ca37a45ddcf055cba84b))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Improve form validation UX with dynamic disabled states
  ([`a17facf`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/a17facf4a9a472b27864102430e2d54defe79112))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Make interactive map responsive across all device sizes
  ([`b5ed777`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/b5ed7778cf05cf38f432ce788da1f1531be358d2))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>


## v0.2.0 (2026-03-11)

### Other

- Feat: read version dynamically from package metadata
  ([`cf2d01a`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/cf2d01aef82a394dc1cf8d3e64106b2ca1e59f26))

Replace hardcoded "4.0.0" version in the Streamlit UI and User-Agent header with the installed
  package version via importlib.metadata. This ensures the displayed version stays in sync with
  semantic-release.

https://claude.ai/code/session_01SqjYWGRjhsP5CdjNCVyqRQ

- Merge pull request #21 from SustainableUrbanSystemsLab/claude/fix-build-versioning-9eDHO
  ([`8bb21d6`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/8bb21d6f444a2948c4a242cc465f37658c10a17c))

feat: read version dynamically from package metadata


## v0.1.0 (2026-03-11)

### Other

- .
  ([`ec7be9e`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/ec7be9e7117b7fc1e5bd0032e51e80351476018b))

- .
  ([`5814b0c`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/5814b0c752add37f151919d387ba81de22f95959))

- .
  ([`ca150e6`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/ca150e66a0d3ba909627c0ec6dfda49e87f57952))

- .
  ([`ac18e56`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/ac18e56612193dec300c2b45fe1df34c9e02d0fa))

- .
  ([`6c1b48a`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/6c1b48a732f4d618c76bb1c7fcc8d1145a6f9828))

- Add epw code explicitly
  ([`29a71cc`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/29a71cc2a95e7c46fdc49ed4552823449b293b4c))

- Add epw code explicitly
  ([`c737b1d`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/c737b1dcdbd40dda36dc0a7be0c8ab2fee5f50b5))

- Add map selection for latitude and longitude
  ([`8109648`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/8109648abbdbb9e057f4e1b51e2d7805e75fd9de))

- Added `streamlit-folium` and `folium` as dependencies - Updated the Streamlit app to include an
  interactive map where users can click to set the latitude and longitude inputs automatically -
  Maintained fallback to default coordinates if no location has been clicked

Co-authored-by: google-labs-jules[bot] <161369871+google-labs-jules[bot]@users.noreply.github.com>

- Added tests
  ([`ca3884c`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/ca3884cd90a68789d78cb906fa129d0fc54bbc2d))

- Added tests
  ([`47e2f40`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/47e2f4019afe255f1b36f8350347221befc6b801))

Update requirements.txt

- Added versioning
  ([`d30f34f`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/d30f34ff0069f3cccae304797318f23b1cd0597a))

- Bump protobuf from 5.29.5 to 5.29.6
  ([`dcf5a6e`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/dcf5a6e0b56212bb822d4c4a12d3402a3eae821a))

Bumps [protobuf](https://github.com/protocolbuffers/protobuf) from 5.29.5 to 5.29.6. - [Release
  notes](https://github.com/protocolbuffers/protobuf/releases) -
  [Commits](https://github.com/protocolbuffers/protobuf/commits)

--- updated-dependencies: - dependency-name: protobuf dependency-version: 5.29.6

dependency-type: indirect ...

Signed-off-by: dependabot[bot] <support@github.com>

- Bump requests from 2.32.3 to 2.32.4
  ([`8230de5`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/8230de57f27b0a85545334a88965ab932d736577))

Bumps [requests](https://github.com/psf/requests) from 2.32.3 to 2.32.4. - [Release
  notes](https://github.com/psf/requests/releases) -
  [Changelog](https://github.com/psf/requests/blob/main/HISTORY.md) -
  [Commits](https://github.com/psf/requests/compare/v2.32.3...v2.32.4)

--- updated-dependencies: - dependency-name: requests dependency-version: 2.32.4

dependency-type: direct:production ...

Signed-off-by: dependabot[bot] <support@github.com>

- Chore: add semantic release workflow and configuration
  ([`12a81da`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/12a81da9ed5391f4710f056b919bbbc11791f2ce))

Add python-semantic-release to project dependencies and configure it in pyproject.toml to handle
  automatic version bumping and release creation when merging to main. Also add a new GitHub Actions
  workflow for this purpose.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Clarify earliest year
  ([`5b0bf7f`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/5b0bf7f8b160e4500fdf3da4a029f2bece20d72e))

- Cleanup
  ([`235087f`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/235087f722da9d579ba42b0efd7f2aa7a623bc03))

Update requirements.txt

Fixes

- Create codeql-analysis.yml
  ([`12cd37c`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/12cd37c14a9bffa1f35384879835ead8462ae1f0))

- Create python-app.yml
  ([`ed971df`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/ed971dfe3d1c0feeaedb46453f7d110547d5efde))

- Create requirements.txt
  ([`2fd0556`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/2fd0556374fc7010dfe9c0037d5db59527f144c3))

- Create streamlit_app.py
  ([`e33c112`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/e33c1127d3c8a24f5dd5064de377c83a1e60446f))

- Create streamlit_app.py
  ([`033ded5`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/033ded5462c7a589422b2ea95bc7cb643a59717b))

- Feat(ui): add visual feedback and disabled state to NREL request button
  ([`d2532b9`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/d2532b9ff0975fe0b09f9b9934c08f8e49d76fab))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Feat: add resources for visualizing EPW files online
  ([`14675a6`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/14675a6c501bcde0eba9200cdbcb2457a744b038))

Adds links to EPWvis and CBE Clima Tool after a successful EPW file download to help users visualize
  their data.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Feat: add reverse geocoding to streamlit map
  ([`e4fdc35`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/e4fdc35967f02882ecd2584d1c21c75a913f1b6f))

- Added `requests` dependency to fetch location names from OpenStreetMap Nominatim API. -
  Implemented `get_location_name` with `@st.cache_data` to optimize Streamlit reruns. - Updated the
  map interaction to automatically populate the 'Location' input with the clicked location's name.

Co-authored-by: google-labs-jules[bot] <161369871+google-labs-jules[bot]@users.noreply.github.com>

- Fix problem with response timeout
  ([`bd531c9`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/bd531c9906fe333a9c2a52790e16f2876e2a691d))

- Fix unit for 'Atmospheric Station Pressure'
  ([`01aeee5`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/01aeee54c114ce816baa2ef587d87cfd1e681f70))

- Fix: use standard python build in semantic release
  ([`b5822b1`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/b5822b1ee44c3e16597bf536afbb362e416f4914))

The python-semantic-release GitHub Action runs in its own Docker container where uv is not
  available. Replace `uv build` with `pip install build && python -m build` which works in the
  container.

https://claude.ai/code/session_01SqjYWGRjhsP5CdjNCVyqRQ

- Fixes
  ([`d81d22f`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/d81d22f9b3bd7b868ac9c83feb02957364f4592b))

- Fixes for new version
  ([`f5c7afa`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/f5c7afa7784b94af336261833cc78bdb27069008))

- Fixes, checked readability
  ([`818f6d7`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/818f6d7c767e4e795e17bc526fa1b3132370b053))

- Initial commit
  ([`aadd044`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/aadd044bece9942d801b4aa780339b246f1f101d))

- Leap year
  ([`1511c01`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/1511c01b0189d98a8a67883cba76c89f20df11c0))

Fix leap year

- Merge branch 'main' of https://github.com/kastnerp/NREL-PSB3-2-EPW into main
  ([`94aa104`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/94aa10494c82a3efbdc98b8c47cee4b4994667b4))

- Merge branch 'main' of https://github.com/kastnerp/NREL-PSM3-2-EPW
  ([`ea13a02`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/ea13a02eb77e3ba18db1024b4482ba7a8fc60bd8))

- Merge pull request #1 from xtearas/main
  ([`364499d`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/364499d7d932454cad173eb8fa34566b487f330c))

update to new version of NREL Physical Solar Model (PSM)

- Merge pull request #10 from
  SustainableUrbanSystemsLab/bolt-optimize-epw-dataframe-7241393348361834664
  ([`a88120b`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/a88120b87ad067941efcb610df31ad8479fcd22d))

⚡ Bolt: Optimize EPW DataFrame construction

- Merge pull request #11 from SustainableUrbanSystemsLab/palette-ux-nrel-button-13406486057792155976
  ([`05f93e4`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/05f93e464635749c7d81e93f1e84ebae32ff259a))

🎨 Palette: Add visual feedback and disabled state to NREL request button

- Merge pull request #12 from SustainableUrbanSystemsLab/bolt-optimize-epw-write-2189851107543233260
  ([`2aeaaf6`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/2aeaaf690d1775ff238dbe62c30c7cce50c73aab))

⚡ Bolt: Optimize EPW file writing using pandas to_csv

- Merge pull request #13 from
  SustainableUrbanSystemsLab/palette-ux-number-inputs-6155559995873868698
  ([`9616433`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/9616433a673312d130a95574493c4bcb4aa364ad))

🎨 Palette: Use Number Inputs for Coordinates

- Merge pull request #14 from
  SustainableUrbanSystemsLab/palette-fix-secrets-warning-14883814781892106374
  ([`d3c82a7`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/d3c82a7d419f30c0c9425b295d70f5119a9ba063))

🎨 Palette: Remove missing secrets warning for better new user experience

- Merge pull request #15 from
  SustainableUrbanSystemsLab/bolt-performance-optimization-pandas-init-6722408013123580279
  ([`1751809`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/17518097f34846ebb5e131ed687993e931ca2215))

⚡ Bolt: [performance improvement] Optimize DataFrame construction with `.values` and `copy=False`

- Merge pull request #16 from
  SustainableUrbanSystemsLab/bolt-optimize-pandas-parsing-2486889407974271361
  ([`e9cdbc5`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/e9cdbc5047d988bb0c8cde4149053e561f3fd2d8))

⚡ Bolt: Optimize pandas CSV parsing to use native numeric types

- Merge pull request #18 from
  SustainableUrbanSystemsLab/add-epw-visualization-links-2825804845212149199
  ([`ae26e14`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/ae26e1476ebc8ea0dcac9de349247ea232a32e6f))

feat: add resources for visualizing EPW files online

- Merge pull request #19 from SustainableUrbanSystemsLab/semantic-release-setup-13068212203405167433
  ([`47d5661`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/47d5661978c62050d3fe599b3d752b92b7a79621))

chore: automate releases with python-semantic-release

- Merge pull request #20 from SustainableUrbanSystemsLab/claude/fix-build-versioning-9eDHO
  ([`9d03e52`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/9d03e529a61080a3bee850173c748d96e06f2cf3))

Remove uv dependency from release workflow and build process

- Merge pull request #3 from SustainableUrbanSystemsLab/dependabot/pip/requests-2.32.4
  ([`6d570c8`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/6d570c890aebb11f9c7c04e6e1ad1b7f471a1269))

Bump requests from 2.32.3 to 2.32.4

- Merge pull request #4 from SustainableUrbanSystemsLab/dependabot/uv/protobuf-5.29.6
  ([`dcb35ad`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/dcb35ad8bf886254794b5f82bcfd83064de50e90))

Bump protobuf from 5.29.5 to 5.29.6

- Merge pull request #5 from
  SustainableUrbanSystemsLab/feature/add-map-selection-3642529088240139114
  ([`0e36d84`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/0e36d849e7290b6a5c1720528f306a736ff24863))

Add Map Selection for Coordinates

- Merge pull request #6 from SustainableUrbanSystemsLab/feat-reverse-geocode-13847258644381804275
  ([`42cb134`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/42cb1349112ab228814ee0ef78253a92950718a0))

feat: add reverse geocoding to streamlit map

- Merge pull request #7 from SustainableUrbanSystemsLab/palette-ux-improvements-13679406432551879432
  ([`c3842ab`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/c3842abd4394a0bfc21dae2ba81fb18a485bbceb))

🎨 Palette: Add tooltips and loading states to NREL conversion form

- Merge pull request #8 from
  SustainableUrbanSystemsLab/bolt-optimize-nrel-api-call-10622319839844184435
  ([`c1fefdd`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/c1fefdd446de48418b65bd199b9efd43a9362610))

⚡ Bolt: Cache NREL API request to prevent duplicate data download

- Merge pull request #9 from
  SustainableUrbanSystemsLab/palette-refactor-download-button-15566733158072118430
  ([`4bfbb23`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/4bfbb23ee522b881dd5915c9f1b1c8610cc9ea7f))

🎨 Palette: Refactor to native Streamlit download button for better UX and Accessibility

- Minor stuff
  ([`4190bbd`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/4190bbd3f4218ac5380f718d98a1794326b67007))

- Optimize DataFrame construction in `assets.py` using NumPy `.values` array.
  ([`6869a69`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/6869a69eb9a14d49b55ac947dd9b90190dd22c9d))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- Raise exception if year not supported
  ([`8d00cc0`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/8d00cc0611d08aa9af1f24c26d4b14a70cd30a69))

.

- Readability
  ([`5c57a90`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/5c57a904c067e8de481ece277eecbcf2ffc9484b))

- Readme
  ([`7f97636`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/7f97636990f1a8d9c0f15ad7811dfbcb0230479e))

- Removed "key" in text widget
  ([`e185fcf`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/e185fcf43339ae77042d4afd4df764ac9c6e43ef))

- Ruff and uv
  ([`9e47629`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/9e47629a4591dd95e24d818f3174acfab32f4030))

- Streamlit App
  ([`430147b`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/430147b74768b0071a51a855245928bc941a4741))

- Test working
  ([`6726ee5`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/6726ee507573c318a46d42e6a79e08e31a9ba421))

- Tests pass
  ([`f6fbe5c`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/f6fbe5cd2548f8b2594513be4cf91f38e0e40882))

- Update pyproject.toml
  ([`b3dce71`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/b3dce711fa0491b6eba22cf0900862a05f238d6b))

- Update README
  ([`b9fe90d`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/b9fe90d030f3bbed30e1f13e03c1a0b24e054b54))

- Update README.md
  ([`fc66e40`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/fc66e4056faeb8e167fc2dd0a1d83ac75ab6425c))

- Update README.md
  ([`bd69405`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/bd6940528075e1e88be6f1530d3dc7efec715d89))

- Update README.md
  ([`7ed1abe`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/7ed1abecc7d4506e4ffb5afd3583609da9f150ac))

- Update README.md
  ([`a304c7b`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/a304c7b19f41684981c8df99ba69b71177c958d1))

- Update README.md
  ([`59262f9`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/59262f955c7a41ebe49d0bc2bb896c1a644213d5))

- Update README.md
  ([`6f37acd`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/6f37acd113ba8e332fab4f38d5375685e8f18f5b))

- Update README.md
  ([`ea44da1`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/ea44da172ba6fff89c604a5113ffe1ede24e6ff4))

- Update requirements.txt
  ([`8814e2f`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/8814e2f9b94d12bc8ab9fd4f8f78da218415fe99))

- Update requirements.txt
  ([`342b5ba`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/342b5ba8988a2daee44342fd4cd4ab9c413cac74))

- Update streamlit_app.py
  ([`4e7eeb7`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/4e7eeb75a17c2c7dd28abc6c81df8eea1703e411))

- Update streamlit_app.py
  ([`88af394`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/88af394325ef502a307a9907bfce88ae9c7eb685))

- Update streamlit_app.py
  ([`4f9b2af`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/4f9b2af9d9a0eab1d09ef8d4b0b425acbb3e8aeb))

- Update to next version of NREL
  ([`fc0786b`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/fc0786b37cfa2489378e6dcc91fb9d19911dc625))

### ⚡

- ⚡ Bolt: Cache NREL API request to prevent duplicate data download
  ([`22bae86`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/22bae86ce8bddd71d6af1832408e9f13b6fb91f4))

Co-authored-by: google-labs-jules[bot] <161369871+google-labs-jules[bot]@users.noreply.github.com>

- ⚡ Bolt: Optimize EPW DataFrame construction
  ([`2442dcb`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/2442dcb9121609488a39bfc1276c41a9b3cef239))

* Refactored `epw_df` creation in `nrel_psm3_2_epw/assets.py` to use a single dictionary
  initialization. This prevents repeated internal memory re-allocations and fragmentation caused by
  adding columns iteratively to an empty dataframe. * Swapped `.values.flatten()` with `.to_numpy()`
  to avoid unnecessary copying of the underlying memory buffers when extracting array data from
  pandas. * Adds a critical journal entry logging this learning to `.jules/bolt.md`.

Co-authored-by: google-labs-jules[bot] <161369871+google-labs-jules[bot]@users.noreply.github.com>

- ⚡ Bolt: Optimize EPW file writing using pandas to_csv
  ([`c7713d0`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/c7713d0ff49bc9e940a347d6af669250bc7331f5))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- ⚡ Bolt: Optimize pandas CSV parsing to use native numeric types
  ([`9adff0d`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/9adff0d96b8950aed69c3d3bc36b96da68b5f21c))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

### 🎨

- 🎨 Palette: Improve UI context and loading feedback in Streamlit app
  ([`26090c0`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/26090c0a417d97b05c9bdbebc0b8580baa4c2acf))

Co-authored-by: google-labs-jules[bot] <161369871+google-labs-jules[bot]@users.noreply.github.com>

- 🎨 Palette: Refactor to native Streamlit download button for better UX and Accessibility
  ([`c18a756`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/c18a7561f280d14309c548e7e6cb9e2dcbd23b39))

Replaced a legacy, custom-built HTML/Base64 download link generator with Streamlit's native
  `st.download_button`.

The previous implementation relied on injecting raw HTML strings with hardcoded inline CSS and
  base64 encoded payloads. It lacked proper ARIA attributes, keyboard focus indicators, and semantic
  markup, creating accessibility barriers. The new native component resolves these issues, ensures
  consistency with the app's overall theme, and significantly reduces code complexity by removing
  unused boilerplate functions and imports.

Co-authored-by: google-labs-jules[bot] <161369871+google-labs-jules[bot]@users.noreply.github.com>

- 🎨 Palette: Remove missing secrets warning for better new user experience
  ([`a272e54`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/a272e54b5e84be72719f6d1a1ec1d6565132cc40))

Prior to this commit, running the Streamlit app without an existing `.streamlit/secrets.toml` file
  triggered a jarring pink Streamlit warning trace inside the UI, creating a confusing first
  impression. By proactively checking for the file's existence before attempting to access
  `st.secrets`, the warning is gracefully suppressed.

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>

- 🎨 Palette: Replace text inputs with number inputs for Latitude and Longitude
  ([`a8bdc8d`](https://github.com/SustainableUrbanSystemsLab/NLR-PSM3-2-EPW/commit/a8bdc8dc00ba4e37c208462ebe6fb5ffa1eb91ac))

Co-authored-by: kastnerp <1919773+kastnerp@users.noreply.github.com>
