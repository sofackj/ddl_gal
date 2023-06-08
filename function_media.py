from moviepy.editor import VideoFileClip, concatenate_videoclips

def final_clip(clip_files_list, clips_widh, final_clip_destination):
    # Create empty list to store clips
    _clip_list = []
    # Look for clip with the good extension
    for clip in clip_files_list:
        # Transform the file object into video object
        video = VideoFileClip(clip).resize(width=clips_widh)
        # Add the item in the list
        _clip_list.append(video)
    # Concatenate clips together
    final_clip = concatenate_videoclips(_clip_list)
    final_clip.write_videofile(f"{final_clip_destination}/my_concatenation.mp4")

