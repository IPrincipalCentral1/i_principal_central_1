














'''





this is the structure of the project "I Manufacturing System" :
    
    I_MANUFACTURING_0_I/
    │
    ├── i_main_0_i.py
    │
    ├── i_design_0_i/
    │   ├── mechanical_0_i/
    │   ├── electrical_0_i/
    │   └── 3d_assembly_0_i/
    │
    ├── i_simulation_0_i/
    │   ├── physics_0_i/
    │   ├── thermal_0_i/
    │   └── stress_0_i/
    │
    ├── i_manufacturing_0_i/
    │   ├── cnc_0_i/
    │   ├── laser_0_i/
    │   ├── printing_3d_0_i/
    │   └── pcb_0_i/
    │
    ├── i_export_0_i/
    │   ├── step_0_i/
    │   ├── stl_0_i/
    │   ├── dxf_0_i/
    │   ├── gerber_0_i/
    │   └── pdf_0_i/
    │
    ├── i_factory_0_i/
    │   ├── factory_api_0_i.py
    │   ├── orders_0_i.py
    │   └── quotations_0_i.py
    │
    └── i_projects_0_i/
        └── drone_0_i/
    






installing the nessacere ( in windows 10 ) :
    
    winget install --id FreeCAD.FreeCAD -e
    
    winget install --id OpenSCAD.OpenSCAD -e
    
    winget install --id KiCad.KiCad -e
    
    winget install --id BlenderFoundation.Blender -e
    
    winget install --id CNRISTI.MeshLab -e
    
    
    
    تثبيت CalculiX
    
    
    
    
    
    
    
    
    
    CalculiX
    
    تحليل الإجهادات والتشوهات والقوى على الهيكل.
    إصدارات Windows الرسمية للمشروع
    
    يوجد إصدار Windows 64-bit جاهز للتشغيل.
    
    الطريقة:
    1. افتح CMD.
    2. نفّذ:
        
        winget search CalculiX
        
    
    إذا لم يظهر إصدار مناسب، استخدم رابط GitHub أعلاه.
    3. حمّل ملف CalculiX-VERSION-win-x64.zip من Releases.
    4. فك الضغط إلى:
    C:\i_software_0_i\CalculiX
    
    
    5. ابحث داخل المجلد عن ملف:
    CalculiXWindowsEnvironment.bat
    
    
    شغّله لتهيئة بيئة العمل، وفق تعليمات المشروع. 
    GitHub+
    
    
    https://github.com/calculix/CalculiX-Windows/releases?utm_source=chatgpt.com
    
    












'''






import os

import sys


cwd = os.path.dirname(os.path.abspath(__file__))


i_path_0_i = os.path.dirname(cwd)


i_path_0_i = os.path.dirname(i_path_0_i)


print(f"i_path_0_i = {i_path_0_i} .")


sys.path.append(i_path_0_i)



i_palce_of_module_0_i = os.path.join(i_path_0_i, "i_main_0_i.py")

#import i_main_0_i




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




#print(f"dir(i_main_0_i) = {dir(i_main_0_i)} .")


global i



i = i_main_0_i.i_class_of_i_0_i(i_semaphore_of_pip_install_0_i=True)


i.i_hello_0_i()








i.i_end_of_process_of_compute_0_i()







