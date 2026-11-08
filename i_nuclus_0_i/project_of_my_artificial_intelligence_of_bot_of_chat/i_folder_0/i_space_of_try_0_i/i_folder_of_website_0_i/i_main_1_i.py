













import os



cwd = os.path.dirname(os.path.abspath(__file__))


i_path_0_i = cwd

i_palce_of_module_0_i = os.path.join(i_path_0_i, "i_main_0_i.py")


import importlib.util

from pathlib import Path

i_path_1_i = Path(i_palce_of_module_0_i).resolve()

if i_path_1_i.is_file():

    i_spec_0_i = importlib.util.spec_from_file_location(
        "i_main_0_i",
        i_path_1_i
    )

    if i_spec_0_i is None or i_spec_0_i.loader is None:
        raise ImportError("Cannot load module")

    i_main_0_i = importlib.util.module_from_spec(i_spec_0_i)

    i_spec_0_i.loader.exec_module(i_main_0_i)

else:
    raise FileNotFoundError(i_path_1_i)



global i



i = i_main_0_i.i_class_of_i_0_i(i_semaphore_of_pip_install_0_i=True)


i.i_hello_0_i()





i_text_0_i = " i_hello_0_i "



print(f"i_text_0_i = {i_text_0_i} .")


i_first_number_0_i = ord(i_text_0_i[0])


i_last_number_0_i = ord(i_text_0_i[1])

print(f"i_first_number_0_i = {i_first_number_0_i} . i_last_number_0_i = {i_last_number_0_i} .")


i_v_0_i = i.i_get_a_function_0_i(i_v_a_i=i_first_number_0_i, i_v_b_i=i_last_number_0_i)


i_v_1_i = i.i_check_and_get_list_of_all_chose_one_0_i(i_list_of_all_chose_one_0_i=i_v_0_i, i_first_number_0_i=i_first_number_0_i, i_last_number_0_i=i_last_number_0_i)


print(f"i_v_0_i = {i_v_0_i} . i_v_1_i = {i_v_1_i} .")





i_v_2_i = i.i_get_list_of_recognition_0_i(i_text_0_i=i_text_0_i)


print(f"i_v_2_i = {i_v_2_i} .")






i_v_3_i = i.i_go_of_trying_0_i(i_list_of_recognition_0_i=i_v_2_i[0][1], i_first_token_0_i=ord(i_text_0_i[0]), i_number_of_maximum_try_0_i=len(i_text_0_i) * 2)






print(f"i_v_3_i = {i_v_3_i} .")






i_v_4_i = i.i_get_list_of_char_from_list_of_token_0_i(i_list_of_all_token_0_i=i_v_3_i)



print(f"i_v_4_i = {i_v_4_i} .")






i_t_0_i = i.time.time()

i.i_my_artificial_intelligance_functional_0_i(i_v_bool_0_i=False, i_var_1_i={})

i_t_1_i = i.time.time()



print(f"i_my_artificial_intelligance_functional_0_i succesfully ended . time == {i_t_1_i - i_t_0_i} second .")



print("\n" * 10)



i_t_0_i = i.time.time()

i.i_music_0_i()

i_t_1_i = i.time.time()


print(f"generation of file of music completed successfully . time == {i_t_1_i - i_t_0_i} second .")




print("\n" * 5)


i_t_0_i = i.time.time()

i.i_video_0_i()

i_t_1_i = i.time.time()


print(f"generation of file of video completed successfully . time == {i_t_1_i - i_t_0_i} second .")






i.i_end_of_process_of_compute_0_i()










