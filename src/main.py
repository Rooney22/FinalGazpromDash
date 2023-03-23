from src.app import app

from src.core.settings import settings

from routes import render_page_content

from layout.sidebar.sidebar_callbacks import toggle_collapse, toggle_classname

from src.pages.authorization.authorization_callbacks import authorize

from src.pages.methods.methods_callbacks import download_data, tab_visualization



if __name__ == '__main__':
    app.run(host=settings.host,
            port=settings.port,
            debug=settings.debug,
            dev_tools_props_check=settings.dev_tools_props_check
            )
