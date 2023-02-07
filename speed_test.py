#pip install speedtest-cli
import speedtest
def spd_test():
    st = speedtest.Speedtest()

    print("Testing Download")
    download_mbps = round((st.download())/10**6,2)

    print("Testing Upload")
    upload_mbps = round((st.upload())/10**6,2)

    return download_mbps, upload_mbps

if __name__ == '__main__':
    download, upload = spd_test()
    print(f"Download Speed : {download}")
    print(f"Upload Speed : {upload}")
