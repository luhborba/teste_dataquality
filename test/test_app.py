"""Arquivo de Testes da Interface Visual."""
import subprocess
import pytest
from time import sleep
from selenium import webdriver


@pytest.fixture
def driver():
    """Fixture para iniciar o webdriver."""
    process = subprocess.Popen(["streamlit", "run", "app.py"])

    driver = webdriver.Firefox()
    driver.set_page_load_timeout(10)
    yield driver

    driver.quit()
    process.kill()

def  test_app_open(driver):
    """Testa se a aplicação está abrindo."""
    driver.get("http://127.0.0.1:8501")
    sleep(3)
    
def test_app_title(driver):
    """Testa se o tiítulo da aplicação está correto."""
    driver.get("http://127.0.0.1:8501")
    sleep(3)
    assert driver.title == "Validação de CSV"