"""
Set an alarm to take a break by playing a youtube video
"""
import webbrowser
import time


def main():
    """
    Test function
    :return: none
    """
    video_address = "https://youtu.be/aJg4OJxp-co"
    counter = 0
    while counter < 3:
        # Delay "sleep"
        time.sleep(60*60)  # 1 hr
        webbrowser.open(video_address)
        counter += 1
        print("It is time to take a break, is: ", time.ctime())


if __name__ == '__main__':
    main()
    exit(0)