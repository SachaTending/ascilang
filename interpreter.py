# this will compile and run code
import time, subprocess, platform

def cls():
    if platform.system()=="Windows":
        if platform.release() in {"10", "11"}:
            subprocess.run("", shell=True) #Needed to fix a bug regarding Windows 10; not sure about Windows 11
            return "\033c"
        else:
            subprocess.run(["cls"])
    else: #Linux and Mac
        return "\033c"

class Commands:
    # This class containing every command
    def delay(self, d: float):
        return f"delay={d}"
    def print(self, *data: tuple[str]):
        data2: str = data[0]
        if data2.endswith("\n"):
            data2 = data2.split()[0]
        #return f"buffer+=\"{data2}\\n\""
        return f"print(\"{data2}\", flush=False)"
    def cls(self, *, nul=None):
        return "print(cls(), flush=False)"
    def flush(self, *, nul=None):
        #return "sys.stdout.write(buffer);sys.stdout.flush()"
        return ""
    def nextframe(self, *, nul=None):
        return "frame+=1;print(frame, flush=False)"
    def wait(self):
        return "time.sleep(delay)"

def get(c: object, name: str, default=None):
    try:
        return c.__getattribute__(name.lower().split("\n")[0])
    except:
        return default

def handle(command: str):
    global run
    if command.startswith(('load', "LOAD")):
        print(">>> Opening...")
        file = open(command.split(" ")[1])
        print(">>> Parsing...")
        p = "delay=0.0;frame=0;buffer=\"\";import sys\n"
        c = Commands()
        while True:
            i = file.readline()
            if i == "":
                break
            #if getattr(c, i.split(" ")[0].lower(), None) != None:
            if get(c, i.split(" ")[0]) != None:
                opts = i.split(" ")
                del opts[0]
                p += get(c, i.split(" ")[0])(*opts) + "\n"
            else:
                print(f">>> Error: invalid command at {file.tell()}:")
                print(f">>> {i}")
                print(i.split(" ")[0].lower())
                break
        print(">>> Compiling...(may take some minutes)")
        run = compile(p, "asci_compiled", mode="exec")
        print(">>> Ready to run!")
        print(">>> To run, type \"run\" in console")
    elif command.startswith(('run', 'RUN')):
        try:
            exec(run)
        except KeyboardInterrupt:
            print(">>> Execution stopped.")

    elif command.startswith(('exit', "EXIT")):
        print(">>> Goodbye!")
        exit(0)
    elif command.startswith(('help', 'HELP')):
        print(">>> Avaible commands: load, run, exit, help")
    else:
        print(">>> Invalid command! Type help to get avaible commands.")

print("Welcome to ASCILang interpreter!")
print("Current commands are: load, run, exit, help")
while True:
    try:
        command = input("> ")
        handle(command)
    except KeyboardInterrupt:
        print(">>> Type exit to exit")