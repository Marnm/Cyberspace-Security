#!/usr/bin/python3
# _*_ code:utf-8 _*_

import F1   # socket
import F2   # time
from scapy.all import *
import F3   # optparse
#FLAG1=F1.F2.F3

def tcpconnscan(host, port):
    try:
        conn = socket.FLAG4(socket.F4, socket.F5)
        # socket AF_INET SOCK_STREAM
        conn.connect((host, port))
        print '[+]%d/tcp open'% port
        conn.close()
    except:
        pass
    #FLAG2=F4.F5
    
    def udpconnscan(host, port):
        try:
            rep = sr1(F6(dst=host)/F7(dport=port), timeout=1, verbose=0)
            # IP UDP
            time.sleep(1)
            if (rep.FLAG5(F8)):
                # haslayer(ICMP)
                print '[-]%d/udp not open'% port
                # FLAG3=F6.F7.F8
                
def portscan(host):
    for FLAG6 in range(1,1023)
    # port
        tcpconnscan(host, port)
        
def main():
    parser = optparse.OptionParser('usage%prog '+'-H <target host>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    (options, args) = F9.parse_args()   #parser
    host = options.F10  # tgtHost
    if host == None:
        print F9.usage  # parser
        exit(0)
    portscan(host)
    #FLAG7 = F9.F10
    
if __name__ == '__main__':
    main()
        
        
