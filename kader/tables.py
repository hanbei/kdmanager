from django.utils.html import format_html
from django_tables2 import tables
import django_tables2 as table

from kader.models import Member

link_template = '''{% if perms.kader.change_member %}
                   <a href="{% url 'edit' value %}"><i class="far fa-edit"></i></a>
                   {% endif %}
                   {% if perms.kader.delete_member %}
                   <a href="{% url 'delete' value %}"><i class="far fa-trash-alt"></i></a>
                   {% endif %}'''


class MemberTable(tables.Table):
    name = table.Column()
    first_name = table.Column()
    birth_date = table.DateColumn()
    gender = table.Column()
    grade = table.Column()
    email = table.EmailColumn()
    zekken = table.BooleanColumn()
    jacket = table.BooleanColumn()
    active = table.BooleanColumn()
    id = table.TemplateColumn(link_template, verbose_name='')

    class Meta:
        model = Member
        template_name = 'django_tables2/bootstrap-responsive.html'
        sequence = ('first_name', 'name', 'birth_date', 'gender', 'grade', 'email', 'zekken', 'jacket', 'active', '...')
        attrs = {'class': 'table table-striped'}

    def render_zekken(self, value):
        return self.render_boolean(value)

    def render_jacket(self, value):
        return self.render_boolean(value)

    def render_active(self, value):
        return self.render_boolean(value)

    def render_boolean(self, value):
        if value:
            return format_html('<i class="far fa-check-square"></i>')
        else:
            return format_html('<i class="far fa-square"></i>')
