from odoo import fields,models

class Book(models.Model):
    _name = "library.book"
    _description = "Library Book Module"
    
    name = fields.Char(string="Title",required=True)
    active = fields.Boolean(string="Active",default=True)
    isbn = fields.Char(string="ISBN")
    genre = fields.Char(string="Genere")
    summary = fields.Text(string="Summary")
    author = fields.Char(string="Author")
    format = fields.Selection(string="Format",
                              selection=[
                                  ("paperback","Paperback"),
                                  ("hardcover","Hardcover"),
                                  ("audiobook","Audiobook"),
                                  ("ebook","E-book"),
                                  ],)
    language = fields.Selection(string="Language",
                                selection=[
                                    ("en","English"),
                                    ("es","Espanish"),
                                    ("fr","French"),
                                    ("de","German"),
                                ],)
    edition = fields.Integer(string="Edition",default=0)
    publisher = fields.Char(string="Publisher")
    publish_date = fields.Date(string="Publish Date")
    price = fields.Float(string="Price")
    
    