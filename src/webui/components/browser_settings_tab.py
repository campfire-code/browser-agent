import os
from distutils.util import strtobool
import gradio as gr
import logging
from gradio.components import Component

from src.webui.webui_manager import WebuiManager
from src.utils import config

logger = logging.getLogger(__name__)

async def close_browser(webui_manager: WebuiManager):
    """
    Close browser
    """
    if webui_manager.bu_current_task and not webui_manager.bu_current_task.done():
        webui_manager.bu_current_task.cancel()
        webui_manager.bu_current_task = None

    if webui_manager.bu_browser_context:
        logger.info("⚠️ Closing browser context when changing browser config.")
        await webui_manager.bu_browser_context.close()
        webui_manager.bu_browser_context = None

    if webui_manager.bu_browser:
        logger.info("⚠️ Closing browser when changing browser config.")
        await webui_manager.bu_browser.close()
        webui_manager.bu_browser = None

def create_browser_settings_tab(webui_manager: WebuiManager):
    """
    Creates a browser settings tab.
    """
    input_components = set(webui_manager.get_components())
    tab_components = {}

    with gr.Group():
        with gr.Row():
            browser_binary_path = gr.Textbox(
                label="浏览器程序路径",
                lines=1,
                interactive=True,
                placeholder="例如：/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome"
            )
            browser_user_data_dir = gr.Textbox(
                label="浏览器用户数据目录",
                lines=1,
                interactive=True,
                placeholder="使用默认用户数据时留空",
            )
    with gr.Group():
        with gr.Row():
            use_own_browser = gr.Checkbox(
                label="使用自己的浏览器",
                value=bool(strtobool(os.getenv("USE_OWN_BROWSER", "false"))),
                info="沿用你已经打开、已登录的浏览器（使用前请先关闭它）",
                interactive=True
            )
            keep_browser_open = gr.Checkbox(
                label="任务结束后保持浏览器打开",
                value=bool(strtobool(os.getenv("KEEP_BROWSER_OPEN", "true"))),
                info="连续执行多个任务时不关闭浏览器",
                interactive=True
            )
            headless = gr.Checkbox(
                label="无界面模式",
                value=False,
                info="浏览器在后台运行，不显示窗口",
                interactive=True
            )
            disable_security = gr.Checkbox(
                label="关闭浏览器安全限制",
                value=False,
                info="仅在确有需要时开启，会降低安全性",
                interactive=True
            )

    with gr.Group():
        with gr.Row():
            window_w = gr.Number(
                label="窗口宽度",
                value=1280,
                info="浏览器窗口宽度（像素）",
                interactive=True
            )
            window_h = gr.Number(
                label="窗口高度",
                value=1100,
                info="浏览器窗口高度（像素）",
                interactive=True
            )
    with gr.Group():
        with gr.Row():
            cdp_url = gr.Textbox(
                label="远程调试地址（CDP）",
                value=os.getenv("BROWSER_CDP", None),
                info="用于连接浏览器远程调试的地址",
                interactive=True,
            )
            wss_url = gr.Textbox(
                label="远程调试地址（WSS）",
                info="用于连接浏览器远程调试的 WebSocket 地址",
                interactive=True,
            )
    with gr.Group():
        with gr.Row():
            save_recording_path = gr.Textbox(
                label="录屏保存路径",
                placeholder="例如：./tmp/record_videos",
                info="浏览器录屏的保存位置",
                interactive=True,
            )

            save_trace_path = gr.Textbox(
                label="运行轨迹保存路径",
                placeholder="例如：./tmp/traces",
                info="助手运行轨迹的保存位置",
                interactive=True,
            )

        with gr.Row():
            save_agent_history_path = gr.Textbox(
                label="执行记录保存路径",
                value="./tmp/agent_history",
                info="助手执行记录的保存目录",
                interactive=True,
            )
            save_download_path = gr.Textbox(
                label="浏览器下载文件保存目录",
                value="./tmp/downloads",
                info="浏览器下载的文件保存到这个目录",
                interactive=True,
            )
    tab_components.update(
        dict(
            browser_binary_path=browser_binary_path,
            browser_user_data_dir=browser_user_data_dir,
            use_own_browser=use_own_browser,
            keep_browser_open=keep_browser_open,
            headless=headless,
            disable_security=disable_security,
            save_recording_path=save_recording_path,
            save_trace_path=save_trace_path,
            save_agent_history_path=save_agent_history_path,
            save_download_path=save_download_path,
            cdp_url=cdp_url,
            wss_url=wss_url,
            window_h=window_h,
            window_w=window_w,
        )
    )
    webui_manager.add_components("browser_settings", tab_components)

    async def close_wrapper():
        """Wrapper for handle_clear."""
        await close_browser(webui_manager)

    headless.change(close_wrapper)
    keep_browser_open.change(close_wrapper)
    disable_security.change(close_wrapper)
    use_own_browser.change(close_wrapper)
