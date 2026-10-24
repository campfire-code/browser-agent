import gradio as gr

from src.webui.webui_manager import WebuiManager
from src.webui.components.agent_settings_tab import create_agent_settings_tab
from src.webui.components.browser_settings_tab import create_browser_settings_tab
from src.webui.components.browser_use_agent_tab import create_browser_use_agent_tab
from src.webui.components.deep_research_agent_tab import create_deep_research_agent_tab
from src.webui.components.load_save_config_tab import create_load_save_config_tab

theme_map = {
    "Default": gr.themes.Default(),
    "Soft": gr.themes.Soft(),
    "Monochrome": gr.themes.Monochrome(),
    "Glass": gr.themes.Glass(),
    "Origin": gr.themes.Origin(),
    "Citrus": gr.themes.Citrus(),
    "Ocean": gr.themes.Ocean(),
    "Base": gr.themes.Base()
}


def create_ui(theme_name="Ocean"):
    css = """
    .gradio-container {
        width: 70vw !important; 
        max-width: 70% !important; 
        margin-left: auto !important;
        margin-right: auto !important;
        padding-top: 10px !important;
    }
    .header-text {
        text-align: center;
        margin-bottom: 20px;
    }
    .tab-header-text {
        text-align: center;
    }
    /* 篝火：隐藏 Gradio 页脚里的英文链接（通过 API 使用、设置、Built with Gradio） */
    footer {
        display: none !important;
    }
    .theme-section {
        margin-bottom: 10px;
        padding: 15px;
        border-radius: 10px;
    }
    """

    # dark mode in default
    js_func = """
    function refresh() {
        // 篝火：把 Gradio 自带的英文提示换成中文
        const zh = {
            "Drop File Here": "拖放文件到这里",
            "Drop Image Here": "拖放图片到这里",
            "Click to Upload": "点击上传",
            "- or -": "或",
            "Upload": "上传"
        };
        const translate = (root) => {
            const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
            let n;
            while ((n = walker.nextNode())) {
                const t = n.nodeValue.trim();
                if (zh[t]) n.nodeValue = n.nodeValue.replace(t, zh[t]);
                else if (/^[-\u2013\u2014\s]*or[-\u2013\u2014\s]*$/i.test(t)) n.nodeValue = "或";
            }
        };
        new MutationObserver(() => translate(document.body)).observe(document.body, {childList: true, subtree: true});
        translate(document.body);

        const url = new URL(window.location);

        if (url.searchParams.get('__theme') !== 'dark') {
            url.searchParams.set('__theme', 'dark');
            window.location.href = url.href;
        }
    }
    """

    ui_manager = WebuiManager()

    with gr.Blocks(
            title="网页自动化助手", theme=theme_map[theme_name], css=css, js=js_func,
    ) as demo:
        with gr.Row():
            gr.Markdown(
                """
                # 🌐 网页自动化助手
                ### 用 AI 帮你操作浏览器
                """,
                elem_classes=["header-text"],
            )

        with gr.Tabs() as tabs:
            with gr.TabItem("⚙️ 模型设置"):
                create_agent_settings_tab(ui_manager)

            with gr.TabItem("🌐 浏览器设置"):
                create_browser_settings_tab(ui_manager)

            with gr.TabItem("🤖 运行任务"):
                create_browser_use_agent_tab(ui_manager)

            with gr.TabItem("🎁 更多助手"):
                gr.Markdown(
                    """
                    ### 基于浏览器自动化的助手
                    """,
                    elem_classes=["tab-header-text"],
                )
                with gr.Tabs():
                    with gr.TabItem("深度研究"):
                        create_deep_research_agent_tab(ui_manager)

            with gr.TabItem("📁 加载与保存设置"):
                create_load_save_config_tab(ui_manager)

    return demo
