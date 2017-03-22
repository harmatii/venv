import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def testStickers(driver):
    driver.get("http://localhost/litecart/en/")
    stickerred = [driver.find_element_by_xpath("//a[@title='Red Duck']//div[@class='sticker new']")]
    assert len(stickerred) == 1
    stickergreen = [driver.find_element_by_xpath("//a[@title='Green Duck']//div[@class='sticker new']")]
    assert len(stickergreen) == 1
    stickerpurple = [driver.find_element_by_xpath("//a[@title='Purple Duck']//div[@class='sticker new']")]
    assert len(stickerpurple) == 1
    stickerblue = [driver.find_element_by_xpath("//a[@title='Blue Duck']//div[@class='sticker new']")]
    assert len(stickerblue) == 1
    stickeryellow = [driver.find_element_by_xpath("//a[@title='Yellow Duck']//div[@class='sticker sale']")]
    assert len(stickeryellow) == 1