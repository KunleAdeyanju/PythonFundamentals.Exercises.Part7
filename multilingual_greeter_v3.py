import multilingual_greeter
from typing import Dict



"""
        Handling addition of new languages
"""
def new_key_input(lang_options: Dict[int, str]) -> int: 
    key = input("Please enter new key\n")
    while True:
        if key in lang_options:
            key = input("That Key already exists, please enter another\n")
        else:
            break
    return key


def new_language_option_input(lang_options: Dict[int, str]) -> str:
    value = input("Please enter new language\n")
    while True:
        if value in lang_options.values():
            value = input("That Language alrealdy exists, please enter another\n")
        else:
            break
    return value 

# not sure if I actually need this one
def add_additional_languages(lang_options: Dict[int, str],name_prompt: Dict[int,str], greeting_options: Dict[int, str], \
                             new_key, new_value,new_greeting,new_name_prompt):
    # new_key = new_key_input(lang_options)
    # new_value = new_language_option_input(lang_options)
    # new_greeting = new_greeting_option()

    lang_options[new_key] = new_value
    name_prompt[new_key] = new_name_prompt
    greeting_options[new_key] = new_greeting
    

def new_name_prompt() -> str:
    return input("Please enter a new name prompt\n")

def new_greeting_option() -> str:
    return input("Please input new greeting message\n")



    



"""
        Below here is where I actually run the program
"""

if __name__ == '__main__':
    user_selection = False  # controls making sure admin or user mode are chosen
    admin_mode = False      # controls choosing admin mode
    user_mode = False       # controls choosing user mode

    while not user_selection:
        user_input = input("Admin or User mode?\n").lower()
        if user_input == "admin":
            print("You can now update Dictionaries, please follow prompts\n")
            admin_mode = True
            user_selection = True
        elif user_input == "user":
            user_mode = True
            user_selection = True

    while admin_mode:
        print("\nWeclome to admin mode, proceed:\n")
        key_new = new_key_input(multilingual_greeter.lang_dict)
        value_new = new_language_option_input(multilingual_greeter.lang_dict)
        name_prompt_new = new_name_prompt()
        greeting_new = new_greeting_option()
        add_additional_languages(multilingual_greeter.lang_dict,multilingual_greeter.name_prompt_dict, \
                                 multilingual_greeter.greetings_dict, key_new, value_new, greeting_new, name_prompt_new)
        
        print(multilingual_greeter.lang_dict)
        print(multilingual_greeter.name_prompt_dict)
        print(multilingual_greeter.greetings_dict)


    while user_mode:
            multilingual_greeter.print_language_options(multilingual_greeter.lang_dict)
            chosen_lang = multilingual_greeter.language_input()
            while multilingual_greeter.language_choice_is_valid(multilingual_greeter.lang_dict, chosen_lang) is False:
                print("Invalid selection. Try again.")
                chosen_lang = multilingual_greeter.language_input()

            selected_prompt = f"{multilingual_greeter.get_name_input(multilingual_greeter.name_prompt_dict, chosen_lang)} \n"
            chosen_name = multilingual_greeter.name_input(selected_prompt)
            multilingual_greeter.greet(chosen_name, multilingual_greeter.greetings_dict, chosen_lang)