import multilingual_greeter
from typing import Dict


user_selection = False  # controls making sure admin or user mode are chosen
admin_mode = False      # controls choosing admin mode
user_mode = False       # controls choosing user mode
key_in_dic = True       # checking if the new key already exists
value_in_dic = True     # checking if the language is already being used

def new_language_key_input(lang_options: Dict[int, str]) -> int: 
    key = input("Please enter a new\n")
    while key_in_dic:
        if key in lang_options:
            key = input("That Key already exists, please enter another\n")
        else:
            key_in_dic = False
            return int(key)


def new_language_option_input(lang_options: Dict[int, str]) -> str:
    value = input("Please enter new language\n")
    while value_in_dic:
        if value in lang_options.values():
            value = input("That Language alrealdy exists, please enter another\n")
        else:
            value_in_dic = False
            return value 

# not sure if I actually need this one
def add_additional_languages(lang_options: Dict[int, str]):
    new_key = new_language_key_input(lang_options)
    new_value = new_language_option_input(lang_options)
    
    lang_options[new_key] = new_value


    



"""
        Below here is where I actually run the program
"""

while not user_selection:
    user_input = input("Admin or User mode?\n").lower()
    if user_input == "admin":
        admin_mode = True
        user_selection = True
    elif user_input == "user":
        user_mode = True
        user_selection = True


while user_mode:
    if __name__ == '__main__':
        multilingual_greeter.print_language_options(multilingual_greeter.lang_dict)
        chosen_lang = multilingual_greeter.language_input()
        while multilingual_greeter.language_choice_is_valid(multilingual_greeter.lang_dict, chosen_lang) is False:
            print("Invalid selection. Try again.")
            chosen_lang = multilingual_greeter.language_input()

        selected_prompt = f"{multilingual_greeter.get_name_input(multilingual_greeter.name_prompt_dict, chosen_lang)} \n"
        chosen_name = multilingual_greeter.name_input(selected_prompt)
        multilingual_greeter.greet(chosen_name, multilingual_greeter.greetings_dict, chosen_lang)