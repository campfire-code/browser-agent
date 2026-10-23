# 网页自动填表 / 采集助手（Browser Use WebUI）

> 篝火出品 · 收录于篝火 App 应用区 · 基于开源项目 [browser-use/web-ui](https://github.com/browser-use/web-ui)（MIT）

用一句话告诉 AI 要做什么（例如"打开某网页，把表格里的内容抄下来"），AI 会自己控制浏览器点击、输入、翻页，替你完成重复的填表和采集。

## 合规提示

- **只在你自己有权操作的网站和账号上使用**，并遵守网站的用户协议、robots 规则和当地法律。
- 不要用它绕过登录验证、验证码，或做批量注册、刷量、抓取他人隐私数据。
- 自动操作可能触发网站风控导致账号受限，使用后果自行承担。AI 可能点错，涉及付款、删除、提交的操作请先人工确认。

## 下载与启动

到 [Releases](https://github.com/campfire-code/browser-agent/releases/latest) 下载 `browser-agent_版本号_portable.zip`，解压到**路径里没有中文和空格**的文件夹。

- **Windows**：双击「启动（Windows 双击）.bat」。
- **Mac**：右键「启动（Mac 双击）.command」→「打开」。

第一次启动会自动安装 uv、Python 3.11、依赖和 Playwright 的 Chromium 浏览器，可选国内镜像加速。以后再启动约几秒，启动完成会自动打开网页界面 http://127.0.0.1:7788。

**首次安装的耗时与空间**（macOS Apple 芯片、宽带实测）：依赖安装约 1 分钟，下载 Chromium 约半分钟（该机器上已有大部分缓存，网络慢或在国内未选镜像时会明显更久），启动界面首次约 30 秒；占用约 **1.3 GB**（Python 依赖 .venv 约 0.8 GB，Chromium 约 0.5 GB，位于系统的 Playwright 缓存目录）。

## 前置条件

- 需要**自己的大模型接口**：软件不带模型。需要一个能做网页操作的模型（建议支持图片输入的模型），自备接口地址、密钥和模型名。
- 需要联网。无需显卡。

## 怎么用

1. 打开界面后，进入 **Agent Settings**：LLM Provider 选 **openai**（兼容 OpenAI 接口的服务，包括各类国内中转，都选这个），在 Base URL 填接口地址，API Key 填密钥，Model Name 填模型名。
2. 进入 **Browser Settings**：默认会用一个独立的浏览器；要沿用你自己浏览器里已登录的账号，可勾选 **Use Own Browser** 并填浏览器路径和用户数据目录（用之前先关闭该浏览器）。
3. 进入 **Run Agent**，在输入框用一句话写出任务，点 **Submit Task**，界面里能看到 AI 的操作过程，随时可 Stop。

**说明**
- **界面是英文**，没有中文版。
- 密钥只保存在本机。启动日志不会打印密钥。注意：在 **Load & Save Config** 页点保存配置，会把你填的设置（含密钥）以明文写进本目录 `tmp/webui_settings/`，不要把这个目录发给别人。
- 本篝火版默认关闭匿名遥测（上游只在 `.env.example` 里关）。
- 上游已在 2025 年 8 月转向新项目 VibeSurf，本工具对应上游最后的 v3.0.0 版本，依赖固定在 browser-use 0.1.48，维护较少。

## 验收用例

| 操作 | 应得到 |
|---|---|
| 双击启动，等待安装完成 | 浏览器自动打开 http://127.0.0.1:7788，显示英文界面 |
| 填好接口、密钥、模型，在 Run Agent 输入"打开 example.com，告诉我页面标题" | 弹出浏览器并打开页面，界面返回标题 Example Domain |

## 和上游的区别

- 新增本中文说明、篝火启动脚本（`campfire/`）、`tool.json` 和发布流程 `.github/workflows/release.yml`；移除了上游的构建工作流。
- `webui.py`：没有 `.env` 时默认关闭匿名遥测和 Gradio 统计；增加 `--open-browser` 参数，界面就绪后自动打开。

## 归属与许可证

上游项目 browser-use/web-ui，版权归原作者所有，按 MIT 协议分发，LICENSE 保留。篝火做的改动同样按 MIT 发布。

---

以下为上游原文。

<img src="./assets/web-ui.png" alt="Browser Use Web UI" width="full"/>

<br/>

[![GitHub stars](https://img.shields.io/github/stars/browser-use/web-ui?style=social)](https://github.com/browser-use/web-ui/stargazers)
[![Discord](https://img.shields.io/discord/1303749220842340412?color=7289DA&label=Discord&logo=discord&logoColor=white)](https://link.browser-use.com/discord)
[![Documentation](https://img.shields.io/badge/Documentation-📕-blue)](https://docs.browser-use.com)
[![WarmShao](https://img.shields.io/twitter/follow/warmshao?style=social)](https://x.com/warmshao)

This project builds upon the foundation of the [browser-use](https://github.com/browser-use/browser-use), which is designed to make websites accessible for AI agents.

We would like to officially thank [WarmShao](https://github.com/warmshao) for his contribution to this project.

**WebUI:** is built on Gradio and supports most of `browser-use` functionalities. This UI is designed to be user-friendly and enables easy interaction with the browser agent.

**Expanded LLM Support:** We've integrated support for various Large Language Models (LLMs), including: Google, OpenAI, Azure OpenAI, Anthropic, DeepSeek, Ollama etc. And we plan to add support for even more models in the future.

**Custom Browser Support:** You can use your own browser with our tool, eliminating the need to re-login to sites or deal with other authentication challenges. This feature also supports high-definition screen recording.

**Persistent Browser Sessions:** You can choose to keep the browser window open between AI tasks, allowing you to see the complete history and state of AI interactions.

<video src="https://github.com/user-attachments/assets/56bc7080-f2e3-4367-af22-6bf2245ff6cb" controls="controls">Your browser does not support playing this video!</video>

## Installation Guide

### Option 1: Local Installation

Read the [quickstart guide](https://docs.browser-use.com/quickstart#prepare-the-environment) or follow the steps below to get started.

#### Step 1: Clone the Repository
```bash
git clone https://github.com/browser-use/web-ui.git
cd web-ui
```

#### Step 2: Set Up Python Environment
We recommend using [uv](https://docs.astral.sh/uv/) for managing the Python environment.

Using uv (recommended):
```bash
uv venv --python 3.11
```

Activate the virtual environment:
- Windows (Command Prompt):
```cmd
.venv\Scripts\activate
```
- Windows (PowerShell):
```powershell
.\.venv\Scripts\Activate.ps1
```
- macOS/Linux:
```bash
source .venv/bin/activate
```

#### Step 3: Install Dependencies
Install Python packages:
```bash
uv pip install -r requirements.txt
```

Install Browsers in playwright. 
```bash
playwright install --with-deps
```
Or you can install specific browsers by running:
```bash
playwright install chromium --with-deps
```

#### Step 4: Configure Environment
1. Create a copy of the example environment file:
- Windows (Command Prompt):
```bash
copy .env.example .env
```
- macOS/Linux/Windows (PowerShell):
```bash
cp .env.example .env
```
2. Open `.env` in your preferred text editor and add your API keys and other settings

#### Step 5: Enjoy the web-ui
1.  **Run the WebUI:**
    ```bash
    python webui.py --ip 127.0.0.1 --port 7788
    ```
2. **Access the WebUI:** Open your web browser and navigate to `http://127.0.0.1:7788`.
3. **Using Your Own Browser(Optional):**
    - Set `BROWSER_PATH` to the executable path of your browser and `BROWSER_USER_DATA` to the user data directory of your browser. Leave `BROWSER_USER_DATA` empty if you want to use local user data.
      - Windows
        ```env
         BROWSER_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe"
         BROWSER_USER_DATA="C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data"
        ```
        > Note: Replace `YourUsername` with your actual Windows username for Windows systems.
      - Mac
        ```env
         BROWSER_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
         BROWSER_USER_DATA="/Users/YourUsername/Library/Application Support/Google/Chrome"
        ```
    - Close all Chrome windows
    - Open the WebUI in a non-Chrome browser, such as Firefox or Edge. This is important because the persistent browser context will use the Chrome data when running the agent.
    - Check the "Use Own Browser" option within the Browser Settings.

### Option 2: Docker Installation

#### Prerequisites
- Docker and Docker Compose installed
  - [Docker Desktop](https://www.docker.com/products/docker-desktop/) (For Windows/macOS)
  - [Docker Engine](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) (For Linux)

#### Step 1: Clone the Repository
```bash
git clone https://github.com/browser-use/web-ui.git
cd web-ui
```

#### Step 2: Configure Environment
1. Create a copy of the example environment file:
- Windows (Command Prompt):
```bash
copy .env.example .env
```
- macOS/Linux/Windows (PowerShell):
```bash
cp .env.example .env
```
2. Open `.env` in your preferred text editor and add your API keys and other settings

#### Step 3: Docker Build and Run
```bash
docker compose up --build
```
For ARM64 systems (e.g., Apple Silicon Macs), please run follow command:
```bash
TARGETPLATFORM=linux/arm64 docker compose up --build
```

#### Step 4: Enjoy the web-ui and vnc
- Web-UI: Open `http://localhost:7788` in your browser
- VNC Viewer (for watching browser interactions): Open `http://localhost:6080/vnc.html`
  - Default VNC password: "youvncpassword"
  - Can be changed by setting `VNC_PASSWORD` in your `.env` file

## Changelog
- [x] **2025/01/26:** Thanks to @vvincent1234. Now browser-use-webui can combine with DeepSeek-r1 to engage in deep thinking!
- [x] **2025/01/10:** Thanks to @casistack. Now we have Docker Setup option and also Support keep browser open between tasks.[Video tutorial demo](https://github.com/browser-use/web-ui/issues/1#issuecomment-2582511750).
- [x] **2025/01/06:** Thanks to @richard-devbot. A New and Well-Designed WebUI is released. [Video tutorial demo](https://github.com/warmshao/browser-use-webui/issues/1#issuecomment-2573393113).
