from moviepy.editor import VideoFileClip, concatenate_videoclips

def final_clip(clip_files_list, clips_widh, final_clip_destination, final_clip_name, length_limit=0, limit_length=False):
    # Create empty list to store clips
    _clip_list = []
    # total_length
    total_length = 0
    # Look for clip with the good extension
    # for clip in clip_files_list:
    while len(clip_files_list) != 0 :
        # Transform the file object into video object
        _the_clip = clip_files_list.pop(0)
        video = VideoFileClip(_the_clip).resize(width=clips_widh)
        # Add the item in the list
        _clip_list.append(video)
        #
        total_length += video.duration
        if limit_length and total_length > length_limit:
            break
    # Concatenate clips together
    try:
        print(f"Nb of videos : {len(_clip_list)}\nVideo length : {int(total_length)}")
        if total_length > 60:
            # print("ok")
            final_clip = concatenate_videoclips(_clip_list)
            final_clip.write_videofile(f"{final_clip_destination}/{final_clip_name}.mp4")
            return clip_files_list
        else:
            print("Video too short...")
            return []
    except:
        print(len(_clip_list))

