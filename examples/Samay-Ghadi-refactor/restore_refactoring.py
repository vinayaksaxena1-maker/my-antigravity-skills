# -*- coding: utf-8 -*-
import os
import shutil

app_path = r"c:/Users/user/Desktop/Samay Ghadi/src/App.tsx"
components_dir = r"c:/Users/user/Desktop/Samay Ghadi/src/components"
backup_path = r"c:/Users/user/Desktop/Samay Ghadi/scratch/App_backup_before_refactoring.tsx"

def restore():
    if not os.path.exists(backup_path):
        print("Error: Backup file not found at " + backup_path)
        return
        
    shutil.copy2(backup_path, app_path)
    print("App.tsx has been restored to its pre-refactoring state.")
    
    # Clean up generated component files
    choghadiya_file = os.path.join(components_dir, "ChaughadiyaRing.tsx")
    hora_file = os.path.join(components_dir, "HoraRing.tsx")
    
    if os.path.exists(choghadiya_file):
        os.remove(choghadiya_file)
        print("Removed generated ChaughadiyaRing.tsx")
        
    if os.path.exists(hora_file):
        os.remove(hora_file)
        print("Removed generated HoraRing.tsx")

if __name__ == "__main__":
    restore()
