import os
import subprocess
import psutil
import sqlite3

name = os.getlogin()
username = ""
memory = ""
xmx = "-Xms"
mb = "M"
title = """
 ███████      ██     ███████       ██     ███████     ███████   ██     ██
░██░░░░██    ████   ░██░░░░██     ████   ░██░░░░██   ██░░░░░██ ░░██   ██ 
░██   ░██   ██░░██  ░██   ░██    ██░░██  ░██    ░██ ██     ░░██ ░░██ ██  
░███████   ██  ░░██ ░███████    ██  ░░██ ░██    ░██░██      ░██  ░░███   
░██░░░░   ██████████░██░░░██   ██████████░██    ░██░██      ░██   ██░██  
░██      ░██░░░░░░██░██  ░░██ ░██░░░░░░██░██    ██ ░░██     ██   ██ ░░██ 
░██      ░██     ░██░██   ░░██░██     ░██░███████   ░░███████   ██   ░░██
░░       ░░      ░░ ░░     ░░ ░░      ░░ ░░░░░░░     ░░░░░░░   ░░     ░░ 
"""

auth_user = ""
pass_user = ""

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL)''')
conn.commit()

def register():
    print("\nРегистрация нового пользователя")
    new_user = input("Введите логин: ")
    new_pass = input("Введите пароль: ")
    
    cursor.execute("SELECT * FROM users WHERE username = ?", (new_user,))
    if cursor.fetchone():
        print("Пользователь с таким именем уже существует!")
        return
    
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_user, new_pass))
    conn.commit()
    print("Регистрация успешна!")

def _auth():
    print(title)
    
    print("\n[1] Авторизация.")
    print("[2] Регистрация.")
    print("[3] Выход.")
    
    choice = input("\nВыбор действия: ")
    
    if choice == "1":
        auth_user = input("Введите логин: ")
        pass_user = input("Введите пароль: ")
        
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (auth_user, pass_user))
        if cursor.fetchone():
            print("Авторизация успешна!")
            start()
        else:
            print("Неверный логин или пароль!")
    elif choice == "2":
        register()
    elif choice == "3":
        exit()
    else:
        print("Недоступный выбор...")

def start():
    while True:
        print(title)
        
        print("\n[1] Запуск игры.")
        print("[2] Смена оперативки.")
        print("[3] Изменить никнейм.")
        print("\n[WARNING] Перед запуском смените имя и память!")
    
        choise = input("\nВыбор действия: ")
        
        if choise == "1":
            subprocess.run('"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/openjdk/jdk8u372-b07-jre/bin/java.exe"-XX:-UseAdaptiveSizePolicy -XX:-OmitStackTraceInFastThrow -Dfml.ignorePatchDiscrepancies=true -Dfml.ignoreInvalidMinecraftCertificates=true -Djava.library.path="C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/natives/1.12.2" '+xmx+memory+mb+' -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Dminecraft.api.auth.host=http://127.0.0.1 -Dminecraft.api.account.host=http://127.0.0.1 -Dminecraft.api.session.host=http://127.0.0.1 -Dminecraft.api.services.host=http://127.0.0.1 -Dlog4j.configurationFile=log4j2_112-116.xml -cp "C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/com/google/code/gson/gson/2.8.0/gson-2.8.0.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/com/google/guava/guava/21.0/guava-21.0.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/com/ibm/icu/icu4j-core-mojang/51.2/icu4j-core-mojang-51.2.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/com/mojang/authlib/1.5.25/authlib-1.5.25.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/com/mojang/patchy/1.3.9/patchy-1.3.9.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/com/mojang/realms/1.10.22/realms-1.10.22.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/com/mojang/text2speech/1.10.3/text2speech-1.10.3.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/com/paulscode/codecjorbis/20101023/codecjorbis-20101023.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/com/paulscode/codecwav/20101023/codecwav-20101023.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/com/paulscode/libraryjavasound/20101123/libraryjavasound-20101123.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/com/paulscode/librarylwjglopenal/20100824/librarylwjglopenal-20100824.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/com/paulscode/soundsystem/20120107/soundsystem-20120107.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/com/typesafe/akka/akka-actor_2.11/2.3.3/akka-actor_2.11-2.3.3.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/com/typesafe/config/1.2.1/config-1.2.1.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/commons-codec/commons-codec/1.10/commons-codec-1.10.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/commons-io/commons-io/2.5/commons-io-2.5.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/io/netty/netty-all/4.1.9.Final/netty-all-4.1.9.Final.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/it/unimi/dsi/fastutil/7.1.0/fastutil-7.1.0.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/java3d/vecmath/1.5.2/vecmath-1.5.2.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/lzma/lzma/0.0.1/lzma-0.0.1.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/net/java/dev/jna/jna/4.4.0/jna-4.4.0.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/net/java/dev/jna/platform/3.4.0/platform-3.4.0.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/net/java/jinput/jinput/2.0.5/jinput-2.0.5.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/net/java/jutils/jutils/1.0.0/jutils-1.0.0.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/net/minecraft/launchwrapper/1.12/launchwrapper-1.12.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/net/minecraftforge/forge/1.12.2-14.23.5.2860/forge-1.12.2-14.23.5.2860.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/net/sf/jopt-simple/jopt-simple/5.0.3/jopt-simple-5.0.3.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/net/sf/trove4j/trove4j/3.0.3/trove4j-3.0.3.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/apache/commons/commons-lang3/3.5/commons-lang3-3.5.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/apache/httpcomponents/httpclient/4.3.3/httpclient-4.3.3.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/apache/logging/log4j/log4j-api/2.15.0/log4j-api-2.15.0.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/apache/logging/log4j/log4j-api/2.8.1/log4j-api-2.8.1.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/apache/logging/log4j/log4j-core/2.15.0/log4j-core-2.15.0.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/apache/logging/log4j/log4j-core/2.8.1/log4j-core-2.8.1.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/apache/maven/maven-artifact/3.5.3/maven-artifact-3.5.3.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/jline/jline/3.5.1/jline-3.5.1.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/lwjgl/lwjgl/lwjgl-platform/2.9.4-nightly-20150209/lwjgl-platform-2.9.4-nightly-20150209.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/lwjgl/lwjgl/lwjgl/2.9.4-nightly-20150209/lwjgl-2.9.4-nightly-20150209.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/lwjgl/lwjgl/lwjgl_util/2.9.4-nightly-20150209/lwjgl_util-2.9.4-nightly-20150209.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/ow2/asm/asm-debug-all/5.2/asm-debug-all-5.2.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/scala-lang/plugins/scala-continuations-library_2.11/1.0.2_mc/scala-continuations-library_2.11-1.0.2_mc.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/scala-lang/plugins/scala-continuations-plugin_2.11.1/1.0.2_mc/scala-continuations-plugin_2.11.1-1.0.2_mc.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/scala-lang/scala-actors-migration_2.11/1.1.0/scala-actors-migration_2.11-1.1.0.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/scala-lang/scala-compiler/2.11.1/scala-compiler-2.11.1.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/scala-lang/scala-library/2.11.1/scala-library-2.11.1.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/scala-lang/scala-parser-combinators_2.11/1.0.1/scala-parser-combinators_2.11-1.0.1.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/scala-lang/scala-reflect/2.11.1/scala-reflect-2.11.1.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/scala-lang/scala-swing_2.11/1.0.1/scala-swing_2.11-1.0.1.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/org/scala-lang/scala-xml_2.11/1.0.2/scala-xml_2.11-1.0.2.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/libraries/oshi-project/oshi-core/1.1/oshi-core-1.1.jar";"C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/versions/TechnoLog/TechnoLog.jar" net.minecraft.launchwrapper.Launch --username '+username+' --version 1.12.2 --gameDir "C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/versions/TechnoLog" --assetsDir "C:/Users/'+name+'/AppData/Roaming/.TechnoLog/minecraft/minecraft/assets" --assetIndex TechnoLog --uuid 63851d6b-7ab0-34fa-b351-eb17d382cf0f --accessToken 63851d6b-7ab0-34fa-b351-eb17d382cf0f --userType mojang --tweakClass net.minecraftforge.fml.common.launcher.FMLTweaker --versionType Forge')
        elif choise == "2":
            memory_info = psutil.virtual_memory()
            total_memory = memory_info.total // (1024 ** 2) 
            print(total_memory // 4)
            memory = input("Введите кол-во оперативки: ")
            print("Вы выделили - ", memory)
        elif choise == "3":
            username = input("Введите никнейм: ")
            print("Ваш новый никнейм - ", username)
    
if __name__ == "__main__":
    _auth()