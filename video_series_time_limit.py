from function_media import final_clip
from largefunctions import clips_list_random_complex

path_lecture = ""
path_to_scrap = ""
video_width = 500
movie_nb = 4

def time_limit_vids(clips_directory, nb_seq, broadness, destination_directory, length_limit, video_name):
    # Start the process
    _videos_list = [f"{clips_directory}/{i}" for i in clips_list_random_complex(clips_directory)]
    #
    _test_list = _videos_list.copy()
    #
    _n = 1
    #
    while _n < nb_seq and len(_test_list) > 0:
        print(_n)
        # Create the sequence
        _test_list = final_clip(_test_list, broadness, destination_directory, f"{video_name}_{_n}", length_limit, limit_length=True)
        #
        _n += 1

if __name__ == "__main__":
    # Start the process
    time_limit_vids(path_to_scrap, movie_nb, video_width, path_lecture, 200, "ogsm")
