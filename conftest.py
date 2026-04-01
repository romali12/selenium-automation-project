import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOpts
from selenium.webdriver.firefox.options import Options as FxOpts
from selenium.webdriver.edge.options import Options as EdgeOpts

# ---- tweak this list to add/remove browsers ------------------
BROWSERS = ["chrome", "firefox", "edge"]
# --------------------------------------------------------------

def _create_local_driver(name: str):
    if name == "chrome":
        return webdriver.Chrome(options=ChromeOpts())
    if name == "firefox":
        return webdriver.Firefox(options=FxOpts())
    if name == "edge":
        return webdriver.Edge(options=EdgeOpts())
    raise ValueError(f"Unsupported browser: {name}")

def _create_remote_driver(name: str):
    grid = "http://localhost:4444/wd/hub"   # change if using a cloud grid
    if name == "chrome":
        return webdriver.Remote(command_executor=grid,
                                options=ChromeOpts())
    if name == "firefox":
        return webdriver.Remote(command_executor=grid,
                                options=FxOpts())
    if name == "edge":
        return webdriver.Remote(command_executor=grid,
                                options=EdgeOpts())
    return None


@pytest.fixture(params=BROWSERS)
def driver(request):
    """Creates a WebDriver for each browser in BROWSERS."""
    use_grid = request.config.getoption("--grid")
    create = _create_remote_driver if use_grid else _create_local_driver
    drv = create(request.param)
    drv.maximize_window()
    yield drv
    drv.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--grid", action="store_true", default=False,
        help="Run on Selenium Grid instead of locally"
    )
