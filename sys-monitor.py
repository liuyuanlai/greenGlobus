#! /home/anl/usr/miniconda2/bin/python
from __future__ import division
import psutil, time, sys
from time import gmtime, strftime

intvl = 1
def main(argv):
    fp_net = open(argv[1], 'w')
    fp_net.write("nic,epoch,dt,rin,rout\n")

    fp_cm = open(argv[2], 'w')
    fp_cm.write("resource,epoch,dt,usage\n")

    net_io_s = psutil.net_io_counters(pernic=True)
    while True:
        time.sleep(intvl)
        net_io_e = psutil.net_io_counters(pernic=True)
        for nic in ('eno1', ):
            if net_io_s.get(nic) is None or net_io_e.get(nic) is None: continue
            net_rin   = 8.*(net_io_e[nic].bytes_recv - net_io_s[nic].bytes_recv) / intvl
            net_rout  = 8.*(net_io_e[nic].bytes_sent - net_io_s[nic].bytes_sent) / intvl
            _str = "%s,%f,%s,%f,%f\n" % (nic, time.time(), strftime("%Y-%m-%d %H:%M:%S", gmtime()), net_rin, net_rout)
            fp_net.write(_str)

        _str = "cpu,%f,%s,%f\n" % (time.time(), strftime("%Y-%m-%d %H:%M:%S", gmtime()), psutil.cpu_percent(interval=None))
        fp_cm.write(_str)

        mem_usage = psutil.virtual_memory()
        _str = "mem,%f,%s,%f\n" % (time.time(), strftime("%Y-%m-%d %H:%M:%S", gmtime()), 100.*mem_usage.used/mem_usage.total)
        fp_cm.write(_str)

        fp_net.flush()
        fp_cm.flush()
        net_io_s = net_io_e

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "please give output file names, the 1st for net, the 2nd for cpu and the 3rd for ram"
        exit()
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("Ok, I am going to save and quit")
        exit()
