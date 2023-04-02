import os
import sys
# לא גמור צריך לשתנות לפי צריכים בהמשך


class Info_and_Install:  # Info_and_Install # אין פעולה בונה
    def Cores_Computer():
        ''' 
        הפעולה מחזירה את מספר המעבדים שבמערכת.
        מחזירה ללא אם לא נקבע
        '''
        return os.cpu_count()

    def Get_Python_Version():
        """
        הפעולה מחזירה את גרסת פייתון שאתה משתמש
        (3.7.4) בצורה הבאה
        """
        # this_py = sys.version_info
        this_py = sys.version_info.major, sys.version_info.minor, sys.version_info.micro
        return this_py

    def Check_Python_Version(py_version):
        """
        פעןלה מקבלת גרסת פייתון מסוגה
        ("3.7")בצורה הבעה str
                ובדוקת בעזרת פייתון את גירסת פייתון
       True האם  גדולה יותר מגרסה שקיבלנו היא מחזר
        False  אחרת
        """
        version = py_version.split('.')  # הגרסה שקיבלנו
        this_py = Info_and_Install.Get_Python_Version()  # הגרסה שך המחשב

        if int(version[0]) > int(this_py[0]):
            return True
        elif int(version[0]) == int(this_py[0]) and int(version[1]) > int(this_py[1]):
            return True
        elif int(version[0]) == int(this_py[0]) and int(version[1]) == int(this_py[1]) and int(version[2]) >= int(this_py[2]):
            return True
        else:
            return False

    def Get_Platform_PC():
        """
        הפעולה מחזירה את סוג מערכת הפעלה
        ואת גרסת מערכת הפעלה בשימוש
        """
        return sys.platform

    def Pip_Install(name_package):
        """
        pip install a python3 packages
        name_package[str]: שם של החבילה
        הפעולה מחזר טקסט שכל מה שקוא בשורת הפקודה
        ואם לא עובד
        של פיתון  installה
        """
        version = Info_and_Install.Get_Platform_PC()
        if sys.platform.startswith(version):
            return os.system('pip install '+str(name_package))
        elif sys.platform.startswith(version):
            return os.system('python3 -m pip install '+str(name_package))
        else:
            return os.system("python - m ensurepip - -default-pip")

    def Install_in_File(file_name):
        """
        מקבלת מיקום של קובץ כלל השם ומוסיפה את כל ספריות בתוכו
        הפעולה מחזר רשימה שכל מה שקוא בשורת הפקודה

        """
        file_lines = [x.rstrip() for x in open(file_name)]
        for i in file_lines:
            Info_and_Install.Pip_Install(i)
        print('fins install')

    def Get_Size_File(filename):
        """
        הפעולה מקבלת קובץ
        הפעולה מחזירה את גודל קובץ
        """
        file_size = os.stat(filename)
        return file_size


if __name__ == "__main__":
    print(Info_and_Install.Get_Platform_PC())
    print(Info_and_Install.Get_Python_Version())
    Info_and_Install.Pip_Install('sys')
    # Info_and_Install.Install_in_File('requirements.txt')
