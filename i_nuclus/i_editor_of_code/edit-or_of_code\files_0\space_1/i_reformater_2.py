
















list_of_liberary_to_install = [
                            
                            ["psutil"] ,
                            
                            


]










import os


import traceback

import sys


import subprocess






print(f"\n\n    pip install --upgrade pip setuptools wheel \n\n\n")


subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])





try:
    
    counter_0 = 0
    
    
    while (counter_0 < len(list_of_liberary_to_install)):
    
    
        try:
    
        
            print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")
            
            
            
            
            subprocess.check_call([sys.executable, "-m", "pip", "install", f"{list_of_liberary_to_install[counter_0][0]}"])
        
    
                
        except:
        
                
                        
            traceback.print_exc()
            
            error = traceback.format_exc()
            
            semaphore = True
            
            print(f"Erreur : {str(error)}")
            
    
    
        counter_0 += 1
    
    
except:

        
                
    traceback.print_exc()
    
    error = traceback.format_exc()
    
    semaphore = True
    
    print(f"Erreur : {str(error)}")
    
    



print("\n" * 10)







import psutil



def bytes_to_gb(b):

    return b / (1024**3)


#!/usr/bin/env python3
"""

mem_info.py

اكتشاف نظام التشغيل بواسطة platform ثم عرض معلومات الذاكرة باستعمال psutil.

يعمل على Linux, Windows, macOS وغيرها (حيثما تتوفر psutil).


"""

import sys
import platform



def bytes_to_human(n):
    """حوّل بايت إلى صيغة بشرية (GB/MB/... ) مع دقتين عشريتين."""
    step = 1024.0
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while n >= step and i < len(units)-1:
        n /= step
        i += 1
    return f"{n:.2f} {units[i]}"


def system_info():
    """معلومات عامة عن النظام مع platform."""
    info = {
        "system": platform.system(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "architecture": platform.architecture()[0],
    }
    return info


def print_memory_info():
    vm = psutil.virtual_memory()
    sm = psutil.swap_memory()

    print("=== information of memory (RAM) ===")
    print(f"Total:      {bytes_to_human(vm.total)}")
    print(f"Available:  {bytes_to_human(vm.available)}")
    print(f"Used:       {bytes_to_human(vm.used)}")
    print(f"Free:       {bytes_to_human(vm.free)}")
    print(f"Active:     {bytes_to_human(getattr(vm, 'active', 0))}")
    print(f"Inactive:   {bytes_to_human(getattr(vm, 'inactive', 0))}")
    print(f"Buffers:    {bytes_to_human(getattr(vm, 'buffers', 0))}")
    print(f"Cached:     {bytes_to_human(getattr(vm, 'cached', 0))}")
    print(f"Percent:    {vm.percent}%")
    print()
    print("=== information of memory virtual (Swap) ===")
    print(f"Total swap:     {bytes_to_human(sm.total)}")
    print(f"Used swap:      {bytes_to_human(sm.used)}")
    print(f"Free swap:      {bytes_to_human(sm.free)}")
    print(f"Swap percent:   {sm.percent}%")
    print()


def i_get_information_of_memory_i_0():
    
    
    
    i_result_in_dict_i_0 = {}
    
    
    
    
    
    
    try:
        
        vm = psutil.virtual_memory()
        
        
        print(f"function_1 :")
        
        print(f"Total RAM:     {bytes_to_gb(vm.total):.2f} GB")
        
        print(f"Available RAM: {bytes_to_gb(vm.available):.2f} GB")
        
        print(f"Used RAM:      {bytes_to_gb(vm.used):.2f} GB")
        
        print(f"Free RAM:      {bytes_to_gb(vm.free):.2f} GB")
        
        print(f"Usage percent: {vm.percent}%")
        
        
        i_result_in_dict_i_0["Total_RAM_GB"] = f"{bytes_to_gb(vm.total)}"
        
        i_result_in_dict_i_0["Available_RAM_GB"] = f"{bytes_to_gb(vm.available)}"
        
        i_result_in_dict_i_0["Used_RAM_GB"] = f"{bytes_to_gb(vm.used)}"
        
        i_result_in_dict_i_0["Usage_percent"] = f"{vm.percent}"
        
        
    except:
        
                
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
        
        
        
    
    
    
    print("\n" * 10)
    
    
    
    print(f"function_2 :")
    
    print(f"free -h\n")
    
    os.system(f"free -h")
    
    print("\n" * 10)
    
    
    
    
    
    print(f"function_3 :")
    
    try:
    
        
        
        sysinfo = system_info()
        print("=== information of the operating system ===")
        print(f"System:     {sysinfo['system']}")
        print(f"Platform:   {sysinfo['platform']}")
        print(f"Machine:    {sysinfo['machine']}")
        print(f"Processor:  {sysinfo['processor']}")
        print(f"Python ver: {sysinfo['python_version']} ({sysinfo['architecture']})")
        print()
    
        print_memory_info()
    
        # اختياري: طباعة مخرجات بصيغة JSON إذا أردت لاحقاً المعالجة آلياً
        try:
            import json
            out = {
                "system": sysinfo,
                "virtual_memory": {
                    "total": psutil.virtual_memory().total,
                    "available": psutil.virtual_memory().available,
                    "used": psutil.virtual_memory().used,
                    "free": psutil.virtual_memory().free,
                    "percent": psutil.virtual_memory().percent
                },
                "swap": {
                    "total": psutil.swap_memory().total,
                    "used": psutil.swap_memory().used,
                    "free": psutil.swap_memory().free,
                    "percent": psutil.swap_memory().percent
                }
            }
            # إذا أردت حفظه في ملف: إلغاء التعليق
            # with open("mem_info.json", "w") as f:
            #     json.dump(out, f, indent=2)
        except Exception:
            pass
    
    except:
        
        
                
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
        
        
        
        
    
    
    return i_result_in_dict_i_0
    
    
    
    

if __name__ == "__main__":
    
    
    
    try:
        
        
        i_result_in_dict_i_0 = i_get_information_of_memory_i_0()
        
        
                
        
        print(f"i_result_in_dict_i_0 = {i_result_in_dict_i_0} .")
        
        
        
        
        
        
        
        
        
    except:
        
        
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
        
        
        
        
        
    
    
    
    
    
    

















