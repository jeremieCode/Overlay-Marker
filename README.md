# Overlay Marker

A fullscreen visual overlay tool for annotating any application in real time.

## Description

The program creates a transparent fullscreen layer that allows placement of sequentially numbered markers.

Use cases:

* Marking points of interest on screen captures
* Annotating live presentations
* Identifying specific interface regions
* Creating temporary visual references

## Requirements

* Python 3.12
* Linux (tested on Ubuntu/Debian)
* `sudo` privileges (required for system-level keyboard capture)

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install PyQt5 pynput keyboard evdev
```

## Execution

```bash
sudo ./venv/bin/python3 main.py
```

## Controls

* **Right click**: Add a numbered marker at cursor position
* **F9**: Toggle foreground/background mode
* **Space**: Clear all markers (foreground mode only)
* **Esc**: Exit

## Operating Modes

### Foreground mode (default)

* Semi-transparent blue overlay
* Mouse events intercepted
* Marker placement enabled

### Background mode

* Semi-transparent red overlay
* Events passed to underlying applications
* Markers remain visible

## Dependencies

* PyQt5: GUI and rendering
* pynput: Mouse event capture
* keyboard: System-level keyboard capture
* evdev: Linux input device interface
