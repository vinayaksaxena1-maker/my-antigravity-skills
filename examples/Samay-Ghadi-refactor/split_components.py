# -*- coding: utf-8 -*-
import os
import shutil

app_path = r"c:/Users/user/Desktop/Samay Ghadi/src/App.tsx"
components_dir = r"c:/Users/user/Desktop/Samay Ghadi/src/components"
backup_path = r"c:/Users/user/Desktop/Samay Ghadi/scratch/App_backup_before_refactoring.tsx"

def extract_code():
    with open(app_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    start_choghadiya = content.find("interface ChaughadiyaRingProps {")
    start_hora = content.find("export function HoraRing(")
    
    if start_choghadiya == -1 or start_hora == -1:
        print("Error: Could not locate start of ChaughadiyaRing or HoraRing")
        return
        
    choghadiya_block = content[start_choghadiya:start_hora]
    last_brace = choghadiya_block.rfind("}")
    choghadiya_code = choghadiya_block[:last_brace+1]
    
    start_app = content.find("export default function App()")
    if start_app == -1:
        print("Error: Could not locate start of App component")
        return
        
    hora_block = content[start_hora:start_app]
    last_brace_hora = hora_block.rfind("}")
    hora_code = hora_block[:last_brace_hora+1]
    
    hora_props_def = """interface HoraRingProps {
  horaList: HoraInterval[];
  activeHora: number;
  currentTime: Date;
}

"""
    
    choghadiya_file_content = f"""import React from 'react';
import {{ ChoghadiyaInterval }} from '../types';

{choghadiya_code}
"""
    
    with open(os.path.join(components_dir, "ChaughadiyaRing.tsx"), "w", encoding="utf-8") as f:
        f.write(choghadiya_file_content)
    print("Created ChaughadiyaRing.tsx")

    hora_file_content = f"""import React from 'react';
import {{ HoraInterval }} from '../types';

{hora_props_def}{hora_code}
"""
    with open(os.path.join(components_dir, "HoraRing.tsx"), "w", encoding="utf-8") as f:
        f.write(hora_file_content)
    print("Created HoraRing.tsx")

    modified_content = content[:start_choghadiya] + content[start_app:]
    
    subcomponents_marker = "// Subcomponents"
    import_addition = "\nimport { ChaughadiyaRing } from './components/ChaughadiyaRing';\nimport { HoraRing } from './components/HoraRing';\n"
    
    marker_pos = modified_content.find(subcomponents_marker)
    if marker_pos != -1:
        insert_idx = marker_pos + len(subcomponents_marker)
        modified_content = modified_content[:insert_idx] + import_addition + modified_content[insert_idx:]
        
    with open(app_path, "w", encoding="utf-8") as f:
        f.write(modified_content)
    print("Modified App.tsx to import ChaughadiyaRing and HoraRing")

if __name__ == "__main__":
    scratch_dir = r"c:/Users/user/Desktop/Samay Ghadi/scratch"
    if not os.path.exists(scratch_dir):
        os.makedirs(scratch_dir)
    shutil.copy2(app_path, backup_path)
    print(f"Backup created at {backup_path}")
    extract_code()
