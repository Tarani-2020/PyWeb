import webbrowser as wb
import os

class HTML:

    def __init__(self):
        self.html = "<!DOCTYPE html><html>"
    
    def add(self, obj):
        self.html += obj.contentText
    
    def addHTML(self, html):
        self.html += html
        
    def addJS(self, js):
        self.html += f"<script type=\"js\">{js}</script>"
    
    def end(self):
        self.html += "</html>"
        
    def run(self):
        path = os.path.abspath("run.html")
        runner = open(path, "w")
        runner.write(self.html)
        runner.close()
        
        wb.open(path)

class Paragraph:
    def __init__(self, content):
        self.contentText = "<p>"
        if(type(content) == type("")):
            self.contentText += content
        else:
            self.contentText += content.contentText
        self.contentText += "</p>"

class Anchor:
    def __init__(self, href:str, content=None):
        self.contentText = f"<a href={href}>"
        if(type(content) == type("")):
            self.contentText += content
        else:
            self.contentText += content.contentText
        self.contentText += "</a>"

class Heading:
    def __init__(self, index, content):
        self.contentText = f"<h{index}>"
        if(type(content) == type("")):
            self.contentText += content
        else:
            self.contentText += content.contentText
        self.contentText += f"</h{index}>"
  
class Iframe:
    def __init__(self, src:str,content="", **options):
        self.contentText = f"<iframe src={src}"
        
        if "height" in options:
            self.contentText += f" height={options["height"]}"
        if "width" in options:
            self.contentText += f" width={options["width"]}"
        if "title" in options:
            self.contentText += f" title={options["title"]}"
        if "name" in options:
            self.contentText += f" name={options["name"]}"
        if "allow" in options:
            self.contentText += f" allow={options["allow"]}"
        if "referrerpolicy" in options:
            self.contentText += f" referrerpolicy={options["referrerpolicy"]}"
        if "loading" in options:
            self.contentText += f" loading={options["loading"]}"
            
        if(type(content) == type("")):
            self.contentText += f">{content}</iframe>"
        else:
            self.contentText += f">{content.contentText}</iframe>"
        

