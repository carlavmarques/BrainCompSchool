#! /usr/bin/env python
# -*- coding: UTF8 -*-
""" Ponto de entrada do módulo Arvora.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Classes neste módulo:
    - :py:class:`SimplePage` A page used as a base for the others.
    - :py:class:`LandingPage` Entry point for the platform.
    - :py:class:`LoginPage` User Registration page.
    - :py:class:`Arvora` Main class with the main functionality.
    - :py:func:`main` Called entry page to start the application.

Changelog
---------
.. versionadded::    24.03
   |br| first version of main (05)

|   **Open Source Notification:** This file is part of open source program **Arvora**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <http://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

"""
MENU_OPTIONS = tuple(zip("PROJETO CONHECIMENTO PESQUISA INTERAÇÃO LOGIN USER".split(),
                     "bars-progress book book-medical hands-asl-interpreting right-to-bracket user".split()))


class SimplePage:
    PAGES = dict()

    def __init__(self, brython, menu=MENU_OPTIONS, hero="none_hero"):
        _menu = [{"title": items, "icon": icons} for items, icons in menu]
        self.brython = brython
        self.hero_class = hero
        self.items = []
        self.page = self.hero(self.navigator(_menu))
        [item.bind("click", self.link) for item in self.items]

    def link(self, ev=None):
        ev.preventDefault()
        page = ev.target.id.strip("-")
        self.PAGES[page].show()

    def show(self):
        self.brython.document["pydiv"].html = ""
        _ = self.brython.document["pydiv"] <= self.page
        self.brython.document["_USER_-"].html = Arvora.ARVORA.current_user

    def build_body(self):
        return ()

    def hero(self, navigator):
        h = self.brython.html
        cnt = h.DIV(self.build_body(), Class="container has-text-centered pb-6 mgb-large")
        hby = h.DIV(cnt, Class="hero-body is-justify-content-center is-align-items-center")
        hea = h.DIV(navigator, Class="hero-head")
        sec = h.SECTION((hea, hby), Class=f"hero {self.hero_class} is-fullheight")
        return sec

    def navigator(self, menu):
        h = self.brython.html

        def do_item(title=None, icon=None):
            spn = h.SPAN(
                h.I(Class=f"fa fa-lg fa-{icon}", Id=f"-_{title}_-")+h.SPAN(title, Id=f"_{title}_-"),
                Class="icon-text", style="color: #333;", Id=f"-_{title}_--")
            return h.A(spn, Id=f"_{title}_", Class="navbar-item", href="./#")
        aim = h.IMG(src="/src/arvora/_media/arvora_ico.png", alt="Arvora", height="28", Id="_MAIN_-")
        arv = h.A(aim, Id="_MAIN_", Class="navbar-item", href="./")
        nbr = h.DIV(arv, Class="navbar-brand", Id="-_MAIN_-")
        self.items = [do_item(**item) for item in menu]
        end = h.DIV(self.items[-1], Class="navbar-end")
        self.items = items = [nbr]+self.items[:-1]+[end]
        nav = h.NAV(items, Class=f"navbar")
        fna = h.DIV(h.DIV(nav, Class="container"), Class="first_nav")
        return fna


class LandingPage(SimplePage):
    def __init__(self, brython, menu=MENU_OPTIONS):
        super().__init__(brython, menu, hero="main_hero")

    def build_body(self):
        h = self.brython.html
        tt1 = h.P("A R V O R A", Class="title main-text has-text-weight-bold")
        tt2 = h.P("Brain Computational School", Class="title is-1 main-text")
        return h.DIV((tt1, tt2))


class LoginPage(SimplePage):
    def __init__(self, brython, menu=MENU_OPTIONS):
        super().__init__(brython, menu, hero="main_hero")
        self.form = self.login = self.passd = None

    def click(self, ev=None):
        _ = self
        ev.preventDefault()
        form = ev.target
        # USER_OPTIONS = form.elements["username"].value
        Arvora.ARVORA.user(form.elements["username"].value)
        SimplePage.PAGES["_MAIN_"].show()

        # self.brython.alert(form.elements["username"].value, form.elements["password"])
        # print(self.login.value, self.passd.type)

    def build_body(self):
        h = self.brython.html
        btn = h.BUTTON("Login", Class="button is-primary is-fullwidth", type="submit")
        self.passd = h.INPUT(Id="password", Class="input is-primary", type="password", placeholder="Password")
        psw = h.DIV(h.LABEL("Password", For="Name")+self.passd, Class="field")
        self.login = h.INPUT(Id="username", Class="input is-primary", type="text", placeholder="Email address")
        eid = h.DIV(h.LABEL("Email", For="email")+self.login, Class="field")
        form = h.FORM((eid, psw, btn), Class="column is-4 box")
        form.bind("submit", self.click)

        cls = h.DIV(form, Class="columns is-flex is-flex-direction-column")
        return cls

class ProjectPage(SimplePage):
    def __init__(self, brython, menu=MENU_OPTIONS):
        super().__init__(brython, menu, hero="main_hero")
    def build_body(self):

        #   ATENÇÃO
        #   Segue abaixo as seguintes informações importantes:
        #   Legenda: Title _t Subtitle _s Anchor _a Imagem _img
        #   Temos Introdução, Objetivo, Usuario(Cliente) e Estágio Atual
        #
        #   O QUE FALTA? Estou com problemas em dimensionar a imagem. O código está na linha 145 com o r_img. Boa sorte e obrigado!
        #   Se conseguir aumentar a parto do PROJETO ARVORA eu agradeceria também ehehehhe


        h = self.brython.html

        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        #hr = h.HR(Class = "content-divider")

        pj_t1 = h.H1("Projeto ", Class = "title main-subtext")
        pj_t2 = h.H1("ARVORA", Class="title main-text")
        pj_t = h.DIV((pj_t1, pj_t2), Class="columns")
        pj_s = h.H2("O que é a Brain Computational School", Class = "subtitle is-1")
        pj_a = h.A("Comece aqui!", href='#intro', Class = "button is-white is-medium is-inverted")
        pj_div=h.DIV((pj_t, pj_s, pj_a), Class="has-text-centered")
        pj = h.SECTION(pj_div, Class=" hero is-medium hero-body is-fullheight columns is-centered")

        r_t = h.H1("Introdução", id = "intro", Class="title is-3 ") # resume title
        r_img = h.FIGURE((h.IMG(src="https://bulma.io/images/placeholders/256x256.png")), Class="image is-fullwidth")
        r_fig = h.DIV(r_img, Class="column is-3 ")
        r_p = h.P(text, Class="subtitle")

        r_text = h.DIV((r_t, r_p), Class="hero is-large hero-body container column is-6 featured-content")
        r = h.SECTION((r_fig, r_text), Class="columns")

        obj_t = h.H1("Objetivo", Class="title is-3 ") # objective title
        obj_p = h.P(text,  Class = "subtitle")
        obj = h.SECTION((obj_t, obj_p),
                        Class="hero is-large hero-body container has-text-left")

        cli_t = h.H1("Usuário", Class="title is-3 ")  # client title
        cli_img = h.FIGURE((h.IMG(src="https://bulma.io/images/placeholders/256x256.png")), Class="image is-fullwidth")
        cli_fig = h.DIV(cli_img, Class="column is-3 ")
        cli_p = h.P(text,  Class = "subtitle")
        cli_text = h.DIV((cli_t, cli_p), Class="hero is-large hero-body container column is-6 featured-content")
        cli = h.SECTION((cli_text, cli_fig), Class="columns")

        done_t = h.H1("Estágio Atual", Class="title is-3 ")  # Estage title
        done_p1 = h.P(text, Class="subtitle")
        done_p2 = h.P(text, Class="subtitle")
        done = h.SECTION((done_t, done_p1, done_p2),
                        Class="hero is-large hero-body container has-text-left columns")
        #r = h.SECTION((r_t, r_p), Class = "content has-text-left")

        box = h.DIV((r, obj, cli, done), CLass = "hero box m-6")
        sec = h.DIV((pj, box), Class = "")

        return sec

users = [
    {
        "name": "Roberto",
        "email": "roberto@mail",
        "points": "100",
        "id": "1",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "tags": "#mav",
        "date": "2021-01-21"
    },
    {
        "name": "Amanda",
        "email": "amanda@mail",
        "points": "72",
        "id": "2",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "tags": "#mav",
        "date": "2021-01-21"
    },
    {
        "name": "Roberto",
        "email": "roberto@mail",
        "points": "100",
        "id": "1",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "tags": "#mav",
        "date": "2021-01-21"
    },
    {
        "name": "Amanda",
        "email": "amanda@mail",
        "points": "72",
        "id": "2",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "tags": "#mav",
        "date": "2021-01-21"
    },
    # {
    #     "name": "Amanda",
    #     "password": "1234",
    #     "email": "amanda@mail",
    #     "posts":[
    #         {
    #             "id": "1",
    #             "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    #             "tags": "#mav",
    #             "date": "2021-01-21"
    #         },
    #     ]
    #  },

]
class KnowledgePage(SimplePage):
    def __init__(self, brython, menu = MENU_OPTIONS):
        super().__init__(brython, menu, hero="main_hero")

    def build_body(self):
        h = self.brython.html

        card = ""

        Dialog = self.brython.Dialog
        InfoDialog= self.brython.InfoDialog

        # def ok(ev):
        #     comment_text =  comment.select_one("INPUT").value
        #     comment.close()
        def click(ev):
            if ev.target.id == "Draft":
                SimplePage.PAGES["_RASCUNHO_"].show()
            elif ev.target.id == "Writing":
                SimplePage.PAGES["_ESCREVER_"].show()
        def show_article(ev):
            SimplePage.PAGES["_ARTIGO_"].show()
        def show_dialog(ev):
            comment = Dialog("Test", ok_cancel=True)
            comment.panel <= h.DIV("Escreva seu comentário: " + h.INPUT())
            comment.bind("click", comment.ok_button)

        search_bar = h.FORM(h.DIV(h.INPUT(Id="local_search",
                                          Class="input is-white has-fixed-size block has-background-grey has-text-success-light mb-4 white-placeholder",
                                          placeholder="Pesquisar artigos"), Class="column"))

        for user in users:

            card_img = h.FIGURE(h.IMG(src="https://bulma.io/images/placeholders/256x256.png"), Class="card-image image is-4by3")

            card_content = h.DIV((
                            h.FIGURE((h.IMG(src="https://res.cloudinary.com/ameo/image/upload/v1639144778/typocat_svbspx.png")), Class = "media-left image is-48x48"),
                            h.P(user["name"], Class = "title is-4"),
                            h.P(user["email"], Class="subtitle is-6"),
                            h.P("Estrelas: " + user["points"]),
                            h.P(user["text"]),
                            h.P(user["tags"]),
                            h.P(user["date"])), Class="content")

            card_buttons = h.DIV((
                            h.BUTTON("Comentar", Class = "button is-primary").bind("click", show_dialog),
                            h.BUTTON("Perguntar", Class="button is-info"),
                            h.BUTTON("Artigos Filhos", Class="button")), Class = "card-footer")

            card += h.DIV((card_img, card_content, card_buttons), Class="box").bind("click", show_article)
        post = h.DIV((search_bar, card), Class= "column is-half is-offset-one-quarter ")
        posts = h.DIV(post, Class="columns body-columns")
        btn1 = h.BUTTON("Rascunho", Id='Draft', Class="button has-background-grey-light is-4 block is-fullwidth")
        btn2 = h.BUTTON("Escreva seu artigo", Id="Writing",
                        Class="button has-background-grey-light is-4 block is-fullwidth")
        side_tab = h.DIV((btn2, btn1), Class="column is-3")
        side_tab.bind("click", click)

        wrapper = h.DIV((side_tab, posts), Class="columns mt-5")
        return wrapper


class Article(SimplePage):
    def __init__(self, brython, menu = MENU_OPTIONS):
        super().__init__(brython, menu, hero="main_hero")
    def build_body(self):
        h = self.brython.html
        Dialog = self.brython.Dialog
        InfoDialog = self.brython.InfoDialog
        user = users[0]

        def show_dialog(ev):
            comment = Dialog("Test", ok_cancel=True)
            comment.panel <= h.DIV("Escreva seu comentário: " + h.INPUT())
            comment.bind("click", comment.ok_button)

        card_img = h.FIGURE(h.IMG(src="https://bulma.io/images/placeholders/256x256.png"),
                            Class="card-image image is-4by3")

        card_content = h.DIV((
            h.FIGURE((h.IMG(src="https://res.cloudinary.com/ameo/image/upload/v1639144778/typocat_svbspx.png")),
                     Class="media-left image is-48x48"),
            h.P(user["name"], Class="title is-4"),
            h.P(user["email"], Class="subtitle is-6"),
            h.P("Estrelas: " + user["points"]),
            h.P(user["text"]),
            h.P(user["tags"]),
            h.P(user["date"])), Class="content")

        card_buttons = h.DIV((
            h.BUTTON("Comentar", Class="button is-primary").bind("click", show_dialog),
            h.BUTTON("Perguntar", Class="button is-info"),
            h.BUTTON("Artigos Filhos", Class="button")), Class="card-footer")





        #comment section




        #user comment
        user_photo = h.FIGURE(
            h.P((h.IMG(src="https://bulma.io/images/placeholders/128x128.png")), Class="image is-64x64"),
            Class="media-left")
        comment_box = h.DIV(h.TEXTAREA(placeholder = "Escreva aqui...", Class = " Focused textarea has-fixed-size has-background-grey"), Class = "media-content field control")
        comment_section = h.ARTICLE((user_photo, comment_box), Class="media mt-5")

        card = h.DIV((card_img, card_content, card_buttons, comment_section), Class="box")
        post = h.DIV(card, Class="column is-half is-offset-one-quarter ")
        posts = h.DIV(post, Class="columns body-columns")
        return posts


class Arvora:
    ARVORA = None

    def __init__(self, br):
        self.users = dict(ADMIN="admin", USER="user")
        self.brython = br
        self.current_user = None
        Arvora.ARVORA = self

    def user(self, current_user):
        self.current_user = current_user

    def start(self):
        br = self.brython
        SimplePage.PAGES = {f"_{page}_": SimplePage(br) for page, _ in MENU_OPTIONS}
        SimplePage.PAGES["_MAIN_"] = LandingPage(br)
        SimplePage.PAGES["_LOGIN_"] = LoginPage(br)
        SimplePage.PAGES["_PROJETO_"] = ProjectPage(br)
        SimplePage.PAGES["_CONHECIMENTO_"] = KnowledgePage(br)
        SimplePage.PAGES["_ARTIGO_"] = Article(br)
        _main = LandingPage(br)
        _main.show()
        return _main


def main(br):
    return Arvora(br).start()
