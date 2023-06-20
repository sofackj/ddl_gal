import os
from function_second import random_items_complex_list
from function_media import final_clip

path_lecture = ""
path_to_scrap = ""
pic_broadness = 500

'''
What you need :
==> The directory should contain video clips
    -> For the same serie you need this pattern SERIENAME_SUBNAME
    -> One shot : NAME is enough  
'''

def video_seq_maker(images_destination_path, images_targeted, broadness, pics_number=10, files_number=9):
    # List all folders containing images
    _clips_list = [item for item in os.listdir(images_targeted)]
    # Determine the series number
    series_nb = len(set([("_").join(clip.split('_')[:-1]) for clip in _clips_list]))
    print(f"Clips number\t=>\t{len(_clips_list)}\nSeries number\t=>\t{series_nb}")
    # Increment for the temp directory (pattern -> test_clip_n)
    n = 1
    ### Start of the loop ######################################################
    while series_nb >= pics_number and n <= files_number:
        # Generate a list of a number of directories in the previous list
        _clips_list, lecture_list = random_items_complex_list(pics_number, _clips_list)
        #
        lecture_list = [f"{images_targeted}/{i}" for i in lecture_list]
        print()
        print(f'=== Generating video file <{n}> =======================================')
        # Create the directory
        final_clip(lecture_list, broadness, images_destination_path, f"test_clip_{n}")
        # Increment of 1 for the next directory
        n += 1
        # Check the condition for the loop
        series_nb = len(set([("_").join(clip.split('_')[:-1]) for clip in _clips_list]))
 
if __name__ == "__main__":
    # Start the process
    # Build the architecture
    video_seq_maker(path_lecture, path_to_scrap, pic_broadness, 20, 4)
    pass