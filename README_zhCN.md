# 🆎 魔兽世界字体工具

通过修改字体来提升《魔兽世界》的游戏体验。

简体中文 | [English](README.md)

<details>
<summary>📖 目录</summary>

- [💼 运行要求](#-%E8%BF%90%E8%A1%8C%E8%A6%81%E6%B1%82)
- [🚚 安装](#-%E5%AE%89%E8%A3%85)
- [🐍 Python 脚本](#-python-%E8%84%9A%E6%9C%AC)
  - [🀄 `chinese.py`](#-chinesepy)
    - [修改 1: 优化中文点号](#%E4%BF%AE%E6%94%B9-1-%E4%BC%98%E5%8C%96%E4%B8%AD%E6%96%87%E7%82%B9%E5%8F%B7)
    - [修改 2: 丶替换为点号（用于角色扮演）](#%E4%BF%AE%E6%94%B9-2-%E4%B8%B6%E6%9B%BF%E6%8D%A2%E4%B8%BA%E7%82%B9%E5%8F%B7%E7%94%A8%E4%BA%8E%E8%A7%92%E8%89%B2%E6%89%AE%E6%BC%94)
    - [修改 3: 强制使用方引号](#%E4%BF%AE%E6%94%B9-3-%E5%BC%BA%E5%88%B6%E4%BD%BF%E7%94%A8%E6%96%B9%E5%BC%95%E5%8F%B7)
    - [使用方法](#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95)
    - [范例](#%E8%8C%83%E4%BE%8B)
- [💻 批处理脚本](#-%E6%89%B9%E5%A4%84%E7%90%86%E8%84%9A%E6%9C%AC)
  - [`fonts_zhtw.bat`](#fonts_zhtwbat)

</details>

## 💼 运行要求

- Python 3.12 或更高版本
- Windows 操作系统（用于运行批处理脚本）

## 🚚 安装

1. 将此 Git 项目克隆到本地计算机。
2. 通过下面的命令来安装所需的 Python 包：

   ```bash
   pip install -r requirements.txt
   ```

## 🐍 Python 脚本

### 🀄 `chinese.py`

这个脚本可以修改字体文件中的特定中文字符，以提升游戏体验。

#### 修改 1: 优化中文点号

使用更适合的字符替换名字中的点号。

替换优先级：日文片假名中点（U+30FB）> 简体中文中点（U+00B7）> 繁体中文中点（U+2022）

#### 修改 2: 丶替换为点号（用于角色扮演）

因为许多国服玩家习惯在名字中使用 `丶` 作为点号来分割姓名，此功能可以替换字符 `丶` 为更合适的点号字符。

替换优先级：日文片假名中点（U+30FB）> 简体中文中点（U+00B7）> 繁体中文中点（U+2022）

#### 修改 3: 强制使用方引号

强制在引号中使用方括号，提升游戏内的可读性（类似于知乎的文本格式）。

#### 使用方法

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

#### 范例

```bash
python chinese_font_tools.py -f "input.ttf" --better-chinese-dot --zhu-to-dot --enforce-corner-brackets
```

<details>
<summary>转换文件夹中的所有字体</summary>

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

## 💻 批处理脚本

### `fonts_zhtw.bat`

这个脚本会将你选择的字体使用《魔兽世界》繁体中文客户端所需的特定名称复制多份。

使用方法：

1. 将脚本复制到 `_retail_\Fonts` 文件夹中。
2. 将你想要的字体文件拖放到脚本上。
3. 脚本会创建带有所需名称的字体文件副本。
