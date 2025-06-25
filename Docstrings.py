def format_name(f_name, l_name):
    """Takes the first name and last name and formats them with
     title case versions of the names."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



