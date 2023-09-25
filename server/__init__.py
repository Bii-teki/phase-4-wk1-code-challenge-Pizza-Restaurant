from jinja2 import Markup

html_string = '<script>alert("Hello!")</script>'
safe_html = Markup(html_string)
