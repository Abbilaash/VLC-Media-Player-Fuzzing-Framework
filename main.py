import os
from winappdbg.winappdbg import Debug, EventHandler

class CrashHandler(EventHandler):
    def __init__(self, log_file):
        super().__init__()
        self.log_file = log_file

    def create_log(self, event):
        crash = event.get_crash()
        if crash is not None:
            with open(self.log_file, "w") as log:
                log.write("Crash detected!\n")
                log.write(f"Process ID: {event.get_pid()}\n")
                log.write(f"Exception Code: {hex(crash.get_exception_code())}\n")
                log.write(f"Fault Address: {hex(crash.get_fault_address())}\n")
                log.write("Registers:\n")
                for reg, value in crash.get_registers().items():
                    log.write(f"  {reg}: {hex(value)}\n")
                log.write("Stack Trace:\n")
                for frame in crash.get_stack_trace():
                    log.write(f"  {frame}\n")
                log.write("\n")

    def on_exception(self, event):
        self.create_log(event)

# Step 2: Run VLC with debugger attached
def debug_vlc_with_file(vlc_path: str, file_path: str, log_file: str):
    handler = CrashHandler(log_file)
    debugger = Debug(handler)

    try:
        # Start VLC process with debugger
        print(f"Starting VLC with file: {file_path}")
        debugger.execv([vlc_path, file_path])
        print(f"Debugger attached to VLC process. Monitoring for crashes...")

        # Run the debugger and monitor for crashes or exceptions
        debugger.loop()
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        print("Debugger loop ended.")


vlc_path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
file_path = "modules/malformed_sample.mp4"


debug_vlc_with_file(vlc_path, file_path, "modules/crash_log.txt")

