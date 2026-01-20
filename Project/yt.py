def list_all_videos(videos):
    pass

def add_video(video):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

while True:
    print("\n Youtube manager")
    print("1.list all youtube videos")
    print("2.add a youtube video")
    print("3.update a youtube video")
    print("4.delete a youtube video")
    choice = input("enter your choice")

    match choice:
        case "1":
            list_all_videos(videos)

        case "2":
            add_video(videos)

        case "3":
            update_video(videos)

        case "4":
            delete_video(videos)
