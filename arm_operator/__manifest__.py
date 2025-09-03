{
    'name': "ARM Operator",
    'version': '1.0',
    'depends': ['base'],
    'author': "Author Name",
    'category': 'Manufacturing',
    'description': """
    Автоматизированное рабочее место оператора производства
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/task_views.xml'
    ],
    'application': True,
    'installable': True
}