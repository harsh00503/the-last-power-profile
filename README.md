# The Last Power Profile

An Avatar: The Last Airbender themed Linux desktop companion that reacts to changes in your system's power profile.

## Features

- Detects power profile changes.
- Displays animated desktop overlays featuring Aang.
- Different appearances for Performance, Balanced and Power Saver modes.
- Runs in the background using systemd.
- Automatically restarts if it crashes.
- Starts automatically on login when enabled.

## Preview

*Screenshots and GIF demonstrations coming soon.*

## Installation

Download the latest `.deb` package from [GitHub Releases](../../releases).

Install:

```bash
sudo apt install ./the-last-power-profile_0.1.0_amd64.deb
```

Enable automatic startup:

```bash
the-last-power-profile enable
```

## Usage

```bash
the-last-power-profile start
the-last-power-profile stop
the-last-power-profile restart
the-last-power-profile status
the-last-power-profile enable
the-last-power-profile disable
```

View logs:

```bash
journalctl --user -u the-last-power-profile.service -f
```

## Requirements

- Ubuntu / Debian (amd64)
- systemd
- power-profiles-daemon
- GNOME (initial target environment)

## Development

Clone the repository:

```bash
git clone https://github.com/harsh00503/the-last-power-profile.git
cd the-last-power-profile
```

Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run:

```bash
python3 src/main.py
```

## Packaging

The application uses PyInstaller to create a standalone executable and `dpkg-deb` to build Debian packages.

## License

MIT License. See [LICENSE](LICENSE).