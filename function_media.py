from moviepy.editor import VideoFileClip, concatenate_videoclips

def final_clip(clip_files_list, clips_widh, final_clip_destination, final_clip_name):
    # Create empty list to store clips
    _clip_list = []
    # total_length
    total_length = 0
    # Look for clip with the good extension
    for clip in clip_files_list:
        # Transform the file object into video object
        video = VideoFileClip(clip).resize(width=clips_widh)
        # Add the item in the list
        _clip_list.append(video)
        #
        total_length += video.duration
    # Concatenate clips together
    print("Video length", total_length)
    final_clip = concatenate_videoclips(_clip_list)
    final_clip.write_videofile(f"{final_clip_destination}/{final_clip_name}.mp4")

