fin = open('memory', 'rb')
memory = []
for temp in fin:
    k = temp.find(':')
    temp = temp[k+2:]
    line = temp.strip('\r\n').split(' ')
    for item in line:
        if item != '':
            memory.append(int(item, 16))
fin.close()
fin = open('disk', 'rb')
disk = []
for temp in fin:
    k = temp.find(':')
    temp = temp[k+2:]
    line = temp.strip('\r\n').split(' ')
    for item in line:
        if item != '':
            disk.append(int(item, 16))
fin.close()

pdbr = 0xd80
va = ['6653', '1c13', '6890', '0af6', '1e6f']
for addr in va:
    print 'Virtual Address ' + addr + ':\n'
    num = int(addr, 16)
    a = (num & 0x7c00) >> 10
    b = (num & 0x3e0) >> 5
    c = num & 0x1f
    print 'pde index:' + str(hex(a))
    pde = memory[pdbr + a]
    valid = (pde & 0x80) >> 7
    pde = pde & 0x7f
    print '  pde contents:(valid ' + str(valid) + ', pfn ' + str(hex(pde)) +')\n'
    if valid == 0:
        print 'Fault (page directory entry not valid)\n'
    else:
        d = (pde << 5) + b
        pte = memory[d]
        valid = (pte & 0x80) >> 7
        pte = pte & 0x7f
        pa = (pte << 5) + c
        print 'pte index:' + str(hex(b)) + '  pte content:(valid ' + str(valid) + ', pfn ' + str(hex(pte)) + ')\n'
        if valid == 0:
            print 'To Disk Sector Address ' + str(hex(pa)) + ' --> Value: ' + str(hex(disk[pa])) + '\n'
        else:
            print 'Translate to Physical Address ' + str(hex(pa)) + ' --> Value: ' + str(hex(memory[pa])) + '\n'
