# Tavro setup diagnosis · 18 November 2026

Windows 11 25H2, Snapdragon X, 16 GB RAM. The browser and API are running. The browser download reached a server using NVIDIA NIM. Memory failed independently because the serving Python environment lacks the native extension. This pass left source, settings, packages and running services unchanged. No model was downloaded and no chat prompt was sent.

## PROJECT REQUIREMENTS

| Status | Requirement | Evidence on this machine |
|---|---|---|
| Present | Source checkout, Python and web tooling | The API listener on port 8000 was PID 15840. Its parent launched `venv\runtime\Scripts\python.exe` from the inner project directory. This is Microsoft Store CPython **3.12.10**, `win-amd64`, under x64 emulation. FastAPI and Uvicorn are installed. Git, uv 0.13.7, Node 24.22.1 and npm 11.19.1 are available. The frontend requires Node 22.22+ and npm 11.19.x or newer within major 11. See `pyproject.toml:14` and `frontend/package.json:6`. |
| Present | Local engine preference | `%USERPROFILE%\.tavro\config.toml` specifies `[engine] default = "ollama"` and `[intelligence] default_model = "qwen3.5:4b"`. This is also the desktop model the repository tests for 16 GB. See `frontend/src-tauri/src/lib.rs:3707`. |
| Missing | Runnable local Ollama and a model in its default store | The checkout’s `frontend/src-tauri/binaries` contains only `.gitignore`. Its ARM64 executable and `lib/ollama` runner are absent. No executable was found on PATH or in the usual install locations, no Ollama install registration was found, and `127.0.0.1:11434/api/tags` refused the connection. The default Ollama model directory is absent. There was no binary to version-test. See `frontend/src-tauri/src/lib.rs:193` and `frontend/src-tauri/scripts/download-ollama.sh:95`. |
| Present / missing | Native memory build tools | Visual Studio 2022 Build Tools, an x64 MSVC linker, Windows SDK and ARM64-hosted stable Rust are installed. The x64 Rust target is **missing**, the installed compiler is **blocked**, and `tavro_rust` is **missing** from the API environment. Maturin is declared as the package’s isolated build backend. See `rust/crates/tavro-python/pyproject.toml:1` and `pyproject.toml:317`. |
| Unverified | Model download and inference | About 306 GiB was free on the project drive. Registry access, an actual model transfer, chat generation and Snapdragon acceleration were not exercised. |

**Optional cloud features.** No cloud credential is required for local Ollama. The active NIM engine used its hosted default, and `NIM_API_KEY` was absent from the server process. NIM’s readiness check can succeed on its model-list endpoint. Authenticated generation remains unverified. Other providers have separate credentials and optional client packages. See `src/tavro/engine/nim.py:31`, `src/tavro/engine/nim.py:257` and `pyproject.toml:59`.

## CONFIRMED ERRORS

**1. Download → HTTP 501.** The existing server log records `POST /v1/models/pull HTTP/1.1` → `501 Not Implemented`. The route returns `Model pulling is only supported with the Ollama engine`. Three observations explain the mismatch.

- **What Settings displays.** The browser initializes the dropdown to Ollama, and its source getter returns `{ kind: 'ollama' }` unconditionally. Browser Save raises `Inference source is configurable in the desktop app only.` The Tauri desktop app instead calls Rust to save the choice in `~/.tavro/inference.json`, stores a custom key separately in secure storage, and applies the choice on the next launch. That JSON file is absent here. Desktop Ollama startup launches the sidecar and passes `--engine ollama --model <tag>` to the API. See `frontend/src/pages/SettingsPage.tsx:337`, `frontend/src/lib/api.ts:1191` and `frontend/src-tauri/src/lib.rs:129`, `:2460`, `:2569`.
- **What the API selected.** The running command was `-m tavro.cli serve --host 127.0.0.1 --port 8000`, with no engine or model argument. `--engine` (`-e`) explicitly selects the primary engine and fails if it is unavailable. Otherwise the backend tries `[engine].default`, then discovers healthy alternatives. `TAVRO_CONFIG` can select another TOML file and was unset here. Deployment examples mention `TAVRO_ENGINE_DEFAULT`, but the Python startup path does not read it. `OLLAMA_HOST` concerns the endpoint address. The log says `Default engine 'ollama' is unavailable; using 'nim'` and `Configured model 'qwen3.5:4b' is not reachable; using 'bigcode/starcoder2-15b'.` See `src/tavro/core/config.py:2074`, `src/tavro/engine/_discovery.py:201`, `src/tavro/cli/serve.py:84`, `:127`, `:194` and `src/tavro/engine/ollama.py:124`.
- **Where the request went.** Both `127.0.0.1:5173/v1/info` and `127.0.0.1:8000/v1/info` returned `nim / bigcode/starcoder2-15b / orchestrator`. Vite’s live proxy target was `http://127.0.0.1:8000` and its `VITE_API_URL` was unset. A saved browser **Settings → API URL** takes precedence over the build-time URL and same-origin proxy. The local API log independently confirms the failing request reached it. Browser Download goes through that API. Tauri Download calls Ollama through Rust. See `frontend/src/lib/api.ts:72`, `:201`, `:272`, `frontend/vite.config.ts:12` and `src/tavro/server/routes.py:1151`.

**2. Memory → HTTP 503.** A live `GET /v1/memory/stats` through port 5173 returned `503` with the detail below. A fresh process using the serving interpreter returned `RUST_AVAILABLE False` and `ModuleNotFoundError: No module named 'tavro_rust'`. SQLite memory requires that module. This environment was installed with the `desktop` extra alone. The local Rust package belongs to the separate `desktop-native` group. The same missing import also prevented rate-limiter initialization in the server log. See `src/tavro/_rust_bridge.py:30`, `src/tavro/tools/storage/sqlite.py:47`, `src/tavro/server/api_routes.py:207`, `:273` and `pyproject.toml:243`, `:317`.

```text
Memory backend unavailable: the native `tavro_rust` extension is not installed in this environment. Build it into the venv that runs the server with `uv run maturin develop -m rust/crates/tavro-python/Cargo.toml` (needs rustc >= 1.88), then restart. Verify with `python -c "from tavro._rust_bridge import RUST_AVAILABLE; print(RUST_AVAILABLE)"`.
```

**3. Native build prerequisite → compiler cannot start.** `rustup run stable rustc --version` exited with `0xC0E90002`. Windows Code Integrity events 3033 and 3077 identify `rustc_driver-150645f85b42168b.dll` and say it “did not meet the Enterprise signing level requirements”. The installed stable manifest identifies Rust 1.99.1. Only `aarch64-pc-windows-msvc` is installed as a target. The workspace declares **Rust 1.89**, newer than the 1.88 in the HTTP error. The documented Windows ARM64 path uses an ARM64 desktop/Ollama and an **x64 CPython 3.12 extension** because several locked Python dependencies lack native ARM64 wheels. See `rust/Cargo.toml:23`, `docs/getting-started/windows-native.md:15` and `.github/workflows/desktop.yml:73`.

**Checks completed.** 39 focused Python tests and 14 frontend tests passed, covering discovery, model selection, model management, missing memory support, ARM64 executable-header validation, inference setup and memory UI handling. The Python tests reused pytest from the checkout’s separate `.venv` with the serving interpreter and isolated test data. The full suite and native compilation were outside this read-only pass. A separate in-memory check reproduced the pull route’s 501 with an Ollama child wrapped in `MultiEngine`.

## FIX IN ORDER

These steps are for a later repair. Run PowerShell from the inner `tavro-main` directory containing `pyproject.toml`.

**1. Make local Ollama available.** Install and open **Ollama for Windows** using the Windows installer referenced by `deploy/windows/install.ps1:410`. In a new PowerShell, run the following. If the tags request refuses the connection, run `ollama serve` in a separate PowerShell and retry it. The pull is the step that downloads the configured model, roughly 3.4 GB by the project’s estimate. [Ollama Windows instructions](https://docs.ollama.com/windows)

```powershell
ollama --version
Invoke-RestMethod http://127.0.0.1:11434/api/tags
ollama pull qwen3.5:4b
ollama list
```

**2. Select Ollama for the existing API.** Once `ollama list` contains `qwen3.5:4b`, restart the API explicitly with the same Python. After startup, refresh Settings and send a short chat to `qwen3.5:4b`.

```powershell
$py = (Resolve-Path .\venv\runtime\Scripts\python.exe).Path
& $py -m tavro.cli stop
& $py -m tavro.cli start --host 127.0.0.1 --port 8000 --engine ollama --model qwen3.5:4b
Invoke-RestMethod http://127.0.0.1:5173/v1/info
```

With Ollama alone, expect `ollama / qwen3.5:4b` and the browser Download route will accept pulls. If NIM is still reachable, this revision can wrap both engines as `multi` even with `--engine ollama`. The browser pull guard rejects the wrapper. Use `ollama pull <tag>` for subsequent downloads in that case. To support the button in multi-engine mode, the project would need to resolve the Ollama child in the pull handler. See `src/tavro/cli/serve.py:266` and `src/tavro/server/routes.py:1159`.

**3. Restore native memory.** Have the device administrator provide a policy-approved stable Rust toolchain or approve the identified compiler component. Verify `rustup run stable rustc --version` prints **1.89 or later**. Once it succeeds, add the x64 target and build the repository’s native group into the serving environment. The explicit environment path avoids updating the separate `.venv`. Copy mode accommodates this OneDrive checkout.

```powershell
$py = (Resolve-Path .\venv\runtime\Scripts\python.exe).Path
$env:UV_PROJECT_ENVIRONMENT = (Resolve-Path .\venv\runtime).Path
$env:RUSTUP_TOOLCHAIN = 'stable'
$env:CARGO_BUILD_TARGET = 'x86_64-pc-windows-msvc'
$env:PYO3_CROSS_PYTHON_VERSION = '3.12'
$env:PYO3_CROSS_PYTHON_IMPLEMENTATION = 'CPython'
rustup target add --toolchain stable x86_64-pc-windows-msvc
uv sync --locked --inexact --no-dev --extra desktop --group desktop-native --python $py --link-mode copy
& $py -B -c "import sysconfig, tavro_rust; from tavro._rust_bridge import RUST_AVAILABLE; print(sysconfig.get_platform(), RUST_AVAILABLE)"
```

Expect `win-amd64 True`. Repeat the explicit stop/start commands in step 2 and run `Invoke-RestMethod http://127.0.0.1:5173/v1/memory/stats`. Success is HTTP 200 with `backend` equal to `sqlite` and an entry count. Zero entries is a valid result.

## NEED FROM ME

Nothing further to diagnose the two reported errors. The remaining dependency for a local memory build is a Rust compiler that the device’s application-control policy permits.
