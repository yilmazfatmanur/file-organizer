import os
import shutil


def findToSubject(folder_path):
    files = []

    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path,item)


        if os.path.isfile(full_path):
            name,ext = os.path.splitext(item)
            ext = ext.lower()

            if ext in [".png", ".jpg", ".jpeg" ]:
                target_folder_name = "Pictures"
            elif ext == ".pdf":
                target_folder_name = "Documents"
            elif ext == ".txt":
                target_folder_name = "TextFiles"
            else:
                target_folder_name = "Others"

            target_folder = os.path.join(folder_path, target_folder_name)

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            files.append(full_path)

            shutil.move(full_path, os.path.join(target_folder, item))
            print("Taşındı: {} -> {}".format(item, target_folder_name))

    return files

folder_path = input("dosya yolunu  giriniz:")
files = findToSubject(folder_path)

print("/nİşlenen dosyalar:")
for f in files:
    print(f)



