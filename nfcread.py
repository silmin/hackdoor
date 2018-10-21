import binascii
import nfc
import time
import subprocess
import idmset

isLock = True

cycleTime = 1
intervalTime = .3
waitTime = 3

reqTarget = nfc.clf.RemoteTarget("212F") #Felica
reqTarget.sensf_req = bytearray.fromhex("0000030000") #Suica

while True:
    clf = nfc.ContactlessFrontend('usb')


    resTarget = clf.sense(reqTarget, iterations=int(cycleTime//intervalTime)+1, interval=intervalTime)

    if resTarget != None:
        
        tag = nfc.tag.activate_tt3(clf, resTarget)
        tag.sys = 3

        idm = binascii.hexlify(tag.idm)
        # print 'idm : ' + idm

        if idm in idmset.dictIDm:
            if isLock:
                print 'success, hi ' + idmset.dictIDm[idm] + ' !'
                chLock = 'sudo python motor.py'
                isLock = False
            else :
                print 'success, bye ' + idmset.dictIDm[idm] + ' !'
                chLock = 'sudo python motor.py'
                isLock = True

            subprocess.call(chLock.split())
        else :
            print 'failure, i do not know idm ' + idm

        time.sleep(waitTime)
    
    clf.close()
