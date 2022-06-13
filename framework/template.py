
"""
Используем шаблонизатор Jinja2
"""
import sys

from jinja2 import Template, FileSystemLoader, Environment, select_autoescape

sys.path.append('../')


def render(template_name, **kwargs):
    """
    Минимальный пример работы с шаблонизатором
    :param template_name: имя шаблона
    :param kwargs: параметры для передачи в шаблон
    :return:
    """

    env = Environment(
        loader=FileSystemLoader('./templates/'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    # # Открываем шаблон по имени
    # with open('templates/' + template_name, encoding='utf-8') as f:
    #     # Читаем
    #     template = Template(f.read())
    #     # рендерим шаблон с параметрами
    #     return template.render(**kwargs)

    template = env.get_template(template_name)
    return template.render(**kwargs)

if __name__ == '__main__':
    # Пример использования
    output_test = render('authors.html', object_list=[{'name': 'Leo'}, {'name': 'Kate'}])
    print(output_test)
