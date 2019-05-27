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

    def _exe_jlink_script(self, jlink_script_content):
        jlink_script = fs.get_tempfile(jlink_script_content)
        res,out,err = proc.runcmd("jlinkexe", "-If", "swd", "-device", "nRF52840_xxAA", "-speed", "4000", "-autoconnect", "1", "-CommanderScript", jlink_script)
        fs.del_tempfile(jlink_script)
        return out

    def reset(self):
        self._exe_jlink_script('r\nexit')

    def burn(self,bin,outfn=None):
        vm_bin = fs.get_tempfile(bin)
        out = self._exe_jlink_script('loadbin "' + vm_bin + '", '+ self.to_dict()["vm_start"] +'\nr\nexit')
        fs.del_tempfile(vm_bin)

        for line in out.split('\n'):
            if 'O.K.' in line:
                break
        else:
            return False,out
        return True,out
