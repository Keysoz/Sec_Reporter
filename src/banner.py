from sys import stdout
from time import sleep
class Colors:
    def __init__(self):
        self.CRED2 = "\33[91m"
        self.CBLUE2 = "\33[94m"
        self.CGREEN2 = "\033[32m"
        self.CYELLOW2 = "\033[93m"
        self.CPURPLE2 = '\033[0;35m' 
        self.CCYAN2 = "\033[36m"
        self.ENDC = "\033[0m"
        
Color = Colors()

def banner():
    font = f"""{Color.CBLUE2}
██╗███╗   ██╗███████╗ ██████╗ ███████╗███████╗ ██████╗    ██╗    ██╗██████╗ ██╗████████╗███████╗    ██╗   ██╗██████╗ ███████╗
██║████╗  ██║██╔════╝██╔═══██╗██╔════╝██╔════╝██╔════╝    ██║    ██║██╔══██╗██║╚══██╔══╝██╔════╝    ██║   ██║██╔══██╗██╔════╝
██║██╔██╗ ██║█████╗  ██║   ██║███████╗█████╗  ██║         ██║ █╗ ██║██████╔╝██║   ██║   █████╗█████╗██║   ██║██████╔╝███████╗
██║██║╚██╗██║██╔══╝  ██║   ██║╚════██║██╔══╝  ██║         ██║███╗██║██╔══██╗██║   ██║   ██╔══╝╚════╝██║   ██║██╔═══╝ ╚════██║
██║██║ ╚████║██║     ╚██████╔╝███████║███████╗╚██████╗    ╚███╔███╔╝██║  ██║██║   ██║   ███████╗    ╚██████╔╝██║     ███████║
╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚══════╝╚══════╝ ╚═════╝     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝     ╚═════╝ ╚═╝     ╚══════╝
{Color.ENDC}                                                                                                                             


    """
    credit = f"{Color.CBLUE2}>{Color.ENDC} InfoSec Write-ups Tool Made By @Keysoz {Color.ENDC}\n\n"
    
    for col in font:
        print(col, end="")
        stdout.flush()
        sleep(0.001)
    
    for col in credit:
        print(col, end="")
        stdout.flush()
        sleep(0.028)
        
def Options():
    opts = [
        f"{Color.CCYAN2}      [1]{Color.ENDC} Get Write-Ups Published Today",
        f"{Color.CPURPLE2}      [2]{Color.ENDC} Search For A Topic",
        f"{Color.CRED2}      [3]{Color.ENDC} Close The Script"]
    
    for col in opts:
        print(col, end="\n")
        stdout.flush()
        sleep(0.050)
        
def main():
    banner()
    Options()
    print("\n")
    
if __name__=="__main__":
    main()