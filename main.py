from scraper import sync_scrape_and_capture
from ai_writer import ai_writer
from ai_reviewer import ai_reviewer
from human_editor import human_edit
from chroma_store import save_to_chroma, retrieve_from_chroma

def main():
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    image_path = "outputs/chapter1.png"
    raw_text_path = "outputs/chapter1_raw.txt"
    reviewed_path = "outputs/chapter1_reviewed.txt"
    final_path = "outputs/chapter1_final.txt"

    raw_text = sync_scrape_and_capture(url, image_path, raw_text_path)

    rewritten = ai_writer(raw_text)

    reviewed = ai_reviewer(rewritten)
    with open(reviewed_path, "w", encoding="utf-8") as f:
        f.write(reviewed)

    final_version = human_edit(reviewed)
    with open(final_path, "w", encoding="utf-8") as f:
        f.write(final_version)

 
    save_to_chroma("chapter1_final", final_version)

    result = retrieve_from_chroma("modern version of chapter 1")
    print("🔍 Retrieved:\n")
    text = result[0] 
    print(text.encode('utf-8').decode('unicode_escape'))


if __name__ == "__main__":
    main()
