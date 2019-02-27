from base import *
from devices import *
import time

class NordicPCA10056(Board):
    ids_vendor = {
        "1366":frozenset(("1015",))
    }

    @staticmethod
    def match(dev):
        return dev["vid"] in NordicPCA10056.ids_vendor and dev["pid"] in NordicPCA10056.ids_vendor[dev["vid"]]

    def reset(self):
        pass

    def burn(self,bin,outfn=None):
        fatal("Mass storage burning is unreliable! Please use jtag...")
        # fname = fs.get_tempfile(bin)
        # if not self.disk:
        #     return False,"Can't find device disk! Have you mounted the DAP Link device?"
        # fs.copyfile2(fname,fs.path(self.disk,"nrf52.hex"))
        # fs.del_tempfile(fname)
        # # wait some time to allow virtualization
        # time.sleep(4/256*(len(bin)/1024))
        # info("Burned!")
        # return True,"Ok"
