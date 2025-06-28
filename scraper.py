from playwright.async_api import async_playwright
import asyncio
import re
import os

def clean_text(raw_html):
    text = re.sub(r"\[\d+\]", "", raw_html)  
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"\s+\n", "\n", text)  
    return text.strip()

async def scrape_and_capture(url, image_path, text_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url, timeout=60000)
        await page.wait_for_selector("#mw-content-text", timeout=60000)

        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        await page.screenshot(path=image_path, full_page=True)

        content = await page.inner_text("#mw-content-text")
        cleaned = clean_text(content)

        os.makedirs(os.path.dirname(text_path), exist_ok=True)
        with open(text_path, "w", encoding="utf-8") as f:
            f.write(cleaned)

        await browser.close()
        return cleaned

def sync_scrape_and_capture(url, image_path, text_path):
    return asyncio.run(scrape_and_capture(url, image_path, text_path))
