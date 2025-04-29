import math
import re

from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

class TimeToRead(BasePlugin):

    page_time_dict = {}
    page_skip_dict = {}


    config_scheme = (
        ('wpm', config_options.Type(int, default=255)),
        ('allPages', config_options.Type(bool, default=True)),
        ('textColor', config_options.Type(str, default="bdbdbd")),
        ('textBeforeMinutes', config_options.Type(str, default="")),
        ('textAfterMinutes', config_options.Type(str, default="min read")),
        ('substitute', config_options.Type(str, default="</h1>")),

    )


    def time(self, text, wpm):
        time = int(math.ceil(len(re.split(re.compile(r'\W+'), text.strip())) / wpm))
        return time


    def on_page_markdown(self, markdown, page, config, files):
        wpm = self.config['wpm']
        all_pages = self.config['allPages']            

        if 'timetoread' in page.meta.keys() and False in page.meta.values():
            key_value = {page.url : False}
            self.page_time_dict.update(key_value)
            return markdown

        if all_pages == True or 'timetoread' in page.meta.keys() and True in page.meta.values():
            self.result = self.time(markdown, wpm)
            key_value = {page.url : self.result}
            self.page_time_dict.update(key_value)
            return markdown

        else:
            return markdown


    def on_post_page(self, output: str, page, config: Config):
        text_color = self.config['textColor']
        text_before_minutes = self.config['textBeforeMinutes']
        text_after_minutes = self.config['textAfterMinutes']
        sub = self.config['substitute']

        for key, value in self.page_time_dict.items():
            if key == page.url:
                if value > 1:
                    wanted = f'</h1><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 20a8 8 0 0 0 8-8 8 8 0 0 0-8-8 8 8 0 0 0-8 8 8 8 0 0 0 8 8m0-18a10 10 0 0 1 10 10 10 10 0 0 1-10 10C6.47 22 2 17.5 2 12A10 10 0 0 1 12 2m.5 5v5.25l4.5 2.67-.75 1.23L11 13V7z"></path></svg><p style="color:#{text_color}">{text_before_minutes}{value} {text_after_minutes}</p>\n'
                elif value == 1:
                    wanted = f'</h1><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 20a8 8 0 0 0 8-8 8 8 0 0 0-8-8 8 8 0 0 0-8 8 8 8 0 0 0 8 8m0-18a10 10 0 0 1 10 10 10 10 0 0 1-10 10C6.47 22 2 17.5 2 12A10 10 0 0 1 12 2m.5 5v5.25l4.5 2.67-.75 1.23L11 13V7z"></path></svg><p style="color:#{text_color}">{text_before_minutes}{value} {text_after_minutes}</p>\n'
                elif value == False:
                    return output
                else: 
                    return output

                if sub in output:
                    where = [m.start() for m in re.finditer(sub, output)][0]
                    before = output[:where]
                    after = output[where:]
                    after = after.replace(sub, wanted, 1)
                    output = before + after
        
                return output
