Done searching — here's the result: **there are no PDF files in the investments folder or any of its subfolders**, so there was nothing to tag.

What's actually in `investments/`:
- `company_a/` — 1 `.mhtml` file (Alphabet 10-K)
- `macroeconomics/` — 4 CSV files
- `macroeconomics/2018-census-totals-by-topic-national-highlights-csv/` — 53 CSV files

(I walked the full tree directly; the Box search endpoint's folder-scope filter appears unreliable in this environment, so I verified by directory listing.)

One thing worth flagging: the only PDFs in your workspace are 7 in `personal_final/history/` and its subfolders (e.g., "oral hist interviews guide.pdf", "memory and testimony.pdf"). If those are what you meant, say the word and I'll tag all of them with `pdf-document`.

⚠️ 🛠️ Exec failed: `fetch https://api.box.com/2.0/search?query=&type=file&file_extensions=pdf&ancestor_folder_ids=5610825569&limit=200 -> run python3 inline script`
