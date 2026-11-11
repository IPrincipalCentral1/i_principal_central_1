













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





print("\n" * 5)


i_t_0_i = i.time.time()

i.i_video_0_i()

i_t_1_i = i.time.time()


print(f"generation of file of video completed successfully . time == {i_t_1_i - i_t_0_i} second .")






i.i_end_of_process_of_compute_0_i()










