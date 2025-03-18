import multilingual_greeter

user_selection = False
admin_mode = False
user_mode = False

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