"""Standalone Tkinter GUI for the mini Information Retrieval project."""
from pathlib import Path
import tkinter as tk
from tkinter import ttk

from inverted_index import build_index
from query_processor import search
from wildcard_processor import wildcard_search


class SearchGUI:
    BG = "#f3f5f1"
    CARD = "#ffffff"
    INK = "#15221d"
    TEAL = "#07675d"
    MUTED = "#5f7068"

    TOPICS = [
        ("Westlaw", "A legal-search example showing why Boolean queries are useful.", "westlaw boolean"),
        ("Dictionary", "A vocabulary list of all terms in the lecture collection.", "dictionary"),
        ("Postings", "The document IDs stored for each dictionary term.", "postings"),
        ("Case folding", "Changes Search and search into the same lowercase form.", "normalization"),
        ("Positional index", "Stores term positions to support phrase searching.", "positional indexes"),
        ("Wildcard", "An asterisk expands a partial term, such as index*.", "index*"),
        ("Edit distance", "Counts insert, delete, and replace operations.", "edit distance"),
        ("Soundex", "Matches names that sound alike but may spell differently.", "soundex"),
    ]

    def __init__(self):
        corpus = Path(__file__).parent / "data" / "lecture_corpus"
        self.documents, self.index = build_index(str(corpus))
        self.root = tk.Tk()
        self.root.title("IR Lecture Search — Desktop GUI")
        self.root.geometry("1200x800")
        self.root.minsize(950, 650)
        self.root.configure(bg=self.BG)
        self._styles()
        self._layout()

    def _styles(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TFrame", background=self.BG)
        style.configure("Card.TFrame", background=self.CARD)
        style.configure("Title.TLabel", background=self.BG, foreground=self.INK, font=("Georgia", 30, "bold"))
        style.configure("Text.TLabel", background=self.BG, foreground=self.MUTED, font=("Segoe UI", 10))
        style.configure("Kicker.TLabel", background=self.BG, foreground=self.TEAL, font=("Consolas", 9, "bold"))
        style.configure("Search.TButton", background=self.INK, foreground="white", borderwidth=0, padding=(18, 11), font=("Segoe UI", 10, "bold"))
        style.map("Search.TButton", background=[("active", self.TEAL)])

    def _layout(self):
        page = ttk.Frame(self.root, padding=(40, 30, 40, 34))
        page.pack(fill="both", expand=True)
        ttk.Label(page, text="INFORMATION RETRIEVAL  ·  50 LECTURE NOTES", style="Kicker.TLabel").pack(anchor="w")
        ttk.Label(page, text="Search the ideas behind web search.", style="Title.TLabel").pack(anchor="w", pady=(10, 5))
        ttk.Label(page, text="A simple desktop project based on the supplied lectures: dictionaries, postings, phrase indexes, wildcards, spelling correction, and Soundex.", style="Text.TLabel", wraplength=850).pack(anchor="w", pady=(0, 22))

        search_bar = ttk.Frame(page, style="Card.TFrame", padding=12)
        search_bar.pack(fill="x")
        self.query = tk.StringVar()
        self.input = ttk.Entry(search_bar, textvariable=self.query, font=("Segoe UI", 12))
        self.input.pack(side="left", fill="x", expand=True, padx=(8, 10), ipady=7)
        self.input.bind("<Return>", lambda _event: self.search())
        ttk.Button(search_bar, text="Search  →", style="Search.TButton", command=self.search).pack(side="left")

        ttk.Label(page, text="BOOLEAN QUERIES: dictionary AND postings  ·  wildcard OR soundex  ·  index NOT positional", style="Kicker.TLabel").pack(anchor="w", pady=(11, 0))
        ttk.Label(page, text="IMPORTANT TERMS — click an example to search it", style="Kicker.TLabel").pack(anchor="w", pady=(18, 9))
        topics = tk.Frame(page, bg=self.BG)
        topics.pack(fill="x")
        for number, (term, explanation, example) in enumerate(self.TOPICS):
            card = tk.Frame(topics, bg=self.CARD, highlightbackground="#d7dfd9", highlightthickness=1, padx=10, pady=9)
            card.grid(row=0, column=number, sticky="nsew", padx=3)
            topics.columnconfigure(number, weight=1)
            tk.Label(card, text=term, bg=self.CARD, fg=self.TEAL, font=("Segoe UI", 9, "bold"), anchor="w").pack(fill="x")
            tk.Label(card, text=explanation, bg=self.CARD, fg=self.MUTED, font=("Segoe UI", 8), justify="left", wraplength=125, height=4, anchor="nw").pack(fill="x", pady=(4, 5))
            tk.Button(card, text=example, command=lambda q=example: self.use_example(q), bg="#dff0e8", fg=self.TEAL, relief="flat", cursor="hand2", font=("Consolas", 8, "bold")).pack(anchor="w")

        lower = ttk.Frame(page)
        lower.pack(fill="both", expand=True, pady=(27, 0))
        lower.columnconfigure(0, weight=3)
        lower.columnconfigure(1, weight=1)
        lower.rowconfigure(0, weight=1)
        result_frame = ttk.Frame(lower)
        result_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 22))
        self.status = ttk.Label(result_frame, text="Ready to search the lecture corpus.", style="Text.TLabel")
        self.status.pack(anchor="w", pady=(0, 9))
        self.results = tk.Text(result_frame, bg=self.CARD, fg=self.INK, relief="flat", wrap="word", font=("Segoe UI", 10), padx=17, pady=15, state="disabled")
        self.results.pack(fill="both", expand=True)
        self.results.tag_configure("filename", foreground=self.TEAL, font=("Segoe UI", 11, "bold"), spacing1=10)
        self.results.tag_configure("body", foreground=self.MUTED, spacing3=7)
        self.results.tag_configure("match", background="#ffe28a", foreground=self.INK)
        trace = tk.Frame(lower, bg=self.INK, padx=20, pady=20)
        trace.grid(row=0, column=1, sticky="nsew")
        tk.Label(trace, text="HOW IT WORKS", bg=self.INK, fg="#b7e7cf", font=("Consolas", 9, "bold")).pack(anchor="w")
        tk.Label(trace, text="1. Load 50 text files\n\n2. Tokenize each document\n\n3. Case-fold words\n\n4. Build an inverted index\n\n5. Intersect postings for AND search\n\n6. Expand wildcard terms", bg=self.INK, fg="white", justify="left", font=("Segoe UI", 10), wraplength=220).pack(anchor="w", pady=(15, 0))

    def use_example(self, text):
        self.query.set(text)
        self.search()

    def search(self):
        query = self.query.get().strip()
        if not query:
            self.status.configure(text="Please type a term to search.")
            return
        doc_ids = wildcard_search(query, self.index) if "*" in query else search(query, self.index, list(self.documents))
        self.status.configure(text=f"{len(doc_ids)} document{'s' if len(doc_ids) != 1 else ''} contain the query: “{query}”.")
        self.results.configure(state="normal")
        self.results.delete("1.0", "end")
        if not doc_ids:
            self.results.insert("end", "No matching lecture notes. Try an example term above.", "body")
        words = [word.replace("*", "") for word in query.split() if word.lower() not in {"and", "or", "not"} and word.replace("*", "")]
        for doc_id in doc_ids:
            filename, text = self.documents[doc_id]
            self.results.insert("end", filename + "\n", "filename")
            start = self.results.index("end-1c")
            self.results.insert("end", text + "\n", "body")
            end = self.results.index("end-1c")
            for word in words:
                position = start
                while True:
                    match = self.results.search(word, position, stopindex=end, nocase=True)
                    if not match:
                        break
                    finish = f"{match}+{len(word)}c"
                    self.results.tag_add("match", match, finish)
                    position = finish
        self.results.configure(state="disabled")

    def run(self):
        self.root.mainloop()
