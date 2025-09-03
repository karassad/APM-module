from odoo import models, fields

class OperatorTask(models.Model):
    _name = 'arm.operator.task'
    _description = 'task for operator'

    name = fields.Char(string='Задание', required=True)
    status = fields.Selection([
        ('ready', 'Готово к работе'),
        ('in_progress', 'В работе'),
        ('done', 'Выполнено'),
        ('scrap', 'Брак')
    ], string='Статус', default='ready')
