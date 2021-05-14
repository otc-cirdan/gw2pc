from datetime import timedelta
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def format_gold(value):
    # One day this may use icons.
    return format_gold_text(value)

@register.filter
def format_gold_text(value):
    if not value:
        value = 0
    copper = int(value % 100)
    value = (value - copper)/100
    silver = int(value % 100)
    value = (value - silver)/100
    gold = int(value)
    if gold:
        return f"{gold}g {silver:02d}s {copper:02d}c"
    elif silver:
        return f"{silver}s {copper:02d}c"
    elif copper:
        return f"{copper}c"
    else:
        return "0c"

@register.filter
def format_gold_text_gs(value):
    if not value:
        value = 0
    value = round(value/100)
    silver = int(value % 100)
    value = (value - silver)/100
    gold = int(value)
    if gold:
        return f"{gold}g {silver:02d}s"
    elif silver:
        return f"{silver}s"
    else:
        return "0s"

@register.filter
def getitem(dictionary, key):
    return dictionary.get(key)

def pctable_cell_classes(table, row=None, column=None):
    classes = []
    if 'hilight_rows' in table and row and row['key'] in table['hilight_rows']:
        classes.append('price-table-hilight-row')
    if 'hilight_cols' in table and column and column['key'] in table['hilight_cols']:
        classes.append('price-table-hilight-col')
    return " ".join(classes)

@register.filter
def multiply(value, arg):
    return value * arg

@register.simple_tag
def render_cell(table, row, column):
    if 'row_first' in table:
        cell_info = table['data'][row['key']][column['key']]
    else:
        cell_info = table['data'][column['key']][row['key']]
    classes = "price-table-price " + pctable_cell_classes(table, row, column)
    if isinstance(cell_info, dict):
        cell_val = cell_info['val']
        if 'hilight' in cell_info:
            classes += " price-table-hilight-col"
    else:
        cell_val = cell_info

    format_gold_function = format_gold_text
    if 'format' in table and table['format'] == 'gs':
        format_gold_function = format_gold_text_gs


    response = f"<td class='{classes}'>\n"
    response += f"{format_gold_function(cell_val)}\n"
    if 'include_stack' in table:
        response += f"<br />{format_gold_function(cell_val*250)}\n"
    response += "</td>"
    return mark_safe(response)

