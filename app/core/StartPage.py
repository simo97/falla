# Falla-StartPage
# -*- encoding: utf-8 -*-
# Sanix-darker

from app.core.Falla import Falla


class StartPage(Falla):
    def __init__(self):
        self.try_it = 0
        self.max_retry = 3
        self.source = "StartPage"
        self.mode = "requests"
        self.results_box = "//section[@id='w-gl--default']"
        self.each_element = {
            "tag": "div",
            "attr": {"class": "w-gl__result"}
        }
        self.href = {
            "tag": "a:w-gl__result-title",
            "type": "attribute",
            "key": "href",
            "child": {}
        }
        self.title = {
            "tag": "a:w-gl__result-title",
            "child": {
                "tag": "h3",
                "type": "text"
            }
        }
        self.cite = {
            "tag": "p:w-gl__description",
            "type": "text",
            "child": {}
        }

    def search(self, search_text, pages=""):
        url = "https://www.startpage.com/sp/search?q=" + search_text.replace(" ", "+") + pages
        print("[+] Searching results for '" + url.split("=")[1].replace("+", " ") +
              "' on '" + self.source + "' :\n")

        return self.fetch(url)

# sp = StartPage()
# print(sp.search("un avion"))
