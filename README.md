# Literature Search Automation

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install selenium.

```bash
pip3 install selenium
```

WebDriver installation:

```bash
https://sites.google.com/a/chromium.org/chromedriver/downloads
```

## Usage

```python
from selenium import webdriver

browser = webdriver.Chrome("/Desktop/chromedriver")

browser.get("https://...")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

