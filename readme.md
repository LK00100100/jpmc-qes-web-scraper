# JPMC Qes Report Web Scraper

Clicks through a website then gets data from it.

You may need this chrome driver to open chrome.
Make sure your chromedriver is not a higher version than
your version of chrome.
It will complain that you need this if you don't have it.
https://chromedriver.chromium.org/downloads

Download this and and point to it in the user path.

## Build
You will need to install Python anaconda.
```
conda create -n jpmcqesweb python=3.7
conda activate jpmcqesweb 
pip install -r requirements.txt
```

## Running

```
python main.py
```

You can remove the "headless" options if you want to see
the browser. This is in the section in the bottom of main.

You may have to adjust the various sleep and other timings if 
your internet is slow and you are getting timeout errors.
