# 🆎 Font Tools for WoW

Enhance your World of Warcraft gaming experience by modifying fonts.

[简体中文](README_zhCN.md) | English

<details>
<summary>📖 Table of Contents</summary>

- [💼 Requirements](#-requirements)
- [🚚 Installation](#-installation)
- [🐍 Python Scripts](#-python-scripts)
  - [🀄 `chinese.py`](#-chinesepy)
    - [MOD 1: Improved Chinese Dot](#mod-1-improved-chinese-dot)
    - [MOD 2: Zhu to Dot (For Role-playing)](#mod-2-zhu-to-dot-for-role-playing)
    - [MOD 3: Enforce Corner Brackets](#mod-3-enforce-corner-brackets)
    - [Usage](#usage)
    - [Example](#example)
- [💻 Batch Scripts](#-batch-scripts)
  - [`fonts_zhtw.bat`](#fonts_zhtwbat)

</details>

## 💼 Requirements

- Python 3.12 or later
- Windows OS (for Batch Scripts)

## 🚚 Installation

1. Clone this repository to your local machine.
2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## 🐍 Python Scripts

### 🀄 `chinese.py`

This script modifies specific Chinese characters in font files to improve the in-game experience.

#### MOD 1: Improved Chinese Dot

Replaces the dot character used in names with a more suitable alternative.

Priority: Japanese Katakana Middle Dot (U+30FB) > Simplified Chinese Middle Dot (U+00B7) > Traditional Chinese Middle Dot (U+2022)

#### MOD 2: Zhu to Dot (For Role-playing)

Replaces the character `丶` with a more appropriate dot character, as many Chinese players use `丶` as a dot in their names.

Priority: Japanese Katakana Middle Dot (U+30FB) > Simplified Chinese Middle Dot (U+00B7) > Traditional Chinese Middle Dot (U+2022)

#### MOD 3: Enforce Corner Brackets

Forces the use of corner brackets for quotes, improving readability in-game (similar to text formatting on Zhihu).

#### Usage

```text
usage: chinese.py [-h] -f FONT [-o OUTPUT] [--better-chinese-dot] [--zhu-to-dot] [--enforce-corner-brackets] [--font-name FONT_NAME] [--force-output]

Modify the Chinese font file for better WoW game experience.

options:
  -h, --help            show this help message and exit
  -f FONT, --font FONT  Path to the input font file
  -o OUTPUT, --output OUTPUT
                        Path to the output font file
  --better-chinese-dot  Replace '‧' with '·' in the font
  --zhu-to-dot          Replace '丶' with '·' in the font
  --enforce-corner-brackets
                        Enforce corner brackets for quotes
  --font-name FONT_NAME
                        Template for the new font name. Use $NAME$ for the original name. Default: '$NAME$ WindModified'
  --force-output        Overwrite existing output file
```

#### Example

```bash
python chinese_font_tools.py -f "input.ttf" --better-chinese-dot --zhu-to-dot --enforce-corner-brackets
```

<details>
<summary>Convert all fonts in a folder</summary>

```cmd
@echo off
setlocal enabledelayedexpansion
call .venv\Scripts\activate.bat
set "SOURCE_DIR=E:\Blizzard\World of Warcraft\Development\Font Source"
set "DEST_DIR=E:\Blizzard\World of Warcraft\_retail_\Interface\Addons\WindMedia\Font"

for /R "%SOURCE_DIR%" %%F in (*.ttf *.otf) do (
    set "RELATIVE_PATH=%%~dpF"
    set "RELATIVE_PATH=!RELATIVE_PATH:%SOURCE_DIR%=!"
    set "OUTPUT_DIR=%DEST_DIR%!RELATIVE_PATH!"
    if not exist "!OUTPUT_DIR!" mkdir "!OUTPUT_DIR!"
    set "OUTPUT_FILE=!OUTPUT_DIR!%%~nxF"
    echo Processing: %%F
    echo Output to: !OUTPUT_FILE!
    python chinese.py ^
    -f "%%F" ^
    -o "!OUTPUT_FILE!" ^
    --better-chinese-dot ^
    --zhu-to-dot ^
    --enforce-corner-brackets ^
    --font-name "$NAME$ Wind Edition" ^
    --force-output
)

echo All fonts processed.
pause
```

</details>

## 💻 Batch Scripts

### `fonts_zhtw.bat`

This script copies your chosen font with specific names required by World of Warcraft.

To use:

1. Copy the script to the `_retail_\Fonts` folder.
2. Drag and drop your desired font file onto the script.
3. The script will create copies of the font file with the required names.
