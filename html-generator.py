class HTML: 
#все что может делать этот класс собирать другие объекты в список children и превращает их в строку и 
# обвернуть с тегами <html></html> и плюс ко всем добавляет не обязательный аттрибут lang
    def __init__(self, langua):
        self.langua = langua
        self.children = []

    def appending_it(self, *kwarg): 
        #данный метод дает возможность складовать в список children другие объекты и взвращает сам объект
        for arge in kwarg:
            self.children.append(arge)
        return self

    def __str__(self): #тут объект превращается в строку
        html = f"<html lang = '{self.langua}'>\n"
        for child in self.children:
            html += str(child)
        html += "</html>"
        return html

class TopLevelTag: 
    #как аргумент принимает тег и умеет пополнять children другими объектами и обворачивать с тегом которого принял как аргумент
    def __init__(self, tag):
        self.tag = tag
        self.children = []

    def appending_it(self, *kwarg): 
        #данный метод дает возможность складовать в список children другие объекты и взвращает сам объект
        for arge in kwarg:
            self.children.append(arge)
        return self

    def __str__(self): #тут все превращается в строку
        html = f"<{self.tag}>\n"
        for child in self.children:
            html += str(child)
        html += f"\n</{self.tag}>\n"
        return html

class Tag:
    #класс Tag на вход принимает несколько явно определьенных аргументов (tag, text, is_single, klass). 
    #**kwargs дает возможность в класс передавать стронные аттрибуты в виде словаря
    # словарь attributes и список children пополняется в ходе составления эклемпляиров класса
    def __init__(self, tag, is_single=False, klass=None, **kwargs):
        self.tag = tag
        self.text = ""
        self.is_single = is_single

        self.attributes = {}
        self.children = []

        if klass is not None: 
            #если в аргумент klass что - то передается (список или кортеж)то их объяденяют в строку 
            # и присвоивают в ключь "class" словаря attributes 
            self.attributes["class"] = " ".join(klass)

        for attr, value in kwargs.items(): 
            #перебрасывает элементы словаря kwargs в словарь attributes по ходу дела заменяя "-" в "_"
            if "_" in attr:
                attr = attr.replace("_", "-")
            self.attributes[attr] = value

    def appending_it(self, *kwarg): 
        #данный метод дает возможность складовать в список children другие объекты и взвращает сам объект
        for arge in kwarg:
            self.children.append(arge)
        return self

    def __str__(self):
        attrs = []
        for attribute, value in self.attributes.items(): 
        #тут разбирается словарь attributes по ключам(attribute) и значениям (value) и создается список attrs с данными словаря через "="
        # в конце список  аttrs преврошается встроку с помощью функции join и обновляет себя
            attrs.append(f'{attribute}="{value}"') 
        attrs = " ".join(attrs)

        if len(self.children) > 0 and len(attrs) > 0:
        #в данной части кода проверятеся содержания в строке attrs и в словаре children и на оснавании их строятся строка из объекта
            opening = f"<{self.tag} {attrs}>"
            if self.text:
                internal = f"{self.text}"
            else:
                internal = ""
            for child in self.children:
                internal += str(child)
            ending = f"</{self.tag}>"
            return opening + internal + ending
        elif len(self.children) > 0 and len(attrs) == 0:
            opening = f"<{self.tag}>"
            if self.text:
                internal = f"{self.text}"
            else:
                internal = ""
            for child in self.children:
                internal += str(child)
            ending = f"</{self.tag}>"
            return opening + internal + ending
        elif self.is_single and len(attrs) > 0:
        #в данной части кода проверятеся содержания в строке attrs и на условие is_single и на оснавании их строятся строка из объекта
            return f"<{self.tag} {attrs}/>"
        elif self.is_single and len(attrs) == 0:
            return f"<{self.tag}/>"
        elif not self.is_single and len(attrs) > 0:
            return f"<{self.tag} {attrs}>{self.text}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.text}</{self.tag}>"

html = HTML(langua="ru")
head = TopLevelTag("head")
title = Tag("title", text = "Some text for some text")
body = TopLevelTag("body")
h1 = Tag("h1", klass=["main-text", "header1"], text = "SSome text for H1")
div1 = Tag("div", klass=["container", "container-fluid"], id="lead")
p1 = Tag("p", text = "some another text")
img1 = Tag("img", is_single=True, src="/icon.png", data_image="responsive")
html.appending_it(head.appending_it(title), body.appending_it(h1, div1.appending_it(p1, img1)))
print(html)