import os
from dotenv import load_dotenv
load_dotenv()
# 篝火：没有 .env 时默认关闭匿名遥测（上游只在 .env.example 里关闭）
os.environ.setdefault("ANONYMIZED_TELEMETRY", "false")
os.environ.setdefault("GRADIO_ANALYTICS_ENABLED", "False")
import argparse
from src.webui.interface import theme_map, create_ui


def main():
    parser = argparse.ArgumentParser(description="Gradio WebUI for Browser Agent")
    parser.add_argument("--ip", type=str, default="127.0.0.1", help="IP address to bind to")
    parser.add_argument("--port", type=int, default=7788, help="Port to listen on")
    parser.add_argument("--theme", type=str, default="Ocean", choices=theme_map.keys(), help="Theme to use for the UI")
    parser.add_argument("--open-browser", action="store_true", help="Open the web UI in the default browser once ready (Campfire)")
    args = parser.parse_args()

    demo = create_ui(theme_name=args.theme)
    demo.queue().launch(server_name=args.ip, server_port=args.port, inbrowser=args.open_browser)


if __name__ == '__main__':
    main()
