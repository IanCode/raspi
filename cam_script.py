#CameraTimeLapse.py

import subprocess

def main():
    global done
    if (len(sys.argv)==2):
        bt_data     = get_data_from_torrent(sys.argv[1])
        info_hash   = get_info_hash(bt_data)
        # call tracker request
        tracker_req(bt_data, info_hash)
    else:
        print('incorrect number of arguments')


if __name__=="__main__":
    main()